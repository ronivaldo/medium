# Technical Implementation Plan – Basic Calculator

## Overview

This plan translates the functional specification for the calculator into concrete technical decisions and artifacts.  It complies with the project constitution (library‑first, CLI mandate, test‑first, simplicity, integration‑first) and ensures that the specification is met with clarity【121547767717787†L709-L734】.  It also aligns with the guidance that a plan should describe *how* to build the system, while the spec focuses on *what*【64704907123017†L541-L549】.

## Technology Stack

- **Programming language**: Python 3.11.  Chosen for its simplicity, portability and built‑in numeric support.
- **Library**: The arithmetic functions will reside in a package called `calc`, within `operations.py`.  This module contains pure functions without side effects and is suitable for reuse.
- **CLI framework**: The command‑line interface will use Python’s standard `argparse` to minimize dependencies and adhere to the simplicity gate【121547767717787†L751-L764】.
- **Testing framework**: `pytest` will be used for unit and integration tests.  Pytest is lightweight and widely adopted.
- **Packaging**: The project will be structured as a Python package with a `pyproject.toml` using the `setuptools` backend for installability.

## Architectural Components

1. **Library (`calc/operations.py`)**

   - Defines four functions: `add(a: float, b: float) -> float`, `subtract(a: float, b: float) -> float`, `multiply(a: float, b: float) -> float`, `divide(a: float, b: float) -> float`.
   - Validates inputs: ensures both arguments are numeric; raises `TypeError` on invalid types.
   - Raises `ZeroDivisionError` when dividing by zero.
   - Contains no state or side effects.  All functions are `pure`.

2. **CLI (`calc_cli.py`)**

   - Uses `argparse` to parse three positional arguments: first operand (string), operator and second operand (string).
   - Converts operands to floats and dispatches to the corresponding library function.
   - Handles exceptions: prints a descriptive error and exits with a non‑zero status.
   - Provides `--help` and `--version` flags.
   - Supports JSON output via an optional `--json` flag for machine‑readable results.

3. **Tests (`tests/`)**

   - **Unit tests** for each arithmetic function:
     - Typical cases (e.g., `add(2, 3)` yields 5).
     - Edge cases (e.g., negative numbers, zero, floats).
     - Invalid input types (e.g., strings) leading to `TypeError`.
     - Division by zero, expecting `ZeroDivisionError`.
   - **Integration tests** for the CLI:
     - Use the `subprocess` module to invoke `calc_cli.py` with various arguments.
     - Assert correct output and exit codes.
     - Test error handling (non‑numeric input, division by zero).
   - Tests are written before any implementation code【121547767717787†L736-L749】.

4. **Project Structure**

```
.
├── calc_spec_driven/
│   ├── constitution.md
│   ├── spec.md
│   ├── plan.md
│   ├── tasks.md
│   ├── calc/
│   │   ├── __init__.py
│   │   └── operations.py
│   ├── calc_cli.py
│   ├── pyproject.toml
│   └── tests/
│       ├── __init__.py
│       └── test_operations.py
```

## Considerations

- **Simplicity**: no additional layers or classes are introduced.  Using `argparse` avoids external dependencies【121547767717787†L751-L764】.
- **CLI output**: human‑readable by default; optional JSON output aids script integration.
- **Extensibility**: though not required, the plan reserves space for future operations (exponents, roots).  New operations would follow the same pattern.
- **Error handling**: invalid inputs are not silently coerced; explicit exceptions and user messages improve usability.

## Quickstart Instructions

Assuming Python 3.11 is installed:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pytest
python calc_cli.py 2 + 3      # Outputs: 5.0
python calc_cli.py 5 / 0      # Outputs error and exit code 1
```

## Compliance with Constitution Gates

Before implementation, verify that the plan satisfies pre‑implementation gates【121547767717787†L783-L794】:

- **Simplicity gate**: Only one project (`calc`), no unnecessary abstraction.
- **Anti‑abstraction gate**: Operates directly on Python built‑ins; no wrapper around `argparse`.
- **Integration‑first gate**: Specifies integration tests using real CLI and library; contract tests will be defined in tasks.

If any gate fails, justification must be recorded in the “complexity tracking” section (not needed for this simple calculator).

