# CS50P: Python Practice Programs

Small programs from Harvard's CS50P course, each named after the Python principle it practices. They are for learning, so some files keep commented-out alternatives from the lecture.

## Setup

```
pip install requests cowsay pillow pytest mypy
```

Run a program with `python file_name.py`. Programs that take arguments are marked below.

## Lecture 0: Functions and Variables

| File | Principle |
|---|---|
| `input_output.py` | `input`, `print`, string methods, f-strings |
| `numbers.py` | `int`, `float`, `round`, number formatting |
| `default_parameters.py` | Default parameter values |
| `functions.py` | Functions, `float` input, calculator with a/s/m/d |

## Lecture 1: Conditionals

| File | Principle |
|---|---|
| `compare.py` | Comparison operators, `or`, `!=` |
| `conditionals.py` | `if` / `elif` / `else`, letter grades |
| `returns.py` | Return values, even/odd check with `%` |
| `match.py` | `match` statement, house sorting |
| `strings.py` | Strings, `strip`, `capitalize`, `title`, login check |

## Lecture 2: Loops

| File | Principle |
|---|---|
| `loops.py` | `while`, `for`, `range`, `continue`, `break` |
| `lists_dicts.py` | Lists, dictionaries, list of dicts |
| `nesting.py` | Nested output, printing a grid of `#` |

## Lecture 3: Exceptions

| File | Principle |
|---|---|
| `exceptions.py` | `try` / `except` / `else`, `ValueError`, retry loop |

## Lecture 4: Libraries

| File | Principle |
|---|---|
| `modules.py` | `random`: `choice`, `randint`, `shuffle` |
| `statistics_module.py` | `statistics`: `mean`, `median` |
| `sys_argv.py` | `sys.argv`, `sys.exit` (pass names as arguments) |
| `packages.py` | Third-party packages from PyPI (`cowsay`) |
| `custom_modules.py` | Writing your own module, `if __name__ == "__main__"` |
| `apis.py` | `requests` and `json` with the iTunes API (pass a search term) |
| `run.py` | `subprocess.run` (pings google.com, Windows syntax) |
| `popen.py` | `subprocess.Popen` (opens command windows, Windows only) |

`packages.py` imports `hello` and `goodbye` from `sayings`, but the module is now called `custom_modules.py`. Change that import to `from custom_modules import hello, goodbye`.

## Lecture 5: Unit Tests

| File | Principle |
|---|---|
| `unit_tests.py` | The code under test (`square`) |
| `assert_statements.py` | `assert` with `try` / `except` |
| `test_unit_tests.py` | `pytest`, `pytest.raises` (run `pytest test_unit_tests.py`) |
| `pytest_folder/` | A `test/` package with `__init__.py` (run `pytest test` inside the folder) |

## Lecture 6: File I/O

| File | Principle |
|---|---|
| `file_io.py` | `open`, `with`, write/append/read, `sorted` |
| `csv_files.py` | `csv.DictWriter`, `csv.DictReader`, `lambda` sort key |
| `pil_images.py` | Pillow: build an animated GIF (`python pil_images.py a.gif b.gif`) |

## Lecture 7: Regular Expressions

| File | Principle |
|---|---|
| `regex_search.py` | `re.search`, validating an email |
| `regex_groups.py` | Capture groups, walrus operator (`:=`) |
| `regex_sub.py` | `re.sub`, extracting a username from a URL |

## Lecture 8: Object-Oriented Programming

| File | Principle |
|---|---|
| `classes.py` | Classes, `__init__`, `__str__`, raising errors |
| `properties.py` | `@property` getters and setters |
| `class_methods.py` | `@classmethod`, class attributes |
| `inheritance.py` | Inheritance, `super()` |
| `operator_overloading.py` | `__add__` |

## Lecture 9: Et Cetera

| File | Principle |
|---|---|
| `sets.py` | Sets |
| `global_variables.py` | `global` |
| `constants.py` | Constants, class constants |
| `type_hints.py` | Type hints (check with `mypy type_hints.py`) |
| `docstrings.py` | Docstrings |
| `argparse_module.py` | `argparse` (`python argparse_module.py -n 3`) |
| `args_kwargs.py` | `*args` and `**kwargs` |
| `map_filter.py` | `map`, `filter`, `lambda` |
| `comprehensions.py` | List and dictionary comprehensions |
| `enumerate_function.py` | `enumerate` |
| `generators.py` | `yield` |
| `iterators.py` | `iter`, `next` |

## Notes

- Files are not named `random.py`, `statistics.py`, `argparse.py` or `subprocess.py`, because those names would shadow the standard library modules and break imports.
- `run.py` and `popen.py` use Windows commands (`ping -n`, PowerShell). `popen.py` opens 10 command windows, so run it with care.
