# Email Validator

Script processing a list of user inputs to generate a report of valid email addresses and their domains.

It demonstrates:

- variables,
- control structures (nested loops and conditionals),
- functions,
- exception handling,
- functions (including `*args` and `**kwargs`)
- basic string manipulation
- pytest (for testing script)

## Structure

```txt
email_validator
├── main.py
├── README.md
├── module
│   ├── email_validator.py
│   └── __init__.py
└── test
    ├── __init__.py
    └── test_email_validator.py
```

- [`email_validator/main.py`](./main.py) email validator script.
- [`test_email_validator.py`](../../tests/test_email_validator.py) test script for email validator.

## How to Use the Script

1. Change dir to `core-python/basics/email_validator`, so that test can also be performed.

   ```sh
   # optional: in python-foundation dir
   # source venv/bin/activate    # Windows: venv\Scripts\activate
   cd core-python/basics/email_validator
   ```

2. Run `main.py`.

   ```sh
   python3 main.py
   ```

   **Output**:

   ```sh
   Report 1: All valid emails

    Domain: gmail.com
      - alice@gmail.com

    Domain: work.com
      - bob@work.com

    Domain: yahoo.com
      - charlie.personal@yahoo.com

    Domain: outlook.com
      - dave@outlook.com

    Report 2: Personal emails only

    Domain: yahoo.com
      - charlie.personal@yahoo.com

    Report 3: All emails (including invalid)

    Domain: gmail.com
      - alice@gmail.com

    Domain: work.com
      - bob@work.com

    Domain: invalid
      - invalid.email

    Domain: yahoo.com
      - charlie.personal@yahoo.com

    Domain: outlook.com
      - dave@outlook.com
   ```

3. Run `test_email_validator.py`:

   ```sh
   pytest tests/test_email_validator.py -v
   ```

   **Output**:

   ```sh
    ========================== test session starts ===========================
    platform linux -- Python 3.12.8, pytest-8.4.1, pluggy-1.6.0 -- /PATH/TO/PYTHON-FOUNDATION/.venv/bin/python3.12
    cachedir: .pytest_cache
    rootdir: /PATH/TO/PYTHON-FOUNDATION/core-python
    collected 4 items

    tests/test_email_validator.py::test_is_valid_email PASSED          [ 25%]
    tests/test_email_validator.py::test_extract_domain PASSED          [ 50%]
    tests/test_email_validator.py::test_generate_report PASSED         [ 75%]
    tests/test_email_validator.py::test_generate_report_edge_cases PASSED [100%]

    =========================== 4 passed in 0.01s ============================

   ```

## Explanations of Concepts

### `*args` (Variable Positional Arguments):

- **What**: Allows a function to accept any number of positional arguments (e.g., `generate_report(emails, "personal", "work")`).
- **Why**: Flexible for functions that need varying inputs (e.g., categories).
- **Where**: Used in scripts or APIs to handle dynamic inputs.
- **New**: `*categories` collects extra arguments as a tuple.
- **Exceptions**: Misusing `*args` with incorrect types (handled by checking `category.lower()`).

---

### `**kwargs` (Variable Keyword Arguments):

- **What**: Allows a function to accept any number of keyword arguments similar like key-value pair (e.g., `show_invalid=True`).
- **Why**: Provides optional configuration without fixed parameters.
- **Where**: Common in utilities or APIs for customizable behavior.
- **New**: `**options` collects keyword arguments as a dictionary; accessed with `.get()`.
- **Exceptions**: Missing keys (handled with `.get(default)`).

---

### String Manipulation:

- **What**: Uses `split('@')`, `in` operator, and `lower()` for email validation and domain extraction.
- **Why**: Processes text data efficiently.
- **Where**: Parsing user inputs or logs.
- **New**: Basic email validation checks for `@`and a domain.
- **Exceptions**: Invalid emails cause `IndexError` (handled in `is_valid_email`).

---

### Nested Loops and `any()`:

- **What**: Nested loop in list comprehension (`any(category.lower() in email.lower() ...)`).
- **Why**: Checks if any category matches an email, simplifying control flow.
- **Where**: Filtering data based on multiple criteria.
- **New**: `any()` is a Python built-in that returns `True` if any element in an iterable is `True`.
- **Exceptions**: Empty iterables or case mismatches (handled with `lower()`).

---

### Pytest:

- **What**: A testing framework for Python to write and run tests.
- **Why**: Automates verification of code functionality, ensuring reliability.
- **Where**: Used in development to validate logic and in CI/CD pipelines for DevOps.
- **New**: Tests are written as functions with `assert` statements; `pytest` discovers and runs them.
- **Exceptions**: Test failures indicate bugs or incomplete test coverage.

---

### Test Functions:

- **What**: Functions like `test_is_valid_email()` that check specific behaviors.
- **Why**: Isolates functionality for targeted validation.
- **Where**: Unit testing individual components (e.g., email validation).
- **New**: Prefix with `test_` for `pytest` to recognize; use descriptive assertions.
- **Exceptions**: Overly specific tests may break with minor code changes.

---

### Importing Modules:

- **What**: Importing functions from `email_validator`.py (e.g., `from basics.email_validator import ...`).
- **Why**: Tests need access to the code being tested.
- **Where**: Common in modular projects with separate test files.
- **New**: Path-based import requires correct directory structure.
- **Exceptions**: Incorrect paths cause `ModuleNotFoundError`.

## Exceptions/Edge Cases

### Of email_validator

- **Invalid Emails**: Handled by `is_valid_email()` with IndexError protection.
- **Empty Inputs**: Empty email lists or categories (handled with checks).
- **Type Hints**: Use `mypy` for static checking:
  ```bash
  pip install mypy
  mypy basics/email_validator.py
  ```

### Of test

- **Test Failures**: Indicate bugs in `email_validator/main.py` (e.g., incorrect domain extraction).
- **Module Import Errors**: Ensure `basics/email_validator/main.py` exists; fix path if `ModuleNotFoundError` occurs.
- **Incomplete Coverage**: Tests cover main cases but not every scenario (e.g., very long emails); add more as needed.
- **Pytest Setup**: Ensure `pytest` is installed; update `requirements.txt` if missed.

## Next Steps:

[Functions](../functions/README.md) demonstrates decorators and lambda functions by implementing a simple task.
