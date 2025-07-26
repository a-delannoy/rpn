from rpn.core.exceptions import DivisionByZeroError


def is_operator(token: str) -> bool:
    return token in {"+", "-", "*", "/"}


def safe_divide(a: float, b: float) -> float:
    """Safely divide two numbers, raising an error if the denominator is zero."""

    assert isinstance(a, float) and isinstance(b, float), (
        "Both arguments must be floats."
    )
    if b == 0:
        raise DivisionByZeroError("Cannot divide by zero.")
    return a / b


def is_valid_operand(operand: str) -> bool:
    """Check if the operand is a valid number."""
    try:
        float(operand)
        return True
    except ValueError:
        return False
