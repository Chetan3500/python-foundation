# Variable Types

This script (main.py) processes a **JSON file** containing product inventory data, uses dictionaries to summarize quantities by category, and applies a discount to low-stock items.

It demonstrates dictionaries,

- JSON processing,
- control structures,
- functions,
- exception handling
- type hints

---

## Structure

```bash
variable_types
├── inventory.json
├── main.py
├── module
│   └── variable_types.py
├── README.md
├── test
│   ├── __init__.py
│   └── test_variables_types.py
└── t.fixture
```

---

## How to use the Script

1. Change dir to `core-python`, so that test can also be performed.

   ```sh
   # optional: in python-foundation dir
   # source venv/bin/activate    # Windows: venv\Scripts\activate
   cd core-python/basics/variable_types/
   ```

2. Run `main.py`.

   ```sh
   python3 main.py
   ```

   **Output**:

   ```sh
   Inventory Summary by Category:
   Error processing product: Invalid quantity for Invalid
   Error processing product: 'category'
   Electronics: 13 items
   Furniture: 10 items

   Low-Stock Products with Discount:
   Error applying discount: '<' not supported between instances of 'str' and 'int'
   Error applying discount: 'quantity'
   Mouse: $26.99 (3 in stock)
   Desk: $134.99 (2 in stock)
   ```

3. Run `test_variable_types.py`:

   ```sh
   pytest -v
   ```

   **Output**:

   ```sh
   ============================= test session starts =============================

   tests/test_variables_types.py::test_load_inventory PASSED               [ 16%]
   tests/test_variables_types.py::test_load_inventory_edge_cases PASSED    [ 33%]
   tests/test_variables_types.py::test_summarize_by_category PASSED        [ 50%]
   tests/test_variables_types.py::test_summarize_by_category_edge_cases PASSED [ 66%]
   tests/test_variables_types.py::test_apply_discount PASSED               [ 83%]
   tests/test_variables_types.py::test_apply_discount_edge_cases PASSED    [100%]

   ============================== 6 passed in 0.04s ==============================
   ```

---

## Explaination of Concept

### Dictionaries:

- **What**: Key-value pairs (e.g., `summary: dict[str, int]` for category quantities).
- **Why**: Efficient for grouping and looking up data by key.
- **Where**: Common in data processing (e.g., summarizing logs) or DevOps configs (e.g., parsing JSON).
- **New**: Uses `.get(key, default)` to safely access keys; mutable but keys must be hashable.
- **Exceptions**: Missing keys cause `KeyError` (handled with `.get()` or `try-except`).

### JSON Processing:

- **What**: Reading JSON files with `json.load()` to convert to Python dictionaries/lists.
- **Why**: JSON is a standard format for configs and APIs, relevant for DevOps and development.
- **Where**: Parsing configuration files (e.g., Docker, Ansible) or API responses.
- **New**: JSON maps to Python types (objects to `dict`, arrays to `list`); here, reads a list of product dictionaries.
- **Exceptions**: Invalid JSON or wrong structure causes errors (handled with `json.JSONDecodeError`, `ValueError`).

### Dictionary Copy:

- **What**: Using `dict.copy()` to avoid modifying original data (e.g., in `apply_discount`).
- **Why**: Prevents unintended side effects when updating dictionaries.
- **Where**: Safe data manipulation in scripts or applications.
- **New**: Creates a shallow copy; nested objects may still be mutable.
- **Exceptions**: Shallow copy doesn’t protect nested structures (not an issue here).

---

## Exceptions/Edge Cases:

Of main script,

- **File Issues**: Missing or invalid `inventory.json` (handled with `FileNotFoundError`, `json.JSONDecodeError`).
- **Invalid Data**: Missing keys, wrong types (handled with `KeyError`, `TypeError`, `ValueError`).
- **JSON Structure**: Assumes a list of dictionaries; other formats cause errors (handled with `ValueError`).

Of test script,

- **Test Failures**: Indicate bugs in `variables_types/main.py` (e.g., incorrect JSON handling).
- **Import Errors**: Ensure `core-python/__init__.py exists`; fix path if `ModuleNotFoundError` occurs.
- **Fixture Issues**: File creation failures (unlikely with `tmp_path` but possible on restricted filesystems).
- **Incomplete Coverage**: Tests cover main cases; add more for complex JSON structures if needed.

---

## Next Steps

[regex_tuples](../regex_tuples/README.md) Explore tuples and regular expressions (regex) for pattern matching in strings.
