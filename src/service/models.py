from sqlalchemy import String, Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import mapped_column, relationship

from database import Base


class EmployeesModel(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    ful_name = Column(String(255), nullable=False)
    degree = Column(String(255), nullable=False)


class TasksModel(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    task = Column(String(255), nullable=False)
    parent = relationship("TasksModel", backref="children", remote_side=id)  # noqa
    status = Column(String(255), default="in work")
    parent_id = mapped_column(ForeignKey("tasks.id"))
    employee = relationship("EmployeesModel", backref="tasks")
    employee_id = mapped_column(ForeignKey("employees.id"))
    deadline = Column(DateTime(timezone=True), nullable=True)
