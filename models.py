from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()

# SCHEMA
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True )
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    weight = Column(Integer)
    goal = Column(Integer)
    target_calorie = Column(Integer)
    current_calorie = Column(Integer)



