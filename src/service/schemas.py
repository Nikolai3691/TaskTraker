from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CreateEmployee(BaseModel):
    id: int
    ful_name: str
    degree: str


class CreateTaskFirst(BaseModel):
    id: int
    task: str
    # status: str
    # parent_id: Optional[int]
    # employee_id: Optional[int]
    deadline: datetime


class CreateTaskNext(BaseModel):
    id: int
    task: str
    status: str
    parent_id: Optional[int]
    employee_id: Optional[int]
    deadline: datetime
