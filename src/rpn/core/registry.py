from rpn.core.calculator import Calculator


class CalculatorRegistry:
    """A class to manage the calculator registry."""

    def __init__(self):
        self._registry = {}

    def __getitem__(self, stack_id: str) -> Calculator:
        return self._registry[stack_id]

    def __setitem__(self, stack_id: str, calculator: Calculator):
        self._registry[stack_id] = calculator

    def __delitem__(self, stack_id: str):
        del self._registry[stack_id]

    def values(self):
        return self._registry.values()

    def get(self, stack_id: str, default=None):
        return self._registry.get(stack_id, default)


registry = CalculatorRegistry()
