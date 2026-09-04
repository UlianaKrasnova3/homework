import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize('value, expected', [
    ('7000792289606361', '7000 79** **** 6361'),
    ('700079228960636100', 'Введен некорректный номер'),
    ('', 'Введен некорректный номер')
])
def test_get_mask_card_number(value, expected):
    assert get_mask_card_number(value) == expected


@pytest.mark.parametrize('value, expected', [
    ('73654108430135874305', '**4305'),
    ('700079228960636100', '**6100'),
    ('', 'Введен некорректный номер')
])
def test_get_mask_account(value, expected):
    assert get_mask_account(value) == expected
