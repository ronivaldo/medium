"""calc package

Exposes the basic arithmetic operations for easy import.

Example:
    >>> from calc import add, subtract
    >>> add(2, 3)
    5.0
"""

from .operations import add, subtract, multiply, divide

__all__ = ["add", "subtract", "multiply", "divide"]
