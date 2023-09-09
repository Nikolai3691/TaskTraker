from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session

from service import crud
from service.schemas import CreateEmployee, CreateTask, CreateHeadTask

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


@router_task.get('/get')
async def get_task(session: AsyncSession = Depends(get_async_session)):
    query = await crud.get_task(session=session)
    return query


@router_task.post("/add")
async def add_task(new_task: CreateTask, session: AsyncSession = Depends(get_async_session)):
    return await crud.add_task(session=session, new_task=new_task)


@router_task.post("/add/head")
async def add_task(new_task: CreateHeadTask, session: AsyncSession = Depends(get_async_session)):
    return await crud.add_head_task(session=session, new_task=new_task)
