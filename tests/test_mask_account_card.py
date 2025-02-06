from src.masks import get_mask_account
import pytest
def test_get_mask_account():
    assert get_mask_account('73654108430135874305') == '**4305'
    assert get_mask_account('7365410843013587430500') == 'Номера счета состоит из 20 символов'
    assert get_mask_account('73654108430135 874305') == 'Введен некорректный номер счета'
    assert get_mask_account('736541084301а 35874305') == 'Введен некорректный номер счета'
    with pytest.raises(TypeError):
        get_mask_account()