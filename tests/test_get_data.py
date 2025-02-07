from src.widget import get_date


def test_get_data_normal(data_test):
    assert get_date("2024-03-11T02:26:18.671407") == data_test


def test_get_data_non_normal(data_test_non_standart):
    assert get_date("дата - 11.03.2024") == data_test_non_standart
