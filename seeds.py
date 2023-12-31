from models import User, Food   # You will need to import your own models
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
# For generating Fake data: https://faker.readthedocs.io/en/master/providers.html
from faker import Faker

fake = Faker()
import random

engine = create_engine("sqlite:///data.db")
Session = sessionmaker(bind=engine)
session = Session() # Query the DB with session example: session.query(ModelOne).all()

import requests
import json
 
print("Seeding...")
# session.query(User.delete())



for _ in range(20):
    
    weight = random.randint(90,215)
    first_name=fake.first_name()
    last_name=fake.last_name()
    user_name = f"{first_name}_{last_name}"


    #1 - Sedentary 2 - Lightly - Active 3 - Active 4 - Very Active
    activity_level = random.randint(1,4)
    if activity_level ==1:
        activity = -4
        
    if activity_level ==2:
        activity = -2
    if activity_level ==3:
        activity = 0
    if activity_level ==4:
        activity = 4
    

    random_goal = random.randint(1,3)
    if random_goal == 1:
        goal = "Lose Weight"
        target_calorie = weight * (13 + activity )
    if random_goal == 2:
        goal = "Maintain Weight"
        target_calorie = weight * (15 + activity)
    if random_goal == 3:
        goal = "Gain Weight"
        target_calorie = weight * (17 + activity)

    
    user = User(username=user_name,first_name=first_name,last_name=last_name,weight=weight,activity_level=activity_level,goal = goal,target_calorie=target_calorie,current_calorie=0)
    
    # session.add(user)
    # session.commit()
