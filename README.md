# Belajar Python

Practice code and study notes from learning Python with the santrikoding course. Each topic is written as runnable code with comments in Indonesian, and some topics include screenshots of the output.

## Repository contents

```
belajar-python/
├── python_untuk_pemula.py   # Basics: variables through classes and constructors
├── python_dasar.py          # Next level: data structures, OOP, exceptions, files, modules, packages
├── constants.py             # Module-level constants example (PI, GRAVITY, MAX_RETRY)
├── matematika.py            # Simple module example (tambah, kali)
├── my_package/              # Package example
│   ├── __init__.py
│   ├── operasi.py           # kurang(a, b)
│   └── geometri.py          # luas_persegi(sisi)
├── contoh.txt               # Sample file for the file handling exercises
├── data.txt                 # Sample file for the file handling exercises
├── screenshots/
│   ├── python-untuk-pemula/ # 8 screenshots
│   └── python-dasar/        # 18 screenshots
├── requirements.txt         # Notes only, no external dependencies
└── .gitignore
```

## Topics covered

### `python_untuk_pemula.py`

- Variables and data types: integer, float, string (single, double, multiline), boolean
- Arithmetic and logical operators (`and`, `or`, `not`)
- Conditionals: `if`, `elif`, `else`
- `for` and `while` loops, plus `break` and `continue`
- Lists and dictionaries: create, access, add, update, delete items
- Functions: parameters, arguments, `*args`, `**kwargs`, default values
- Classes, objects, constructors, methods, and the `self` parameter

### `python_dasar.py`

- Program structure, comments, indentation, input and output, the `main()` function
- Basic data types: int, float, str, bool, list, tuple, dict, set
- Type conversion and variable naming rules
- Constants, and sharing them through a module (`constants.py`)
- Operators: arithmetic, comparison, logical, assignment, membership, identity
- Control flow and functions (`*args`, `**kwargs`)
- Lists, tuples, sets (including set operations), and dictionaries (including nested)
- OOP: classes and objects, encapsulation (public, protected, private, getters, setters), inheritance (`super()`), polymorphism, abstraction (`ABC`, `abstractmethod`)
- Exception handling: `try`, `except`, `else`, `finally`, and custom exceptions
- File handling
- Modules and packages (`my_package`)

## Running the code

Developed with Python 3.14. The minimum version that runs the code has not been tested.

All code uses only the standard library (`abc`, `math`, `os`, `datetime`), so there is nothing to install. `requirements.txt` contains only comments, so `pip install -r requirements.txt` is safe to run and installs nothing.

```bash
# Optional: create and activate a virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# Run the practice files
python python_untuk_pemula.py
python python_dasar.py
```

Run from the repository root so that `import constants`, `import matematika`, and `import my_package` resolve.

The file handling section reads and writes `contoh.txt` and `data.txt`, so the contents of those files may change after you run the code.

## Screenshots

Output for each section is in `screenshots/`, named `tutorial-1.png` and so on, following the order of the material:

- [`screenshots/python-untuk-pemula/`](screenshots/python-untuk-pemula)
- [`screenshots/python-dasar/`](screenshots/python-dasar)

## Commit history

Commits follow the format `feat(python-basics): add <topic> examples with screenshots`, one commit per topic (dictionary, class and object, encapsulation, inheritance, polymorphism, abstraction, exception handling, file handling, modules, packages).

## Goal

Keep practice code, study notes, and Python learning progress in one place.
