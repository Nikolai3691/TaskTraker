from sqlalchemy import select, insert, delete, update

from sqlalchemy.orm import subqueryload
from service.models import EmployeesModel, TasksModel
from service.schemas import CreateEmployee, CreateTask, CreateHeadTask, EmployeeUpdate, UpdateTask, UpdateHeadTask
from sqlalchemy.ext.asyncio import AsyncSession


class ServiceBase:
    def __init__(self, session: AsyncSession):
        self.session = session


class Employee(ServiceBase):

    async def add_employee(self, new_employee: CreateEmployee):
        create_employee = insert(EmployeesModel).values(**new_employee.dict())
        await self.session.execute(create_employee)
        await self.session.commit()
        return new_employee

    async def get_employee(self):
        employee = select(EmployeesModel)
        result = await self.session.execute(employee)
        return result.scalars().all()

    async def update_employee(self, employee_id: int, employee_update: EmployeeUpdate):
        new_employee = update(EmployeesModel).where(EmployeesModel.id == employee_id).values(**employee_update.dict())
        await self.session.execute(new_employee)
        await self.session.commit()
        return employee_update

    async def delete_employee(self, delete_id: int):
        del_employee = delete(EmployeesModel).where(EmployeesModel.id == delete_id)
        await self.session.execute(del_employee)
        await self.session.commit()


class Tasks(ServiceBase):

    async def add_head_task(self, new_task: CreateHeadTask):
        create_task = insert(TasksModel).values(**new_task.dict())
        await self.session.execute(create_task)
        await self.session.commit()
        return new_task

    async def add_task(self, new_task: CreateTask):
        create_task = insert(TasksModel).values(**new_task.dict())
        await self.session.execute(create_task)
        await self.session.commit()
        return new_task

    async def get_task(self):
        task = select(TasksModel).options(subqueryload(TasksModel.employee))
        result = await self.session.execute(task)
        return result.scalars().all()

    async def update_head_task(self, head_task_id: int, new_head_task: UpdateHeadTask):
        new_task = update(TasksModel).where(TasksModel.id == head_task_id)
        await self.session.execute(new_task.values(**new_head_task.dict()))
        await self.session.commit()
        return new_head_task

    async def update_task(self, task_id: int, new_task: UpdateTask):
        task = update(TasksModel).where(TasksModel.id == task_id)
        await self.session.execute(task.values(**new_task.dict()))
        await self.session.commit()
        return new_task

    async def delete_task(self, delete_id: int):
        del_task = delete(TasksModel).where(TasksModel.id == delete_id)
        await self.session.execute(del_task)
        await self.session.commit()


class Sevices(ServiceBase):

    async def get_busy_employee(self):
        task = select(TasksModel).filter(TasksModel.status == 'in work').options(subqueryload(TasksModel.employee))
        return [
            f'сотрудник: {el.employee.ful_name}, задача: {el.task} id - {el.id} родительская задача - {el.parent_id}'
            for el in await self.session.scalars(task)]

    async def get_task_not_in_work(self):
        task = select(TasksModel).where(TasksModel.status != 'in work').filter(TasksModel.parent_id != None)
        result = await self.session.execute(task)
        return result.scalars().all()

    async def get_list_objects(self):
        list_objects = select(TasksModel).filter(TasksModel.parent_id == None).options(
            subqueryload(TasksModel.employee))
        return [(el.task, el.deadline, [el.employee.ful_name]) for el in await self.session.scalars(list_objects)]
