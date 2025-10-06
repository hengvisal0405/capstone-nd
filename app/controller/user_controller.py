from sqlalchemy.ext.asyncio import AsyncSession
from app.models.users_model import User
from app.schemas.user_schemas import User as UserData


async def user_create(db: AsyncSession, user: UserData):
    new_user = User(name=user.name)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user
