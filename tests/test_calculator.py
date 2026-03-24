import pytest
from src.calculator import add, subtract, multiply, divide

# Basic unit tests — one assertion each
def test_add():        assert add(2, 3) == 5
def test_subtract():  assert subtract(5, 3) == 2
def test_multiply():  assert multiply(3, 4) == 12
def test_divide():    assert divide(10, 2) == 5.0

# Test that an exception IS raised
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)

# Marked — skipped in CI, runs nightly on schedule
@pytest.mark.external
def test_external_api():
    pass  # placeholder for live API call

