# app/schemas/user.py
from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    name: str
class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    name: Optional[str] = None


class User(UserBase):
    id: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)
