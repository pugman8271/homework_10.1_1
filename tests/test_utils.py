from src.utils import operations_json_get_info


def test_operations_json_get_info_correct(transactions_json):
    assert operations_json_get_info("data/operations.json") == transactions_json


def test_operations_json_get_info_incorrect(transactions_json):
    assert operations_json_get_info("") == 'файл не найден'
    assert operations_json_get_info("///") == 'файл не найден'
    assert operations_json_get_info(".data.operations.json") == 'файл не найден'
    assert operations_json_get_info(1) == []
    assert operations_json_get_info('tests/operations_test_empty.json') == []
