from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session

from service import crud
from service.schemas import CreateEmployee, CreateTask, CreateHeadTask, EmployeeUpdate, UpdateTask, UpdateHeadTask

router_employee = APIRouter(
    prefix='/employee',
    tags=['Employee']
)

router_task = APIRouter(
    prefix='/task',
    tags=['Task']
)


@router_employee.post("/add")
async def add_employee(new_employee: CreateEmployee, session: AsyncSession = Depends(get_async_session)):
    return await crud.add_employee(session=session, new_employee=new_employee)


@router_employee.get("/get")
async def get_employee(session: AsyncSession = Depends(get_async_session)):
    query = await crud.get_employee(session=session)
    return query


@router_employee.put("/update")
async def update_employee(employee_update: EmployeeUpdate, employee_id: int,
                          session: AsyncSession = Depends(get_async_session)):
    return await crud.update_employee(session=session, employee_update=employee_update, employee_id=employee_id)


@router_employee.delete("/delete")
async def delete_employee(delete_id: int, session: AsyncSession = Depends(get_async_session)):
    return await crud.delete_employee(delete_id=delete_id, session=session)


@router_task.post("/add/head")
async def add_task_head(new_task: CreateHeadTask, session: AsyncSession = Depends(get_async_session)):
    return await crud.add_head_task(session=session, new_task=new_task)


@router_task.post("/add")
async def add_task(new_task: CreateTask, session: AsyncSession = Depends(get_async_session)):
    return await crud.add_task(session=session, new_task=new_task)


@router_task.get('/get')
async def get_task(session: AsyncSession = Depends(get_async_session)):
    query = await crud.get_task(session=session)
    return query


@router_task.put("/update_head")
async def update_head_task(head_task_id: int, new_head_task: UpdateHeadTask,
                           session: AsyncSession = Depends(get_async_session)):
    return await crud.update_head_task(head_task_id=head_task_id, new_head_task=new_head_task, session=session)


@router_task.put("/update")
async def update_task(head_task_id: int, new_head_task: UpdateTask,
                      session: AsyncSession = Depends(get_async_session)):
    return await crud.update_task(head_task_id=head_task_id, new_head_task=new_head_task, session=session)


@router_task.delete("/delete")
async def delete_task(delete_id: int, session: AsyncSession = Depends(get_async_session)):
    return await crud.delete_task(delete_id=delete_id, session=session)
