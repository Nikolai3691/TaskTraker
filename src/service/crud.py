from sqlalchemy import select, insert, delete, update
from typing import List

from sqlalchemy.orm import selectinload, subqueryload
from service.models import EmployeesModel, TasksModel
from service.schemas import CreateEmployee, CreateTask, CreateHeadTask, EmployeeUpdate, UpdateTask, UpdateHeadTask, \
    GetEmployee, GetTask
from sqlalchemy.ext.asyncio import AsyncSession


async def add_employee(session: AsyncSession, new_employee: CreateEmployee):
    create_employee = insert(EmployeesModel).values(**new_employee.dict())
    await session.execute(create_employee)
    await session.commit()
    return new_employee


async def get_employee(session: AsyncSession):
    employee = select(EmployeesModel)
    result = await session.execute(employee)
    return result.scalars().all()


async def update_employee(session: AsyncSession, employee_id: int, employee_update: EmployeeUpdate):
    new_employee = update(EmployeesModel).where(EmployeesModel.id == employee_id).values(**employee_update.dict())
    await session.execute(new_employee)
    await session.commit()
    return employee_update


async def delete_employee(session: AsyncSession, delete_id: int):
    del_employee = delete(EmployeesModel).where(EmployeesModel.id == delete_id)
    await session.execute(del_employee)
    await session.commit()


async def add_head_task(session: AsyncSession, new_task: CreateHeadTask):
    create_task = insert(TasksModel).values(**new_task.dict())
    await session.execute(create_task)
    await session.commit()
    return new_task


async def add_task(session: AsyncSession, new_task: CreateTask):
    create_task = insert(TasksModel).values(**new_task.dict())
    await session.execute(create_task)
    await session.commit()
    return new_task


async def get_task(session: AsyncSession):
    task = select(TasksModel).options(subqueryload(TasksModel.employee))
    result = await session.execute(task)
    return result.scalars().all()


async def update_head_task(session: AsyncSession, head_task_id: int, new_head_task: UpdateHeadTask):
    new_task = update(TasksModel).where(TasksModel.id == head_task_id)
    await session.execute(new_task.values(**new_head_task.dict()))
    await session.commit()
    return new_head_task


async def update_task(session: AsyncSession, task_id: int, new_task: UpdateTask):
    task = update(TasksModel).where(TasksModel.id == task_id)
    await session.execute(task.values(**new_task.dict()))
    await session.commit()
    return new_task


async def delete_task(session: AsyncSession, delete_id: int):
    del_task = delete(TasksModel).where(TasksModel.id == delete_id)
    await session.execute(del_task)
    await session.commit()


async def get_busy_employee(session: AsyncSession):
    task = select(TasksModel).filter(TasksModel.status == 'in work').options(subqueryload(TasksModel.employee))
    return [f'сотрудник: {el.employee.ful_name}, задача: {el.task} id - {el.id} родительская задача - {el.parent_id}'
            for el in await session.scalars(task)]


async def get_task_not_in_work(session: AsyncSession):
    task = select(TasksModel).where(TasksModel.status != 'in work').filter(TasksModel.parent_id != None)
    result = await session.execute(task)
    return result.scalars().all()


async def get_list_objects(session: AsyncSession):
    list_objects = select(TasksModel).filter(TasksModel.parent_id == None).options(subqueryload(TasksModel.employee))
    return [(el.task, el.deadline, [el.employee.ful_name]) for el in await session.scalars(list_objects)]

