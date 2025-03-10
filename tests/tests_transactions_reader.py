import os
from unittest.mock import patch
import pandas as pd


from src.transactions_reader import transactions_reader_csv, transactions_reader_xlsx


@patch('csv.DictReader')
def test_transactions_reader_csv(mock_test):
    mock_test.return_value = [{'id': 'test_id', 'state': 'test_state'}]
    assert transactions_reader_csv('../transactions.csv') == [{'id': 'test_id', 'state': 'test_state'}]


@patch('src.transactions_reader.pd.read_excel')
def test_transactions_reader_xlsx(mock_test):
    mock_test.return_value = pd.DataFrame([{'id': 'test_id', 'state': 'test_state'}])
    assert transactions_reader_xlsx('../transactions_excel.xlsx') == [{'id': 'test_id', 'state': 'test_state'}]