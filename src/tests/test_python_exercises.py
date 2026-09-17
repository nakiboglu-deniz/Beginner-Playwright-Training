import pytest

from python_exercises import (
    is_prime,
    add,
    subtract,
    multiply,
    divide,
    get_even_numbers,
    get_even_numbers_comprehension,
)


# Exercise 1 Tests
def test_prime_numbers():
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(5) is True
    assert is_prime(7) is True
    assert is_prime(13) is True


def test_non_prime_numbers():
    assert is_prime(0) is False
    assert is_prime(1) is False
    assert is_prime(4) is False
    assert is_prime(9) is False
    assert is_prime(15) is False


# Exercise 2 Tests
def test_add():
    assert add(5, 3) == 8
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(3, 5) == -2


def test_multiply():
    assert multiply(4, 5) == 20
    assert multiply(-2, 3) == -6


def test_divide():
    assert divide(10, 2) == 5
    assert divide(7, 2) == 3.5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


# Exercise 3 Tests
def test_even_numbers_loop():
    result = get_even_numbers()

    assert result[0] == 2
    assert result[-1] == 100
    assert len(result) == 50
    assert all(num % 2 == 0 for num in result)


# Exercise 4 Tests
def test_even_numbers_comprehension():
    result = get_even_numbers_comprehension()

    assert result[0] == 2
    assert result[-1] == 100
    assert len(result) == 50
    assert all(num % 2 == 0 for num in result)


def test_both_methods_equal():
    assert get_even_numbers() == get_even_numbers_comprehension()