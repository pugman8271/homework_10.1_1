import pytest


@pytest.fixture()
def data_test():
    return "11.03.2024"


@pytest.fixture()
def data_test_non_standart():
    return "Дата введена некорректно, введите в формате: ДД.ММ.ГГГГ"


############################################
@pytest.fixture()
def numbers():
    return "7000 79** **** 6361"


@pytest.fixture()
def numbers_19():
    return "7000 79** **** 6122"


@pytest.fixture()
def numbers_13():
    return "7000 79** **** 8960"


@pytest.fixture()
def numbers_space():
    return "Введен некорректный номер карты"


############################################


@pytest.fixture
def card_data():
    return [
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ]


############################################


@pytest.fixture
def mask_account():
    return "**4305"


@pytest.fixture
def mask_account_non_20():
    return "Номера счета состоит из 20 символов"


@pytest.fixture
def mask_account_space():
    return "Введен некорректный номер счета"


@pytest.fixture
def mask_account_letter():
    return "Введен некорректный номер счета"


@pytest.fixture
def test_filter_by_state_non():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def test_filter_by_state_canceled():
    return [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def date():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def date_similar():
    return [
        {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T21:27:25.241689"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T08:21:33.419441"},
        {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T02:08:58.425572"},
    ]


@pytest.fixture
def date_revers():
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.fixture
def non_standart():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019/07/03"},
        {"id": 615064591, "state": "CANCELED", "date": "2018/10/14"},
        {"id": 594226727, "state": "CANCELED", "date": "2018/09/12"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018/06/30"},
    ]
