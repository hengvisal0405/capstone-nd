from fastapi import APIRouter, Depends, Query
# from sqlalchemy.ext.asyncio import AsyncSession
# from typing import Optional
# from app.base.database import get_db
# from app.base.ionepy.ione import get_language
# from app.schemas.tenant.tenant_schemas import TenantData
# from app.controller.plan.plan_controller import plan_index
# from app.controller.tenant.tenant_controller import (tenant_index, tenant_view,
#                                                      tenant_update)
router = APIRouter()


@router.get("/tenants/plan/index")
async def func_plan_index():
    return {'jello': "hi"}


@router.get("/tenants/plan/testing")
async def func_plan_iaaandex():
    return {'jellasdfasdfasdfo': "hi"}


# @router.get("/tenants/company/index")
# async def func_company_index(name: Optional[str] = None,
#                              email: Optional[str] = None,
#                              address: Optional[str] = None,
#                              plan: Optional[str] = None,
#                              page_size: int = 20,
#                              page: int = 1,
#                              db: AsyncSession = Depends(get_db)):
#     return await tenant_index(
#         db=db,
#         name=name,
#         email=email,
#         address=address,
#         plan=plan,
#         page_size=page_size,
#         page=page,
#     )

# @router.get("/tenants/company/view/")
# async def func_company_view(tenant_id: int = Query(...),
#                             db: AsyncSession = Depends(get_db)):
#     return await tenant_view(db, tenant_id)

# @router.put('/tenants/company/update/')
# async def func_company_update(tenant_id: int = Query(...),
#                               db: AsyncSession = Depends(get_db),
#                               tenant_data: TenantData = Depends(
#                                   TenantData.as_form)):
#     return await tenant_update(db,
#                                tenant_id=tenant_id,
#                                update_tenant=tenant_data)
