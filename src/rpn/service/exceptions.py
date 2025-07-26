from rpn.core.exceptions import RPNError


class ServiceError(RPNError):
    """Base class for all service-related exceptions."""


class StackNotFoundError(ServiceError):
    """Exception raised when a stack is not found."""
