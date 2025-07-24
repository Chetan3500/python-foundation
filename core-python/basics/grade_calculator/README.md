# Grade Calculator

Script reads a text file containing student grades, calculates the average grade for each student, and writes passing students (average ≥ 60) to an output file.

It demonstrates:

- variables,
- control structures,
- functions,
- exception handling,
- and file I/O in a simple.

## Structure

```txt
grade_calculator
├── grades.txt
├── main.py
├── passing_students.txt
└── README.md
```

- [`main.py`](./main.py): Grade calculator script.

- [`grades.txt`](./grades.txt): Text file containing student grades.

- [passing_students.txt](./passing_students.txt): Student who passed, overwrite everytime when script executed.

## How to Use the Script

1. Make sure to place `main.py` and `grades.txt` in same directory.

2. Run the Script:

   ```bash
   python core-python/basics/grade_calculator/main.py
   ```

   **Output**:

   ```sh
   # terminal
   Skipping student 'Invalid' due to invalid grades.
   Student Averages:
   Alice: 90.00
   Bob: 60.00
   Charlie: 75.00
   Passing students written to passing_students.txt
   ```

   ```sh
   # passing_students.txt
   Alice: 90.00
   Bob: 60.00
   Charlie: 75.00
   ```

## Explanation of the Script

### Variables and Data Types:

- **What**:
  - Strings (`input_file`, `name`),
  - lists (`students`, `grades`),
  - tuples (storing `name, grades`),
  - floats (averages).
- **Why**: Stores and processes student data.
- **Where**: General data manipulation in applications or scripts.
- **Exceptions**: Invalid grade formats (handled with `ValueError`).

---

### Control Structures:

- **What**:
  - `if` checks for valid data;
  - `for` loops iterate over file lines and students.
- **Why**: Implements logic to process and filter data.
- **Where**: Filtering results or iterating over datasets.
- **Exceptions**: Empty files or invalid lines (handled with checks).

---

### Functions:

- **What**: `read_grades()`, `calculate_average()`, `write_passing_students()` modularize tasks.
- **Why**: Reusable, readable code.
- **Where**: Reusing logic in larger projects or automation.
- **Exceptions**: Incorrect arguments or empty inputs.

---

### Exception Handling:

- **What**: Handles `FileNotFoundError`, `ValueError`, `IOError`.
- **Why**: Prevents crashes from invalid files or data.
- **Where**: Robust scripts for real-world use.
- **Exceptions**: Overly broad `except` (avoided by specifying errors).

---

### File I/O:

- **What**:
  - Reads `grades.txt`,
  - writes to `passing_students.txt`.
- **Why**: Processes and saves data persistently.
- **Where**: Managing configs, logs, or reports.
- **Exceptions**: File permission issues or invalid paths.

## Explanation of Concepts

### Text file Reading/Writing:

- **What**: Reading a text file line-by-line `(open('r'))` and writing to a file `(open('w'))`.
- **Why**: Common for processing data like logs or user inputs.
- **Where**: Used in scripts to read configs or save results (e.g., student grades, logs).

---

### List Comprehension:

- **What**: Concise way to create lists (e.g., `[int(grade) for grade in parts[1:]]`).
- **Why**: Cleaner and faster than loops for transforming data.
- **Where**: Filtering or converting data (e.g., converting strings to integers).

---

### String Splitting (`strip()`, `split()`):

- **What**:
  - `strip()` removes whitespace;
  - `split(',')` splits a string into a list by a delimiter.
- **Why**: Parses text data into usable parts.
- **Where**: Common in file processing or user input parsing.

---

### What Are Type Hints?

Type hints are annotations that specify the expected data types of variables, function parameters, or return values (e.g., `str`, `int`, `list`, `tuple`). They’re optional and don’t affect runtime behavior but help tools like VS Code catch errors early.

- **Example**:

  ```python
  def write_passing_students(students: list[tuple[str, list[int]]], output_file: str) -> None:
  ```

  - `students: list[tuple[str, list[int]]]` means students is a list of tuples, where each tuple contains a string (student name) and a list of integers (grades).
  - `output_file: str` means output_file is a string (file path)
  - `def write_passing_students(...) -> None` means this function return nothing.

Check: [Summary](#summary)

#### Why It Matters:

- **Readability**: Type hints clarify what data a function expects, making your code easier to understand for others (e.g., when sharing on GitHub).
- **Error Detection**: Tools like Pylance can warn you if you pass incorrect types (e.g., passing a list instead of a string for `output_file`).
- **Professionalism**: Type hints are common in production code, especially for developer and DevOps roles, showing you follow modern practices.

#### Where It’s Used:

- **Developer**: In applications to ensure functions receive correct data types (e.g., in web apps or APIs).
- **DevOps**: In automation scripts to validate inputs (e.g., ensuring a file path is a string).

#### Exceptions/Edge Cases:

- Type hints are optional and ignored at runtime, so they don’t catch errors during execution (use `try-except` for that).
- Incorrect type hints can mislead readers, so they must match the actual data.
- Older Python versions (<3.5) don’t support type hints, but you’re likely using a newer version (3.6+).

### Summary

**What Are Type Hints?**

- **What**: Notes in code (e.g., `: str`, `: list[int]`) that specify expected data types.
- **Why**: Makes code clearer, helps tools catch errors, and improves collaboration.
- **New**: A modern Python feature for better code quality, suggested by VS Code’s Pylance extension.
- **How to Use**: Add to function parameters and variables; no runtime impact.

## Exceptions/Edge Cases

- **File Issues**: Missing `grades.txt` or invalid format (handled by `try-except`).
- **Invalid Data**: Non-numeric grades or malformed lines (skipped with warnings).
- **Output Overwrites**: Existing `passing_students.txt` is overwritten (add a check if needed).

## Next Steps:

[Book price analyzer](../book-price-analyzer/) project which is similar to this one.
