import pytest
from fizzbuzz import FizzBuzz


@pytest.mark.parametrize(
    "number, expected_result",
    [
        (1, "1"),
        (2, "2"),
        (3, "Fizz"),
        (5, "Buzz"),
        (9, "Fizz"),
        (10, "Buzz"),
        (15, "FizzBuzz"),
        (21, "Fizz"),
        (25, "Buzz"),
        (30, "FizzBuzz"),
        (38, "38"),
    ],
)
def test_fizzbuzz(number, expected_result):
    my_fizzbuzz = FizzBuzz(number)
    assert my_fizzbuzz.convert_to_fizzbuzz() == expected_result
