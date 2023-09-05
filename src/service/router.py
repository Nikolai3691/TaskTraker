from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session
from sqlalchemy import select, insert, delete, update
from service.models import EmployeesModel, TasksModel
from service.schemas import CreateEmployee

router = APIRouter(
    prefix='/service',
    tags=['Service']
)


@router.post("/")
async def add_employee(nev_eployee: CreateEmployee, session: AsyncSession = Depends(get_async_session)):
    statement = insert(EmployeesModel).values(**nev_eployee.dict())
    await session.execute(statement)
    await session.commit()
    return {'status': 'success'}


@router.get("/")
async def get_employee(session: AsyncSession = Depends(get_async_session)):
    query = select(EmployeesModel).where(EmployeesModel.id == 2)
    result = await session.execute(query)
    return result.all()
