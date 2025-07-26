import pytest

from rpn.service.base import (
    clear_stack,
    create_stack,
    delete_stack,
    get_stack,
    get_stacks,
    push_token,
)
from rpn.service.exceptions import ServiceError


def test_create_stack():
    stack_id, stack = create_stack()

    assert (stack_id, stack) in get_stacks()

    delete_stack(stack_id)


def test_get_stack():
    stack_id, stack = create_stack()
    push_token(stack_id, "3")
    push_token(stack_id, "4")
    assert get_stack(stack_id) == (stack_id, [3.0, 4.0])

    delete_stack(stack_id)


def test_clear_stack():
    stack_id, _ = create_stack()
    push_token(stack_id, "5")
    clear_stack(stack_id)
    assert get_stack(stack_id) == (stack_id, [])

    delete_stack(stack_id)


def test_push_token():
    stack_id, _ = create_stack()
    push_token(stack_id, "2")
    assert get_stack(stack_id) == (stack_id, [2.0])

    push_token(stack_id, "3")
    assert get_stack(stack_id) == (stack_id, [2.0, 3.0])

    push_token(stack_id, "+")
    assert get_stack(stack_id) == (stack_id, [5.0])

    delete_stack(stack_id)


def test_create_several_stacks():
    stack1_id, stack_1 = create_stack()
    stack2_id, stack_2 = create_stack()

    stacks = get_stacks()
    assert len(stacks) == 2
    assert (stack1_id, stack_1) in stacks
    assert (stack2_id, stack_2) in stacks

    delete_stack(stack1_id)
    delete_stack(stack2_id)


def test_push_tokens_on_several_stacks():
    stack1_id, _ = create_stack()
    stack2_id, _ = create_stack()

    assert push_token(stack1_id, "1") == [1.0]
    assert push_token(stack1_id, "2") == [1.0, 2.0]
    assert push_token(stack1_id, "+") == [3.0]

    assert push_token(stack2_id, "3") == [3.0]
    assert push_token(stack2_id, "4") == [3.0, 4.0]
    assert push_token(stack2_id, "*") == [12.0]

    delete_stack(stack1_id)
    delete_stack(stack2_id)


def test_push_invalid_token():
    stack_id, _ = create_stack()

    with pytest.raises(ServiceError, match="Invalid token"):
        push_token(stack_id, "1.2.3")

    delete_stack(stack_id)
