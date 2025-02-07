import pytest
from src.processing import filter_by_state


def test_filter_by_state_non_status(test_filter_by_state_non):
    assert (
        filter_by_state(
            [
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                },
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                },
                {
                    "id": 615064591,
                    "state": "CANCELED",
                    "date": "2018-10-14T08:21:33.419441",
                },
            ]
        )
        == test_filter_by_state_non
    )


def test_filter_by_state_by_status(test_filter_by_state_canceled):
    assert (
        filter_by_state(
            [
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                },
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                },
                {
                    "id": 615064591,
                    "state": "CANCELED",
                    "date": "2018-10-14T08:21:33.419441",
                },
            ],
            "CANCELED",
        )
        == test_filter_by_state_canceled
    )


@pytest.mark.parametrize(
    "value, status, expected",
    [
        (
            [
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                },
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                },
                {
                    "id": 615064591,
                    "state": "CANCELED",
                    "date": "2018-10-14T08:21:33.419441",
                },
            ],
            "EXECUTED",
            [
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                },
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                },
            ],
        ),
        (
            (
                [
                    {
                        "id": 41428829,
                        "state": "EXECUTED",
                        "date": "2019-07-03T18:35:29.512364",
                    },
                    {
                        "id": 939719570,
                        "state": "EXECUTED",
                        "date": "2018-06-30T02:08:58.425572",
                    },
                    {
                        "id": 594226727,
                        "state": "CANCELED",
                        "date": "2018-09-12T21:27:25.241689",
                    },
                    {
                        "id": 615064591,
                        "state": "CANCELED",
                        "date": "2018-10-14T08:21:33.419441",
                    },
                ],
                "CANCELED",
                [
                    {
                        "id": 594226727,
                        "state": "CANCELED",
                        "date": "2018-09-12T21:27:25.241689",
                    },
                    {
                        "id": 615064591,
                        "state": "CANCELED",
                        "date": "2018-10-14T08:21:33.419441",
                    },
                ],
            )
        ),
    ],
)
def test_filter_by_state_parametrize(value, status, expected):
    assert filter_by_state(value, status) == expected

    with pytest.raises(TypeError):
        filter_by_state()
        filter_by_state([])
        filter_by_state(6546846165)
        filter_by_state('')

