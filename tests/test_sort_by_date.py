
from src.processing import sort_by_date


def test_sort_by_date(date):
    expected = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    result = sort_by_date(date)
    assert result == expected


def test_sort_by_date_similar(date_similar):
    expected = [
        {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T21:27:25.241689"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T08:21:33.419441"},
        {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T02:08:58.425572"},
    ]
    result = sort_by_date(date_similar)
    assert result == expected


def test_sort_by_date_revers(date_revers):
    expected = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    result = sort_by_date(date_revers, True)
    assert result == expected


def test_sort_by_date_non_standart(non_standart):
    expected = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019/07/03"},
        {"id": 615064591, "state": "CANCELED", "date": "2018/10/14"},
        {"id": 594226727, "state": "CANCELED", "date": "2018/09/12"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018/06/30"},
    ]
    result = sort_by_date(non_standart)
    assert result == expected
