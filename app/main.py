from fastapi import FastAPI
# from app.base.ionepy.ione import AppException, app_exception_handler
from app.routes import route
from fastapi.middleware.cors import CORSMiddleware
from app.base.untility import settings
app = FastAPI()

@app.on_event("startup")
async def startup():
    pass

app.include_router(route.router)
# app.add_exception_handler(AppException, app_exception_handler)
