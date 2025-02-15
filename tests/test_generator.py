from generators.generator import filter_by_currency, transaction_descriptions, card_number_generator
import pytest


def test_filter_by_currency(transactions):
    usd_transactions_list = list(filter_by_currency(transactions))
    assert {transaction["date"] for transaction in usd_transactions_list} =={'2018-06-30T02:08:58.425572',
 '2018-08-19T04:27:37.904916',
 '2019-04-04T23:20:05.206878'}

    rub_transactions_list = list(filter_by_currency(transactions, "RUB"))
    assert {transaction["id"] for transaction in rub_transactions_list} == {873106923, 594226727}

    no_currency_transactions_list = list(filter_by_currency(transactions, "EURO"))
    assert no_currency_transactions_list == []

    empty_transactions_list = list(filter_by_currency([], "USD"))
    assert empty_transactions_list == []



def test_transaction_descriptions(transactions):
    descriptions_list = list(transaction_descriptions(transactions))
    expected_descriptions = ['Перевод организации',
    'Перевод со счета на счет',
    'Перевод со счета на счет',
    'Перевод с карты на карту',
    'Перевод организации']
    assert descriptions_list == expected_descriptions

    empty_descriptions_list = list(transaction_descriptions([]))
    assert empty_descriptions_list == []

@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        )])

def test_card_number_generator(start, stop, expected):
    generated_numbers = list(card_number_generator(start, stop))
    assert generated_numbers == expected
    assert list(card_number_generator(10000000000, 10000000000)) == ["0000 0100 0000 0000"]
    assert list(card_number_generator(1, 1)) == ['0000 0000 0000 0001']


