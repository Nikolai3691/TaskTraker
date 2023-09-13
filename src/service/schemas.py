from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class GetEmployee(BaseModel):
    id: int
    ful_name: str
    degree: str

    class Config:
        orm_mode = True


class GetBusyEmployee(BaseModel):
    employee: list['GetEmployee']
    task: str

    class Config:
        orm_mode = True


class GetTask(BaseModel):
    id: int
    task: str
    status: str
    parent_id: int
    parent: str
    employee: list['GetEmployee']
    employee_id: int
    deadline: datetime

    class Config:
        orm_mode = True


class CreateEmployee(BaseModel):

    ful_name: str
    degree: str

    class Config:
        orm_mode = True


class EmployeeUpdate(BaseModel):
    ful_name: str
    degree: str

    class Config:
        orm_mode = True


class CreateHeadTask(BaseModel):
    task: str
    employee_id: Optional[int]
    deadline: datetime

    class Config:
        orm_mode = True


class CreateTask(BaseModel):
    task: str
    parent_id: Optional[int]
    employee_id: Optional[int]
    deadline: datetime

    class Config:
        orm_mode = True


class UpdateTask(BaseModel):
    task: str
    status: Optional[str]
    parent_id: Optional[int]
    employee_id: Optional[int]
    deadline: datetime

    class Config:
        orm_mode = True


class UpdateHeadTask(BaseModel):
    task: str
    status: Optional[str]
    employee_id: Optional[int]
    deadline: datetime

    class Config:
        orm_mode = True
