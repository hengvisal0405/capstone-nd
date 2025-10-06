from sqlalchemy import Column, Integer, String, TIMESTAMP, func
from app.base.database import Base
from sqlalchemy import Column, Integer, String, DateTime
# from app.base.ionepy.ione import get_phnom_penh_time, ActiveStatus


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    created_at = Column(DateTime )
