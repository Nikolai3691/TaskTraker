from sqlalchemy import String, Column, Integer, ForeignKey, DateTime, MetaData
from sqlalchemy.orm import mapped_column, relationship

from database import Base

metadata = MetaData()


class EmployeesModel(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ful_name = Column(String(255), nullable=False)
    degree = Column(String(255), nullable=False)


class TasksModel(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    employee = relationship("EmployeesModel", backref="tasks")
    employee_id = mapped_column(ForeignKey("employees.id"))
    parent = relationship("TasksModel", backref="children", remote_side=id)  # noqa
    parent_id = mapped_column(ForeignKey("tasks.id"))
    deadline = Column(DateTime(timezone=True), nullable=True)
