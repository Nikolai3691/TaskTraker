from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session
from typing import List

from service.crud import Employee, Tasks, Sevices

from service.schemas import CreateEmployee, CreateTask, CreateHeadTask
from service.schemas import UpdateTask, UpdateHeadTask, GetEmployee, EmployeeUpdate

router_employee = APIRouter(
    prefix='/employee',
    tags=['CRUD_Employee']
)

router_task = APIRouter(
    prefix='/task',
    tags=['CRUD_Task']
)

router_service = APIRouter(
    prefix='/service',
    tags=['Service']
)


@router_employee.post("/add", response_model=CreateEmployee)
async def add_employee(new_employee: CreateEmployee, session: AsyncSession = Depends(get_async_session)):
    employee = await Employee(session).add_employee(new_employee=new_employee)
    return employee


@router_employee.get("/get", response_model=List[GetEmployee])
async def get_employee(session: AsyncSession = Depends(get_async_session)):
    employee = await Employee(session).get_employee()
    return employee


@router_employee.put("/update", response_model=EmployeeUpdate)
async def update_employee(employee_update: EmployeeUpdate, employee_id: int,
                          session: AsyncSession = Depends(get_async_session)):
    return await Employee(session).update_employee(employee_update=employee_update, employee_id=employee_id)


@router_employee.delete("/delete")
async def delete_employee(delete_id: int, session: AsyncSession = Depends(get_async_session)):
    return await Employee(session).delete_employee(delete_id=delete_id)


@router_task.post("/add/head", response_model=CreateHeadTask)
async def add_task_head(new_task: CreateHeadTask, session: AsyncSession = Depends(get_async_session)):
    return await Tasks(session).add_head_task(new_task=new_task)


@router_task.post("/add", response_model=CreateTask)
async def add_task(new_task: CreateTask, session: AsyncSession = Depends(get_async_session)):
    return await Tasks(session).add_task(new_task=new_task)


@router_task.get('/get')
async def get_task(session: AsyncSession = Depends(get_async_session)):
    task = await Tasks(session).get_task()
    return task


@router_task.put("/update_head", response_model=UpdateTask)
async def update_head_task(head_task_id: int, new_head_task: UpdateHeadTask,
                           session: AsyncSession = Depends(get_async_session)):
    return await Tasks(session).update_head_task(head_task_id=head_task_id, new_head_task=new_head_task)


@router_task.put("/update", response_model=UpdateTask)
async def update_task(task_id: int, new_task: UpdateTask,
                      session: AsyncSession = Depends(get_async_session)):
    return await Tasks(session).update_task(task_id=task_id, new_task=new_task)


@router_task.delete("/delete")
async def delete_task(delete_id: int, session: AsyncSession = Depends(get_async_session)):
    return await Tasks(session).delete_task(delete_id=delete_id)


@router_service.get("/get_busy_employee")
async def get_busy_employee(session: AsyncSession = Depends(get_async_session)):
    busy_employee = await Sevices(session).get_busy_employee()
    return busy_employee


@router_service.get("/get_task_not_in_work")
async def get_task_not_in_work(session: AsyncSession = Depends(get_async_session)):
    head_task = await Sevices(session).get_task_not_in_work()
    return head_task


@router_service.get("/get_list_objects")
async def get_list_objects(session: AsyncSession = Depends(get_async_session)):
    list_objects = await Sevices(session).get_list_objects()
    return list_objects
