import pytest


@pytest.fixture()
def data_test():
    return "11.03.2024"


@pytest.fixture()
def data_test_non_standart():
    return "Дата введена некорректно, введите в формате: ДД.ММ.ГГГГ"
