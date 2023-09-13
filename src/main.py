from fastapi import FastAPI

from service.router import *

app = FastAPI(title='TaskTracker')

app.include_router(router_employee)
app.include_router(router_task)
app.include_router(router_service)
