from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Schemas(BaseModel):
    class Config:
        orm_mode = True


class GetEmployee(Schemas):
    id: int
    ful_name: str
    degree: str


class GetBusyEmployee(Schemas):
    employee: list['GetEmployee']
    task: str


class GetTask(Schemas):
    id: int
    task: str
    status: str
    parent_id: int
    parent: str
    employee: list['GetEmployee']
    employee_id: int
    deadline: datetime


class CreateEmployee(Schemas):
    ful_name: str
    degree: str


class EmployeeUpdate(Schemas):
    ful_name: str
    degree: str


class CreateHeadTask(Schemas):
    task: str
    employee_id: Optional[int]
    deadline: datetime


class CreateTask(Schemas):
    task: str
    parent_id: Optional[int]
    employee_id: Optional[int]
    deadline: datetime


class UpdateTask(Schemas):
    task: str
    status: Optional[str]
    parent_id: Optional[int]
    employee_id: Optional[int]
    deadline: datetime


class UpdateHeadTask(Schemas):
    task: str
    status: Optional[str]
    employee_id: Optional[int]
    deadline: datetime
