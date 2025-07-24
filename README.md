# Python Foundation

A repository showcasing my foundational Python skills for developer and DevOps roles, covering Core Python, OOP, and DSA.

## Install

1. Clone locally:

   ```sh
   git clone https://github.com/Chetan3500/python-foundation.git
   cd python-foundation/
   ```

2. Set-up a Virtual Environment (Optional)

   ```sh
   python -m venv venv
   source venv/bin/activate
   ```

## Folder Structure

```txt
python-foundation/
├── core-python
│   ├── basics
│   ├── modules
│   └── tests
├── dsa
│   ├── algorithms
│   │   └── tests
│   └── data-structures
│       └── tests
├── oop
│   └── server_manager
│       └── tests
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

- [Core python](./core-python/)

  For scripts demonstrating variables, control structures, functions, exception handling, file I/O, and modules.

  Covers foundational Python skills for scripting and automation.

  **Subfolders**:

  - [`basics/`](./core-python/basics/): Individual scripts for each concept to show isolated understanding.
  - [`modules/`](./core-python/modules/): Modular code with reusable utilities and example scripts.
  - [`tests/`](./core-python/tests/): Unit tests to demonstrate robust coding practices.

- [`oop/`](./oop/): For OOP projects (e.g., a server management tool).

  Shows ability to write scalable, modular code.

  **Subfolders**: Organize by project (e.g., [`server_manager/`](./oop/server_manager/) for a DevOps tool).

- [`dsa/`](./dsa/): For data structures (lists, dictionaries, etc.) and algorithms (searching, sorting, recursion).

  Demonstrates problem-solving and optimization skills.

  **Subfolders**: Split into [`data_structures/`](./dsa/data-structures/) and [`algorithms/`](./dsa/algorithms/) for clarity.

- **Supporting Files**:

  - `.gitignore`:

    - Excludes unnecessary files (e.g., virtual environments, `__pycache__`).
    - **Content**: Ignore `venv/`, `__pycache__/`, `\*.pyc`, and temporary files.

  - `requirements.txt`:

    - Lists dependencies (e.g., `pytest` for testing) for reproducibility.
    - **Content**: Generated with `pip freeze > requirements.txt` after setting up a virtual environment.

## Usage

Run scripts in each folder, e.g., `python core-python/basics/project_name/main.py`.

## Exceptions/Edge Cases

**Virtual Environment Issues**: Ensure `venv` is activated before running scripts or installing dependencies.
