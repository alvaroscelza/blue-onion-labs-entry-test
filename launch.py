from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Launch(Base):
    __tablename__ = 'launch'

    id = Column(Integer, primary_key=True)
    launch_id = Column(String)
    creation_date = Column(DateTime())
    longitude = Column(Integer)
    latitude = Column(Integer)
