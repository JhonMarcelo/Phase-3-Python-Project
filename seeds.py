from models import User, Food   # You will need to import your own models
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
# For generating Fake data: https://faker.readthedocs.io/en/master/providers.html
from faker import Faker
#add this line so can use fake. somthing
fake = Faker()
import random

engine = create_engine("sqlite:///data.db")
Session = sessionmaker(bind=engine)
session = Session() # Query the DB with session example: session.query(ModelOne).all()

# Use ipdb to interact with DB using session
# import ipdb; ipdb.set_trace() # # Dont forget to add ipdb as a dependency - pipenv install ipdb



# For working with an API and retrieving json data
import requests
import json

print("Seeding...")
# session.query(User.delete())



for _ in range(20):
    
    weight = random.randint(90,215)
    first_name=fake.first_name()
    last_name=fake.last_name()
    user_name = f"{first_name}_{last_name}"

    rand = random.randint(1,3)
    
    if rand == 1:
        goal = "Lose Weight"
        target_calorie = weight
    if rand == 2:
        goal = "Maintain Weight"
    if rand == 3:
        goal = "Gain Weight"

    
    user = User(username=user_name,first_name=first_name,last_name=last_name,weight=weight,goal = goal,target_calorie=)
    print(user)


# Example request
response = requests.get(API_URL)
json_data = json.loads(response.text)
