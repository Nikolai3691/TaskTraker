from sqlalchemy import select, insert, delete, update
from service.models import EmployeesModel, TasksModel
from service.schemas import CreateEmployee, CreateTask, CreateHeadTask
from sqlalchemy.ext.asyncio import AsyncSession


async def get_employee(session: AsyncSession):
    employee = select(EmployeesModel).order_by(EmployeesModel.id)
    result = await session.execute(employee)
    return result.scalars().all()


async def add_employee(session: AsyncSession, new_employee: CreateEmployee):
    create_employee = insert(EmployeesModel).values(**new_employee.dict())
    await session.execute(create_employee)
    await session.commit()
    return {'status': 'success'}


async def get_task(session: AsyncSession):
    task = select(TasksModel).order_by(TasksModel.id)
    result = await session.execute(task)
    return result.scalars().all()


async def add_head_task(session: AsyncSession, new_task: CreateHeadTask):
    create_task = insert(TasksModel).values(**new_task.dict())
    await session.execute(create_task)
    await session.commit()
    return {'status': 'success'}


async def add_task(session: AsyncSession, new_task: CreateTask):
    create_task = insert(TasksModel).values(**new_task.dict())
    await session.execute(create_task)
    await session.commit()
    return {'status': 'success'}
