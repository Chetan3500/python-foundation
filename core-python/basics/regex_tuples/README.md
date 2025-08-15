# Regex Tuples

This script ([`regex_tuples/main.py`](./main.py)) processes a list of log entries (as strings) to extract IP addresses and timestamps using **regular expressions**, storing results as **tuples**.

It demonstrates

- tuples,
- regex,
- control structures,
- functions,
- exception handling,
- and type hints,

focusing on in-memory processing to differ from [variables_types](../variable_types/README.md) (JSON/file I/O) while introducing a DevOps-relevant skill (log parsing).

---

## Structure

```sh
core-python
├── basics
│   ├── regex_tuples
│   │   ├── re_handle.txt
│   │   ├── main.py
│   │   ├── README.md
│   │   └── regex_cheatsheet.md
├── tests
│   ├── test_regex_tuples.py
```

- [re_handle.txt](./re_handle.txt) show valid way to get ip.
- [regex_cheatsheet](./regex_cheatsheet.md) contain regex way of handling.

## How to use the Script

1. Change dir to `core-python`, so that test can also be performed.

   ```sh
   # optional: in python-foundation dir
   # source venv/bin/activate    # Windows: venv\Scripts\activate
   cd core-python
   ```

2. Run `main.py`.

   ```sh
   python3 basics/regex_tuples/main.py
   ```

   **Output**:

   ```sh
    Extract Log Info:
    Log: 192.168.1.1 [2025-08-14 11:49:00] GET /api -> ('192.168.1.1', '2025-08-14 11:49:00')
    Log: 10.0.0.1 [2025-08-14 11:50:00] POST /login -> ('10.0.0.1', '2025-08-14 11:50:00')
    Log: 192.168.1.2 [2025-08-14 12:01:00] GET /data -> ('192.168.1.2', '2025-08-14 12:01:00')
    Log: invalid log entry -> None
    Log: 192.168.1.3 [2025-08-14 11:55:00] GET /api -> ('192.168.1.3', '2025-08-14 11:55:00')
    Log: None -> None

    Filtered Logs (IP prefix: '192.168'):
    IP: 192.168.1.1, Timestamp: 2025-08-14 11:49:00
    IP: 192.168.1.2, Timestamp: 2025-08-14 12:01:00
    IP: 192.168.1.3, Timestamp: 2025-08-14 11:55:00

    Log Counts by Hour:
    2025-08-14 11: 2 logs
    2025-08-14 12: 1 logs
   ```

3. Run `test_regex_tuples.py`:

   ```sh
   PYTHONPATH=. pytest tests/test_regex_tuples.py -v
   ```

   **Output**:

   ```sh
   $ PYTHONPATH=. pytest tests/test_regex_tuples.py -vv
   ========================== test session starts ===========================
   platform linux -- Python 3.12.8, pytest-8.4.0, pluggy-1.6.0 -- /PATH/TO/PYTHON-FOUNDATION/.venv/bin/python3.12
   cachedir: .pytest_cache
   rootdir: /PATH/TO/PYTHON-FOUNDATION/core-python
   plugins: anyio-4.9.0
   collected 4 items

   tests/test_regex_tuples.py::test_extract_log_info PASSED         [ 25%]
   tests/test_regex_tuples.py::test_filter_logs PASSED              [ 50%]
   tests/test_regex_tuples.py::test_count_by_hour PASSED            [ 75%]
   tests/test_regex_tuples.py::test_count_by_hour_edge_cases PASSED [100%]

   ========================== 4 passed in 0.05s ===========================
   ```

---

## Explaination of Concept

### Tuples:

- **What**: Immutable sequences (e.g., `Tuple[str, str]` for IP and timestamp).
- **Why**: Lightweight, fixed-size data storage; ensures data integrity.
- **Where**: Storing structured data (e.g., log entry details) in apps or scripts.
- **New**: Defined with `(x, y)`; immutable unlike lists; supports type hints with `Tuple`.
- **Exceptions**: Cannot modify after creation; errors if unpacking wrong sizes (handled with `None`).

---

### Regular Expressions (Regex):

- **What**: Pattern matching for strings (e.g., `r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'` for IPs).
- **Why**: Extracts specific data (e.g., IPs, timestamps) from unstructured text.
- **Where**: Common in log parsing (DevOps) or input validation (development).
- **New**: Uses `re.match()` to match patterns; groups (`()`) capture data.
- **Exceptions**: Invalid patterns or inputs cause errors (handled with `try-except`).

---

### Union Type (`|`):

- **What**: Type hint like `Tuple[str, str] | None` for multiple possible return types.
- **Why**: Specifies that a function may return a tuple or `None`.
- **Where**: Used in modern Python for flexible return types.
- **New**: Native in Python 3.12; no `typing.Union` needed.
- **Exceptions**: Overuse can reduce type safety (used minimally here).

---

## Exceptions/Edge Cases:

For main Script,

- **Invalid Logs**: Malformed logs or `None` (handled with `None` return).
- **Regex Errors**: Invalid patterns or inputs (handled with `try-except`).
- **Regex Limitations**: Simple IP/timestamp pattern; extend for complex logs if needed.

For test Script,

- **Test Failures**: Indicate bugs in `regex_tuples/main.py` (e.g., incorrect regex matching).
- **Import Errors**: Ensure `core-python/__init__.py` exists; fix path if `ModuleNotFoundError` occurs.
- **Regex Limitations**: Tests assume simple IP/timestamp patterns; extend for complex logs if needed.

---

## Next Steps

[Generators_comprehensions](../generators_comprehensions/README.md) processes a list of numbers using a generator to yield Fibonacci numbers (memory-efficient) and list comprehensions to filter and transform data (e.g., even/odd numbers).
