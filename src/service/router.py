from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session
from sqlalchemy import select, insert, delete, update
from service.models import EmployeesModel, TasksModel
from service.schemas import CreateEmployee, CreateTaskFirst, CreateTaskNext

router = APIRouter(
    prefix='/service',
    tags=['Service']
)


@router.post("/employye")
async def add_employee(nev_eployee: CreateEmployee, session: AsyncSession = Depends(get_async_session)):
    statement = insert(EmployeesModel).values(**nev_eployee.dict())
    await session.execute(statement)
    await session.commit()
    return {'status': 'success'}


@router.post("/task_first")
async def add_task_first(nev_task: CreateTaskFirst, session: AsyncSession = Depends(get_async_session)):
    statement = insert(TasksModel).values(**nev_task.dict())
    await session.execute(statement)
    await session.commit()
    return {'status': 'success'}


@router.post("/task_next")
async def add_task_next(nev_task: CreateTaskNext, session: AsyncSession = Depends(get_async_session)):
    statement = insert(TasksModel).values(**nev_task.dict())
    await session.execute(statement)
    await session.commit()
    return {'status': 'success'}


@router.get("/employee")
async def get_employee(degree: str, session: AsyncSession = Depends(get_async_session)):
    query = select(EmployeesModel).filter(EmployeesModel.degree == degree)
    result = await session.execute(query)
    return result.scalars().all()
