from src.decorators import log
import pytest


def test_decorators_log_console_error(capsys):
    @log(None)
    def foo(x, y):
        return x + y

    with pytest.raises(TypeError):
        foo(2, "5")
    captured  = capsys.readouterr()
    assert captured.out  == "Ошибка foo TypeError ((2, '5'), {})\n\n"

def test_decorators_log_console_succsess(capsys):
    @log(None)
    def foo(x, y):
        return x + y
    foo(2,5)
    captured = capsys.readouterr()
    assert captured.out == 'foo ok \n\n'

def test_decorators_log_succsess():

    @log(filename='mylog.txt')
    def foo(x, y):
        return x + y

    foo(2,5)
    with open('mylog.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        last_line = lines[-1]
        expected = last_line
    assert expected == 'foo ok \n'