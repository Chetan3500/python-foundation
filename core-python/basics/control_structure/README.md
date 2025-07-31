# Control Structure

This script processes a list of user actions (e.g., login, logout, error) using **structural pattern matching** (`match` statement) and sets to track unique users.

It demonstrates

- control structures,
- sets,
- functions,
- exception handling, and
- type hints.

---

## Structure

```sh
core-python
├── basics
│   ├── control_structure
│   │   ├── README.md
│   │   └── main.py
└── tests
    └── test_control_structure.py
```

- [main.py](./main.py) Processes user actions using pattern matching (match) and tracks unique users with sets.
- [test_control_structure.py](../../tests/test_control_structure.py): Pytest tests for control_structures.py, covering action processing and summarization.

---

## How to use the Script

1. Change dir to `core-python`, so that test can also be performed.

   ```sh
   # optional: in python-foundation dir
   # source venv/bin/activate    # Windows: venv\Scripts\activate
   cd core-python
   ```

2. Run `main.py`.

   ```sh
   python3 basics/control_structure/main.py
   ```

   **Output**:

   ```sh
    Processing Actions:
    User Alice logged in at timestamp 1001
    User Bob logged out
    Error occurred with code 404
    User Alice logged in at timestamp 1002
    Invalid action format: {'type': 'invalid'}
    Error processing action: {'user': 'Charlie'}
    Error processing action: None

    Unique Users: {'Bob', 'Alice', 'Charlie'}

    Action Summary:
    Login: 2
    Logout: 1
    Error: 1
    Invalid: 3
   ```

3. Run `test_control_structure.py`:

   ```sh
   PYTHONPATH=. pytest tests/test_control_structure.py -v
   ```

   **Output**:

   ```sh
    ========================== test session starts ===========================
    platform linux -- Python 3.12.8, pytest-8.4.1, pluggy-1.6.0 -- /PATH/TO/PYTHON-FOUNDATION/.venv/bin/python3.12
    cachedir: .pytest_cache
    rootdir: /PATH/TO/PYTHON-FOUNDATION/core-python
    collected 6 items

    tests/test_control_structure.py::test_process_action PASSED        [ 16%]
    tests/test_control_structure.py::test_process_action_edge_cases PASSED [ 33%]
    tests/test_control_structure.py::test_get_unique_users PASSED      [ 50%]
    tests/test_control_structure.py::test_get_unique_users_edge_cases PASSED [ 66%]
    tests/test_control_structure.py::test_summarize_actions PASSED     [ 83%]
    tests/test_control_structure.py::test_summarize_actions_edge_cases PASSED [100%]

    =========================== 6 passed in 0.02s ============================
   ```

---

## Explaination of Concept

### Structural Pattern Matching (match):

- **What**: Python 3.12’s `match` statement for pattern-based control flow (e.g., matching dictionary structures).
- **Why**: Simplifies complex conditionals, making code more readable than nested `if` statements.
- **Where**: Handling structured data (e.g., JSON-like actions in apps or logs in DevOps).
- **New**: Introduced in Python 3.10, enhanced in 3.12; uses `match`/`case` with patterns like `{'type': 'login', 'user': str(user)}`.
- **Exceptions**: Missing keys or wrong types cause errors (handled with `try-except`).

---

### Sets:

- **What**: Unordered collections of unique items (e.g., `set[str]` for unique user names).
- **Why**: Efficient for tracking unique elements and membership testing.
- **Where**: Deduplicating data (e.g., users in logs) or set operations (union, intersection).
- **New**: Created with `set()` or `{}`, using `.add()` to insert items.
- **Exceptions**: Only hashable types (e.g., strings, not lists) can be added.
- **More info**: On Terminal > `pydoc3.10 set`

---

### Any Type:

- **What**: Type hint `Any` from `typing` module for flexible dictionary values.
- **Why**: Allows type hints for dynamic data like dictionaries with mixed value types.
- **Where**: Common when processing JSON-like data or flexible inputs.
- **New**: Used in `dict[str, Any]` for action dictionaries.
- **Exceptions**: Overuse of `Any` reduces type safety; used sparingly here.
- **More info**: On Terminal > `pydoc3.10 typing`

---

## Exceptions/Edge Cases:

- **Invalid Actions**: Missing keys, wrong types, or `None` (handled with `try-except` and `case _`).
- **Empty Inputs**: Empty action lists (handled by returning empty sets or zero counts).
- **Match Limitations**: Simple patterns used; complex patterns may require deeper validation.

---

## Next Steps

[Variables_types](../variable_types/README.md) to explore dictionaries or tuples with type hints.
