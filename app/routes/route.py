from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.base.database import get_db
from app.schemas.user_schemas import User as UserData
from app.controller.user_controller import user_create

router = APIRouter()


@router.get("/tenants/plan/index")
async def func_plan_index():
    return {"jello": "hi"}


@router.get("/tenants/plan/testing")
async def func_plan_index_testing():
    return {"jellasdfasdfasdfo": "hi"}


@router.post("/users/create")
async def func_user_create(db: AsyncSession = Depends(get_db),
                           user_data: UserData = Depends()):
    return await user_create(db, user=user_data)
