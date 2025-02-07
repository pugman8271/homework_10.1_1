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
