import pytest
from typing import Callable
from basics.functions.main import process_numbers

def test_process_numbers_valid_input() -> None:
    """Test process_numbers with valid numeric inputs."""
    numbers: list[float] = [1.0, 2.0, 3.0]
    square: Callable[[float], float] = lambda x: x ** 2
    assert process_numbers(numbers, square) == [1.0, 4.0, 9.0], "Should square valid numbers"
    cube: Callable[[float], float] = lambda x: x ** 3
    assert process_numbers(numbers, cube) == [1.0, 8.0, 27.0], "Should cube valid numbers"

def test_process_numbers_invalid_input() -> None:
    """Test process_numbers with invalid inputs."""
    numbers: list[Any] = [1.0, "2", 3.0, "abc", 5.0]
    square: Callable[[float], float] = lambda x: x ** 2
    result = process_numbers(numbers, square)
    assert result == [1.0, 9.0, 25.0], "Should process valid numbers, skip invalid ones"

def test_process_numbers_empty_list() -> None:
    """Test process_numbers with empty list."""
    square: Callable[[float], float] = lambda x: x ** 2
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        process_numbers([], square)

def test_process_numbers_invalid_operation() -> None:
    """Test process_numbers with invalid operation."""
    numbers: list[float] = [1.0, 2.0, 3.0]
    invalid_op: Callable[[float], float] = lambda x: x / 0  # Causes ZeroDivisionError
    result = process_numbers(numbers, invalid_op)
    assert result == [], "Should return empty list for invalid operation"
