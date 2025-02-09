import pytest

from src.widget import get_date, mask_account_card


def test_get_data_normal(data_test: str) -> None:
    assert get_date("2024-03-11T02:26:18.671407") == data_test


def test_get_data_non_normal(data_test_non_standart: str) -> None:
    assert get_date("дата - 11.03.2024") == data_test_non_standart


def test_mask_account_card() -> None:
    with pytest.raises(TypeError):
        mask_account_card()


@pytest.mark.parametrize(
    "value, expect",
    [
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ],
)
def test_mask_card_number(value: str, expect: str, card_data: str) -> None:
    assert mask_account_card(value) == expect
