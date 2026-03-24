import pytest
import requests
from src.calculator import add, subtract, multiply, divide


# Basic unit tests — one assertion each
def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(3, 4) == 12


def test_divide():
    assert divide(10, 2) == 5.0


# Replaces writing 4 identical test functions
@pytest.mark.parametrize("a, b, expected", [
    (2,   3,   5),    # positive
    (0,   0,   0),    # zeros
    (-1,  1,   0),    # negative
    (100, -50, 50),   # large values
])
def test_add_cases(a, b, expected):
    assert add(a, b) == expected


# Test that an exception IS raised
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)


# Apply multiple markers to one test

@pytest.mark.external
@pytest.mark.slow
def test_weather_api():
    resp = requests.get("https://openweathermap.org/api")
    assert resp.status_code == 200
