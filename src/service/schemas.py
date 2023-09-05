from datetime import datetime

from pydantic import BaseModel


class CreateEmployee(BaseModel):
    id: int
    ful_name: str
    degree: str


class CreateTask(BaseModel):
    id: int
    title: str
    employee: str
    employee_id: int
    parent: str
    parent_id: int
    deadline: datetime
