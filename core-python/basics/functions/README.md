# Functions

Script demonstrates **decorators** and **lambda** functions by implementing a simple task:

- timing function execution and
- processing a list of numbers with lambda-based operations (e.g., square, cube).

## Structure

```txt
core-python
├── basics
│   ├── functions
│   │   ├── main.py
│   │   └── README.md
│   └── README.md
├── README.md
└── tests
    └── test_functions.py

```

- [`main.py`](./main.py) functions script.
- [`test_functions.py`](../../tests/test_functions.py) test script for email validator.

## How to Use the Script

1. Change dir to `core-python`, so that test can also be performed.

   ```sh
   # optional: in python-foundation dir
   # source venv/bin/activate    # Windows: venv\Scripts\activate
   cd core-python
   ```

2. Run `main.py`.

   ```sh
   python3 basics/functions/main.py
   ```

   **Output**:

   ```sh
    Processing numbers with square operation:
    process_numbers took 0.0000 seconds
    Squared: [1.0, 4.0, 9.0, 16.0, 25.0]

    Processing numbers with cube operation:
    process_numbers took 0.0000 seconds
    Cubed: [1.0, 8.0, 27.0, 64.0, 125.0]

    Processing empty list:
    Error - Input list cannot be empty

    Processing invalid input:
    Skipped invalid inputs: ['abc']
    process_numbers took 0.0000 seconds
    Invalid input result: [1.0, 9.0]
   ```

3. Run `test_functions.py`:

   ```sh
   PYTHONPATH=. pytest tests/test_functions.py -v
   ```

   **Output**:

   ```sh
    $ PYTHONPATH=. pytest tests/test_functions.py -vv
    ========================== test session starts ===========================
    platform linux -- Python 3.12.8, pytest-8.4.0, pluggy-1.6.0 -- /PATH/TO/PYTHON-FOUNDATION/.venv/bin/python3.12
    cachedir: .pytest_cache
    rootdir: /PATH/TO/PYTHON-FOUNDATION/core-python
    plugins: anyio-4.9.0
    collected 4 items

    tests/test_functions.py::test_process_numbers_valid_input PASSED   [ 25%]
    tests/test_functions.py::test_process_numbers_invalid_input PASSED [ 50%]
    tests/test_functions.py::test_process_numbers_empty_list PASSED    [ 75%]
    tests/test_functions.py::test_process_numbers_invalid_operation PASSED [100%]

    =========================== 4 passed in 0.01s ============================

   ```

## Explanations of Concepts

- **Decorators**:

- **What**: Functions that modify other functions (e.g., `timing_decorator` adds timing to `process_numbers`).
- **Why**: Adds functionality (e.g., logging, timing) without changing the original function.
- **Where**: Used in frameworks (e.g., Flask for routing) or DevOps scripts (e.g., logging automation tasks).
- **New**: Uses `@decorator` syntax and `wraps` to preserve function metadata.
- **Exceptions**: Incorrect decorator implementation can alter function behavior (e.g., missing `@wraps` loses metadata).

---

### **Lambda Functions**:

- **What**: Anonymous functions defined inline (e.g., `lambda x: x ** 2`).
- **Why**: Concise for simple operations passed as arguments.
- **Where**: Common in functional programming (e.g., `map()`, `filter()`) or callbacks.
- **New**: Defined with lambda args: expression; here, used for squaring/cubing numbers.
- **Exceptions**: Limited to single expressions; complex logic needs regular functions.

---

### **Callable Type**:

- **What**: Type hint `Callable[[float]`, float] for functions taking a float and returning a float.
- **Why**: Specifies function signatures in type hints for clarity.
- **Where**: Used in professional code with dynamic function passing.
- **New**: Requires `typing.Callable` (one of few `typing` imports needed in Python 3.12).
- **Exceptions**: Incorrect type usage caught by `mypy`.

---

### **Function Metadata (`@wraps`)**:

- **What**: Preserves original function’s name and docstring in decorators.
- **Why**: Ensures decorated functions remain introspectable (e.g., for debugging).
- **Where**: Standard in decorator implementation.
- **New**: Imported from `functools`.
- **Exceptions**: Omitting `@wraps` can cause confusion in debugging.

## Exceptions/Edge Cases

- **Decorator Issues**: Missing `@wraps` could obscure function metadata (handled with `functools.wraps`).
- **Invalid Inputs**: Empty lists or non-numeric inputs (handled with `ValueError`, `TypeError`).
- **Type Hints**: Use `mypy` for static checking:
  ```bash
  pip install mypy
  mypy core-python/basics/functions.py
  ```
- **Performance**: Timing decorator may show negligible times for fast functions.

## Next Steps:

[Control Structure](../control_structure/README.md) explore control structures with Python 3.12’s structural pattern matching (match statement) and introduce sets for unique data handling,
