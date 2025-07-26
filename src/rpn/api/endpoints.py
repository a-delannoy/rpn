from typing import List

from fastapi import APIRouter, HTTPException

from rpn.api.models import StackResponse
from rpn.service import base as service
from rpn.service.exceptions import ServiceError

router = APIRouter()


@router.post("/stacks/", response_model=StackResponse)
def create_stack():
    stack_id, stack = service.create_stack()
    return {"stack_id": stack_id, "stack": stack}


@router.post("/stacks/{stack_id}/push", response_model=StackResponse)
def push_token(
    stack_id: str,
    token: str,
):
    try:
        stack = service.push_token(stack_id, token)
    except ServiceError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"stack_id": stack_id, "stack": stack}


@router.get("/stacks/", response_model=List[StackResponse])
def list_stacks():
    return [
        {"stack_id": stack_id, "stack": stack}
        for stack_id, stack in service.get_stacks()
    ]


@router.get("/stacks/{stack_id}", response_model=StackResponse)
def get_stack(
    stack_id: str,
):
    try:
        stack_id, stack = service.get_stack(stack_id)
    except ServiceError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return {"stack_id": stack_id, "stack": stack}


@router.post("/stacks/{stack_id}/clear", status_code=204)
def clear_stack(
    stack_id: str,
):
    try:
        service.clear_stack(stack_id)
    except ServiceError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return HTTPException(status_code=204, detail="Stack cleared successfully.")


@router.delete("/stacks/{stack_id}", status_code=204)
def delete_stack(
    stack_id: str,
):
    try:
        service.delete_stack(stack_id)
    except ServiceError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return HTTPException(status_code=204, detail="Stack deleted successfully.")
