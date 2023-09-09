from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CreateEmployee(BaseModel):
    ful_name: str
    degree: str


class CreateHeadTask(BaseModel):
    task: str
    employee_id: Optional[int]
    deadline: datetime


class CreateTask(BaseModel):
    task: str
    status: Optional[str]
    parent_id: Optional[int]
    employee_id: Optional[int]
    deadline: datetime
