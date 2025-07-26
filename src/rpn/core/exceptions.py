class RPNError(Exception):
    """Base class for all RPN-related exceptions."""


class CoreError(RPNError):
    """Base class for core-related exceptions."""


class DivisionByZeroError(CoreError):
    """Exception raised for division by zero errors."""
