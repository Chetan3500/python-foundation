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
            result = operation(num)
            results.append(result)
        except TypeError:
            invalid_inputs.append(num)
        except ZeroDivisionError as e:
            print(f"{e} - float division by zero")

    if invalid_inputs:
        print(f"Skipped invalid inputs: {invalid_inputs}")

    return results
