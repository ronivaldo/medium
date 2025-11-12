import subprocess
import sys
import json

import pytest

from calc.operations import add, subtract, multiply, divide


# Unit tests for arithmetic functions
@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 3, 5.0),
        (-1, -1, -2.0),
        (2.5, 0.5, 3.0),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (3, 2, 1.0),
        (0, 5, -5.0),
        (2.5, 0.5, 2.0),
    ],
)
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 3, 6.0),
        (-1, 5, -5.0),
        (2.5, 0.4, 1.0),
    ],
)
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (6, 3, 2.0),
        (-6, -2, 3.0),
        (2.5, 0.5, 5.0),
    ],
)
def test_divide(a, b, expected):
    assert divide(a, b) == expected


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)


def test_invalid_type_add():
    with pytest.raises(TypeError):
        add("a", 3)


# Integration tests for CLI

def run_cli(args):
    cmd = [sys.executable, "calc_cli.py"] + args
    result = subprocess.run(
        cmd,
        cwd="..",  # run from project root where calc_cli.py lives
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return result


def test_cli_add():
    result = run_cli(["2", "+", "3"])
    assert result.returncode == 0
    assert result.stdout.strip() == "5.0"


def test_cli_divide_json():
    result = run_cli(["10", "/", "2", "--json"])
    assert result.returncode == 0
    data = json.loads(result.stdout)
    assert data["result"] == 5.0
    assert data["a"] == 10.0
    assert data["op"] == "/"
    assert data["b"] == 2.0


def test_cli_divide_by_zero():
    result = run_cli(["5", "/", "0"])
    assert result.returncode == 1
    assert "cannot divide by zero" in result.stderr


def test_cli_invalid_input():
    result = run_cli(["five", "+", "2"])
    assert result.returncode == 1
    assert "Invalid numeric value" in result.stderr
