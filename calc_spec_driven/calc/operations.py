"""
calc.operations

A simple arithmetic library providing four basic operations: addition, subtraction,
multiplication and division.  Functions validate inputs and raise exceptions on
invalid data or forbidden operations (e.g., division by zero).

This module is designed to be reusable and side‑effect free, in keeping with
Spec‑Driven Development’s library‑first principle.
"""
from typing import Union

Number = Union[int, float]


def _validate_numbers(a: Number, b: Number) -> None:
    """Validate that both arguments are numbers (int or float).

    Raises:
        TypeError: If either `a` or `b` is not an int or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError(f"Expected numeric type for a, got {type(a).__name__}")
    if not isinstance(b, (int, float)):
        raise TypeError(f"Expected numeric type for b, got {type(b).__name__}")


def add(a: Number, b: Number) -> float:
    """Return the sum of two numbers.

    Args:
        a: The first addend.
        b: The second addend.

    Returns:
        The sum as a float.
    """
    _validate_numbers(a, b)
    return float(a + b)


def subtract(a: Number, b: Number) -> float:
    """Return the result of subtracting `b` from `a`.

    Args:
        a: The minuend.
        b: The subtrahend.

    Returns:
        The difference as a float.
    """
    _validate_numbers(a, b)
    return float(a - b)


def multiply(a: Number, b: Number) -> float:
    """Return the product of two numbers.

    Args:
        a: The first factor.
        b: The second factor.

    Returns:
        The product as a float.
    """
    _validate_numbers(a, b)
    return float(a * b)


def divide(a: Number, b: Number) -> float:
    """Return the result of dividing `a` by `b`.

    Args:
        a: The dividend.
        b: The divisor.

    Returns:
        The quotient as a float.

    Raises:
        ZeroDivisionError: If `b` is zero.
    """
    _validate_numbers(a, b)
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return float(a / b)
