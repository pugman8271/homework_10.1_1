from src.masks import get_mask_card_number
import pytest
def test_get_mask_card_number():
    assert get_mask_card_number('7000792289606361') == '7000 79** **** 6361'
    assert get_mask_card_number('700079228960636122') == '7000 79** **** 6122'
    assert get_mask_card_number('700079228960') == '7000 79** **** 8960'
    assert get_mask_card_number('70007922 8960') == 'Введен некорректный номер карты'
    with pytest.raises(TypeError):
        get_mask_card_number()


