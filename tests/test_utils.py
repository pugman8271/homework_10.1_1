from src.utils import operations_json_get_info


def test_operations_json_get_info_correct(transactions_json):
    assert operations_json_get_info("data/operations.json") == transactions_json


def test_operations_json_get_info_incorrect(transactions_json):
    assert operations_json_get_info("") == []
    assert operations_json_get_info("///") == []
    assert operations_json_get_info(".data.operations.json") == []
