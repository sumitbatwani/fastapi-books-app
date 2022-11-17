from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Students(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String) 
    age = Column(Integer)
    result = Column(Boolean, default=False)