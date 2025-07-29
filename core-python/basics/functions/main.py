"""Function"""

import time
from typing import Callable, Any
from functools import wraps


def timing_decorator(func: Callable[..., Any]) -> Callable[..., Any]:
    """Print how long a func takes to run"""

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time: float = time.time()
        result = func(*args, **kwargs)
        end_time: float = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result

    return wrapper


@timing_decorator
def process_numbers(
    numbers: list[float], operation: Callable[[float], float]
) -> list[float]:
    """Transform numbers using a provided lambda"""
    if not numbers:
        raise ValueError("Input list cannot be empty")

    results: list[float] = []
    invalid_inputs: list[Any] = []

    for num in numbers:
        try:
            # if not isinstance(num, (int, float)):
            if num + "":
                invalid_inputs.append(num)
        except TypeError:
            try:
                result = operation(float(num))
                results.append(result)
            except ValueError as e:
                print(e)
            except ZeroDivisionError as e:
                print(f"{e} - float division by zero")

    if invalid_inputs:
        print(f"Skipped invalid inputs: {invalid_inputs}")

    return results


def main() -> None:
    """Main function to demonstrate the use of process_numbers with decorators"""
    # Sample data
    numbers: list[float] = [1.0, 2.0, 3.0, 4.0, 5.0]

    # Define lambda operation
    square: Callable[[float], float] = lambda x: x**2
    cube: Callable[[float], float] = lambda x: x**3

    # Process number with different operations
    print("Processing numbers with square operation:")
    squared_numbers = process_numbers(numbers, square)
    print(f"Squared: {squared_numbers}")

    print("\nProcessing numbers with cube operation:")
    cubed_numbers = process_numbers(numbers, cube)
    print(f"Cubed: {cubed_numbers}")

    # Edge case: Empty list
    print("\nProcessing empty list:")
    try:
        empty_result = process_numbers([], square)
        print(f"Empty list result: {empty_result}")
    except ValueError as e:
        print(e)

    # Edge case: Invalid input
    print("\nProcessing invalid input:")
    invalid_numbers: list[Any] = [1.0, "abc", 3.0]
    invalid_result = process_numbers(invalid_numbers, square)
    print(f"Invalid input result: {invalid_result}")


if __name__ == "__main__":
    main()
