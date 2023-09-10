from sqlalchemy import select, insert, delete, update
from sqlalchemy.orm import query
from service.models import EmployeesModel, TasksModel
from service.schemas import CreateEmployee, CreateTask, CreateHeadTask, EmployeeUpdate, UpdateTask, UpdateHeadTask
from sqlalchemy.ext.asyncio import AsyncSession


async def add_employee(session: AsyncSession, new_employee: CreateEmployee):
    create_employee = insert(EmployeesModel).values(**new_employee.dict())
    await session.execute(create_employee)
    await session.commit()
    return {'status': 'success'}


async def get_employee(session: AsyncSession):
    employee = select(EmployeesModel)
    result = await session.execute(employee)
    return result.scalars().all()


async def update_employee(session: AsyncSession, employee_id: int, employee_update: EmployeeUpdate):
    new_employee = update(EmployeesModel).where(EmployeesModel.id == employee_id).values(**employee_update.dict())
    await session.execute(new_employee)
    await session.commit()
    return {'status': 'success'}


async def delete_employee(session: AsyncSession, delete_id: int):
    del_employee = delete(EmployeesModel).where(EmployeesModel.id == delete_id)
    await session.execute(del_employee)
    await session.commit()


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


async def get_task(session: AsyncSession):
    task = select(TasksModel).order_by(TasksModel.id)
    result = await session.execute(task)
    return result.scalars().all()


async def update_head_task(session: AsyncSession, head_task_id: int, new_head_task: UpdateHeadTask):
    new_task = update(TasksModel).where(TasksModel.id == head_task_id)
    await session.execute(new_task.values(**new_head_task.dict()))
    await session.commit()
    return {'status': 'success'}


async def update_task(session: AsyncSession, head_task_id: int, new_head_task: UpdateTask):
    new_task = update(TasksModel).where(TasksModel.id == head_task_id)
    await session.execute(new_task.values(**new_head_task.dict()))
    await session.commit()
    return {'status': 'success'}


async def delete_task(session: AsyncSession, delete_id: int):
    del_task = delete(TasksModel).where(TasksModel.id == delete_id)
    await session.execute(del_task)
    await session.commit()
