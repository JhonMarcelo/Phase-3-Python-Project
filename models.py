from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()

# SCHEMA
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True )
    username = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    weight = Column(Integer)
    goal = Column(String)
    target_calorie = Column(Integer)
    current_calorie = Column(Integer)

    def __repr__(self):
        return f"\n<User"\
            + f"id = {self.id}, "\
            + f"username = {self.username}, "\
            + f"first_name = {self.first_name}, "\
            + f"last_name = {self.last_name}, "\
            + f"weight = {self.weight}, "\
            + f"goal = {self.goal}, "\
            + f"target calorie = {self.target_calorie}, "\
            + f"current calorie = {self.current_calorie}, "\
            + ">"


class Food(Base):
    __tablename__ = 'foods'

    id = Column(Integer, primary_key=True)
    food_name = Column(String)
    category = Column(Integer)
    calorie = Column(Integer)

    def __repr__(self):
        return f"\n<Meal"\
            + f"id = {self.id}, "\
            + f"food name = {self.food_name}, "\
            + f"category = {self.category}, "\
            + f"calorie = {self.calorie}, "\
            + ">"
