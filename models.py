from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import create_engine,Column, Float, Integer, String, ForeignKey
import time
from sqlalchemy.orm import sessionmaker
import requests
import json


engine = create_engine("sqlite:///data.db")
Session = sessionmaker(bind=engine)
session = Session()



Base = declarative_base()

# SCHEMA
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True )
    username = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    weight = Column(Integer)
    activity_level = Column(Integer)
    goal = Column(String)
    target_calorie = Column(Integer)
    current_calorie = Column(Integer)

    #food relationship
    foods = relationship("Food", backref="User")

    
    def find_or_create_username(username):
        user = session.query(User).filter_by(username=username).first()
        
        if user:
            return user
        else:
            print(f"User {username} has been created!")
            time.sleep(1)
            
    def find_username(username):
        user = session.query(User).filter_by(username=username).first()
        
        if user:
            return user
        
    def update_user_weight(username,new_value):
        user = session.query(User).filter_by(username=username).first()
        user.weight = new_value
        session.commit()
        
    def update_user_goal(username,new_value):
        user = session.query(User).filter_by(username=username).first()
        user.goal = new_value
        session.commit()

    def update_user_activity_level(username,new_value):
        user = session.query(User).filter_by(username=username).first()
        user.activity_level = new_value
        session.commit()


    def __repr__(self):
        return f"\n<User"\
            + f"id = {self.id}, "\
            + f"username = {self.username}, "\
            + f"first_name = {self.first_name}, "\
            + f"last_name = {self.last_name}, "\
            + f"weight = {self.weight}, "\
            + f"activity level = {self.activity_level}, "\
            + f"goal = {self.goal}, "\
            + f"target calorie = {self.target_calorie}, "\
            + f"current calorie = {self.current_calorie}, "\
            + ">"


class Food(Base):
    __tablename__ = 'foods'

    id = Column(Integer, primary_key=True)
    food_name = Column(String)
    category = Column(Integer)
    calorie = Column(Float)
    #user_id foreign_key
    user_id = Column(Integer, ForeignKey("users.id"))


    def find_food(search_food):
        query = search_food
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
        response = requests.get(api_url, headers={ 'X-Api-Key': 'g1YS+rGcrHNzKP5Cghvkig==kq6PuzyW9qltjQLs'})
        food_fetched = json.loads(response.text)

        if food_fetched:
            return food_fetched
        
    def lookup_food(user_id):
        lookup_food = session.query(Food).filter_by(user_id=user_id).all()
        return lookup_food

    def delete_food(user_id,food):
        lookup_delete = session.query(Food).where(Food.food_name==food,Food.user_id==user_id).first()
        session.delete(lookup_delete)
        session.commit()
        return lookup_delete

    def __repr__(self):
        return f"\n<Meal"\
            + f"id = {self.id}, "\
            + f"food_name = {self.food_name}, "\
            + f"category = {self.category}, "\
            + f"calorie = {self.calorie}, "\
            + f"user_id = {self.user_id}, "\
            + ">"

