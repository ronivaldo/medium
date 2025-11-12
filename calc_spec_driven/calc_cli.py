#!/usr/bin/env python3
"""
calc_cli.py

Command‑line interface for the basic calculator.  Parses command‑line arguments,
invokes the appropriate operation from the `calc` library, and prints the result.
It adheres to the CLI interface mandate of the project constitution【121547767717787†L723-L734】.
"""
import argparse
import json
import sys
from typing import Any

from calc import add, subtract, multiply, divide


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="A simple calculator that performs addition, subtraction, multiplication and division."
    )
    parser.add_argument("a", type=str, help="The first operand (number)")
    parser.add_argument("op", type=str, choices=["+", "-", "*", "/"], help="The operator")
    parser.add_argument("b", type=str, help="The second operand (number)")
    parser.add_argument(
        "--json", action="store_true", help="Output result as JSON with keys 'a', 'op', 'b', 'result'"
    )
    parser.add_argument("--version", action="version", version="calc-cli 1.0.0")
    return parser.parse_args()


def convert_operand(value: str) -> float:
    try:
        return float(value)
    except ValueError:
        raise ValueError(f"Invalid numeric value: '{value}'")


def calculate(a: float, op: str, b: float) -> float:
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }
    func = operations.get(op)
    if func is None:
        raise ValueError(f"Unsupported operator: {op}")
    return func(a, b)


def main(argv: Any = None) -> int:
    args = parse_args()
    try:
        a = convert_operand(args.a)
        b = convert_operand(args.b)
        result = calculate(a, args.op, b)
        if args.json:
            output = json.dumps({"a": a, "op": args.op, "b": b, "result": result})
        else:
            output = str(result)
        print(output)
        return 0
    except ZeroDivisionError:
        print("Error: cannot divide by zero", file=sys.stderr)
        return 1
    except (TypeError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
