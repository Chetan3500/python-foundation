# Book price analyzer

This program,

- reads a text file with book titles and prices,
- calculates the total and average price, and
- writes books above a price threshold to an output file.

## Structure

```sh
book-price-analyzer/
├── README.md
├── books.txt
├── expensive_books.txt
└── main.py
```

- [`main.py`](./main.py) - Book price analyzer script.

- [`books.txt`](./books.txt): Text file containing books title and price.

- [`expensive_books.txt`](./expensive_books.txt): books above a price threshold i.e 20.0 to an output file.

## How to Use the Script

1. Make sure to place `main.py` and `books.txt` in same directory.

2. Run Script:

   ```sh
   # change dir to project dir
   cd core-python/basics/book-price-analyzer
   python main.py
   ```

   **Output**:

   ```sh
   # terminal
   Error: Invalid price format on title: 'Invalid'.
   Book Price Summary:
   Total Price: $58.24
   Average Price: $19.41
   Expensive books written to expensive_books.txt
   ```

   ```txt
   # expensive_books.txt
   1984: $22.50
   ```

## Concept

Similar to previous [`Grade Calculator`](../grade_calculator/README.md/#explanation-of-concepts).

## Script explaination

---

### Variables and Data Types:

- **What**:
  - Strings (`input_file`, `title`),
  - floats (`price`, `total`, `average`),
  - lists (`books`),
  - tuples (`(title, price)`).
- **Why**: Stores and processes book data.
- **Where**: General data manipulation in apps or scripts.
- **Exceptions**: Invalid price formats (handled with `ValueError`).

---

### Control Structures:

- **What**:
  - `if` checks for valid data;
  - `for` loops iterate over file lines and books.
- **Why**: Implements logic to process and filter data.
- **Where**: Filtering results or iterating over datasets.
- **Exceptions**: Empty files or invalid lines (handled with checks).

---

### Functions:

- **What**: `read_books()`, `calculate_stats()`, `write_expensive_books()` with type hints.
- **Why**: Modularizes tasks for reusability and clarity.
- **Where**: Reusing logic in larger projects.
- **Exceptions**: Invalid inputs or empty lists (handled with defaults).

---

### Exception Handling:

- **What**: Handles `FileNotFoundError`, `ValueError`, `IOError`.
- **Why**: Ensures robustness against file or data issues.
- **Where**: Reliable scripts for real-world use.
- **Exceptions**: Avoid overly broad `except` (specific errors used).

---

### File I/O:

- **What**:
  - Reads `books.txt`,
  - writes to `expensive_books.txt`.
- **Why**: Persists data for reporting or storage.
- **Where**: Managing configs or results.
- **Exceptions**: File permission issues (handled with `IOError`).

---

### Type Hints:

- **What**: specify types.

  - `str`,
  - `list[tuple[str, float]]`,
  - `float`,
  - `-> None`

- **Why**: Enhances code clarity and supports tools like mypy.
- **Where**: Professional projects and shared codebases.
- **Exceptions**: Runtime errors still require `try-except` (type hints don’t prevent them).

## Exceptions/Edge Cases

- **File Issues**: Missing `books.txt` or invalid format (handled by `try-except`).
- **Invalid Data**: Non-numeric prices or malformed lines (skipped with warnings).
- **Output Overwrites**: Existing `expensive_books.txt` is overwritten (add a check if needed).
- **Type Hints**:
  - Ignored at runtime;
  - use mypy for static type checking:
    ```bash
    pip install mypy
    mypy core-python/basics/book_price_analyzer.py
    ```

## Next Steps:

[Email Validator](../email_validator/README.md)

- Processes a list of emails, validates them, and generates reports by domain, with optional category filtering and invalid email reporting.
- Uses type hints, `*args`, and `**kwargs`.
