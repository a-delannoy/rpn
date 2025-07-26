from rpn.core.calculator import Calculator
from rpn.core.exceptions import CoreError
from rpn.core.registry import registry
from rpn.service.exceptions import ServiceError, StackNotFoundError


def create_stack() -> tuple[str, list[float]]:
    calculator = Calculator()

    registry[str(calculator.id)] = calculator
    return str(calculator.id), calculator.get_stack()


def delete_stack(stack_id: str) -> None:
    if registry.get(stack_id) is None:
        raise StackNotFoundError(f"Stack with ID {stack_id} does not exist.")
    del registry[stack_id]


def get_stack(stack_id: str) -> tuple[str, list[float]]:
    if registry.get(stack_id) is None:
        raise StackNotFoundError(f"Stack with ID {stack_id} does not exist.")
    return str(stack_id), registry[stack_id].get_stack()


def get_stacks() -> list[tuple[str, list[float]]]:
    return [
        (str(calculator.id), calculator.get_stack()) for calculator in registry.values()
    ]


def clear_stack(stack_id: str) -> None:
    if registry.get(stack_id) is None:
        raise StackNotFoundError(f"Stack with ID {stack_id} does not exist.")
    registry[stack_id].clear()


def push_token(stack_id: str, token: str) -> list[float]:
    if registry.get(stack_id) is None:
        raise StackNotFoundError(f"Stack with ID {stack_id} does not exist.")
    try:
        registry[stack_id].push_token(token)
    except CoreError as e:
        raise ServiceError(f"Failed to push token: {e}")
    return registry[stack_id].get_stack()
