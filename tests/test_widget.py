import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize('value, expected', [
    ('Visa Platinum 7000792289606361', 'Visa Platinum 7000 79** **** 6361'),
    ('Счет 73654108430135874305', 'Счет **4305'),
    ('Счет 6468647367889477958900', 'Счет **8900'),
    ('MasterCard 7158300734726758', 'MasterCard 7158 30** **** 6758'),
    ('Visa Classic 683198247673765800', 'Введен некорректный номер')
])
def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected


@pytest.mark.parametrize('value, expected', [
    ('2024-03-11T02:26:18.671407', '11-03-2024'),
    ('2023/12/25T00:00:00.000000', '25/12/2023'),
    ('2023.12.25T00:00:00.000000', '25.12.2023'),
    ('2024-03/11T02:26:18.671407', 'Дата не распознана'),
    ('', 'Дата не распознана'),
    ('2024/03/11', '11/03/2024'),
    ('abcd-ef-gh', 'Дата не распознана'),
    ('дата 2024-03-11', '11-03-2024')
])
def test_get_date(value, expected):
    assert get_date(value) == expected
