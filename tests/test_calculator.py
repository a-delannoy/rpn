import pytest

from rpn.core.calculator import Calculator
from rpn.core.exceptions import CoreError, DivisionByZeroError


@pytest.fixture
def calculator() -> Calculator:
    """Fixture to create a new Calculator instance for each test."""
    return Calculator()


def test_push_token(calculator: Calculator):
    """Test pushing a token onto the stack."""
    calculator.push_token(5)
    assert calculator.stack == [5]


def test_push_several_tokens(calculator: Calculator):
    """Test pushing several tokens onto the stack."""
    calculator.push_token(5)
    calculator.push_token(3)
    assert calculator.stack == [5, 3]


def test_clear(calculator: Calculator):
    """Test clearing the calculator's stack."""
    calculator.push_token(5)
    calculator.push_token(3)
    calculator.clear()
    assert calculator.stack == []


def test_sum(calculator: Calculator):
    """Test summing two numbers."""
    calculator.push_token(5)
    calculator.push_token(3)
    calculator.push_token("+")
    assert calculator.stack == [8]


def test_subtract(calculator: Calculator):
    """Test subtracting two numbers."""
    calculator.push_token(5)
    calculator.push_token(3)
    calculator.push_token("-")
    assert calculator.stack == [2]


def test_multiply(calculator: Calculator):
    """Test multiplying two numbers."""
    calculator.push_token(5)
    calculator.push_token(3)
    calculator.push_token("*")
    assert calculator.stack == [15]


def test_divide(calculator: Calculator):
    """Test dividing two numbers."""
    calculator.push_token(6)
    calculator.push_token(3)
    calculator.push_token("/")
    assert calculator.stack == [2]


def test_divide_by_zero(calculator: Calculator):
    """Test dividing by zero."""
    calculator.push_token(6)
    calculator.push_token(0)
    with pytest.raises(DivisionByZeroError, match="Cannot divide by zero."):
        calculator.push_token("/")


def test_invalid_operator(calculator: Calculator):
    """Test using an invalid operator."""
    calculator.push_token(5)
    calculator.push_token(3)
    with pytest.raises(CoreError, match="Invalid token: %"):
        calculator.push_token("%")


def test_invalid_operand(calculator: Calculator):
    """Test using an invalid operand."""
    with pytest.raises(CoreError, match="Invalid token: 1.2.3"):
        calculator.push_token("1.2.3")


def test_wide_expression(calculator: Calculator):
    """Test a wide expression."""
    calculator.push_token(5)
    calculator.push_token(3)
    calculator.push_token(2)
    calculator.push_token("+")
    calculator.push_token("*")
    assert calculator.stack == [25]


def test_not_enough_operands(calculator: Calculator):
    """Test operation with not enough operands."""
    calculator.push_token(5)
    with pytest.raises(CoreError, match="Not enough operands in stack for operation."):
        calculator.push_token("+")
