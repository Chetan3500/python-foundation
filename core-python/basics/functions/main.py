"""Function"""

from typing import Callable, Any
from module.functions import process_numbers

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
