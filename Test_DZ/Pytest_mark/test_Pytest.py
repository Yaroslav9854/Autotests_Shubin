import pytest

@pytest.mark.parametrize("a, b, expected", [
    (2, 2, 4),   # позитивный кейс
    (1, 1, 2),   # позитивный кейс
    (0, 0, 0),   # граничный случай
    (-1, 1, 0),  # позитивный кейс
    (2, 2, 5),   # негативный кейс — намеренно неверное ожидание
])
def test_sum(a, b, expected):
    assert a + b == expected