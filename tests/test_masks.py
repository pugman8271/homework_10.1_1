import pytest

from src.masks import get_mask_card_number


def test_get_mask_card_number(numbers):
    assert get_mask_card_number("7000792289606361") == numbers


def test_get_mask_card_numbers_19(numbers_19):
    assert get_mask_card_number("700079228960636122") == numbers_19


def test_get_mask_card_numbers_13(numbers_13):
    assert get_mask_card_number("700079228960") == numbers_13


def test_get_mask_card_numbers_space(numbers_space):
    assert get_mask_card_number("70007922 8960") == numbers_space

    with pytest.raises(TypeError):
        get_mask_card_number()


import pytest

from src.masks import get_mask_account


def test_get_mask_account(mask_account):
    assert get_mask_account("73654108430135874305") == mask_account


def test_get_mask_account_non_20(mask_account_non_20):
    assert get_mask_account("7365410135874305") == mask_account_non_20


def test_get_mask_account_space(mask_account_space):
    assert get_mask_account("73654101 874305") == mask_account_space


def test_get_mask_account_letter(mask_account_letter):
    assert get_mask_account("73654146sasdw") == mask_account_letter

    with pytest.raises(TypeError):
        get_mask_account()
