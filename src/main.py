from fastapi import FastAPI

from service.router import router as service_router

app = FastAPI(title='TaskTracker')

app.include_router(service_router)
