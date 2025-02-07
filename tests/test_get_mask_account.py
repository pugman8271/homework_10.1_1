import pytest

from src.widget import mask_account_card


def test_mask_account_card():
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
def test_mask_account_card(value, expect):

    assert mask_account_card(value) == expect
