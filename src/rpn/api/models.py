from typing import List

from pydantic import BaseModel


class StackResponse(BaseModel):
    stack_id: str
    stack: List[float]
