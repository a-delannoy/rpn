import operator
from typing import Callable
from uuid import uuid4

from rpn.core.exceptions import CoreError, DivisionByZeroError
from rpn.core.utils import is_operator, is_valid_operand, safe_divide


class Calculator:
    def __init__(self):
        self.id = uuid4()
        self.stack = []

    def _get_operator_function(self, token: str) -> Callable:
        op_funcs = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": safe_divide,
        }
        if token not in op_funcs:
            raise CoreError(f"Unknown operator: {token}")
        return op_funcs[token]

    def push_token(self, token: str) -> None:
        """Push a token onto the stack, performing operations if necessary."""

        if is_operator(token=token):
            if len(self.stack) < 2:
                raise CoreError("Not enough operands in stack for operation.")
            b = self.stack.pop()
            a = self.stack.pop()
            op_func = self._get_operator_function(token)
            try:
                result = op_func(a, b)
            except DivisionByZeroError as e:
                # Push back operands if operation fails
                self.stack.append(a)
                self.stack.append(b)
                raise e
            self.stack.append(result)
        elif is_valid_operand(operand=token):
            self.stack.append(float(token))
        else:
            raise CoreError(f"Invalid token: {token}")

    def clear(self):
        """Clear the calculator's stack."""
        self.stack.clear()

    def get_stack(self) -> list:
        """Get the current stack."""
        return self.stack.copy()
