from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import create_engine,Column, Float, Integer, String, ForeignKey
import time
from sqlalchemy.orm import sessionmaker



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

    # @classmethod
    def find_or_create_username(username):
        user = session.query(User).filter_by(username=username).first()
        # import ipdb; ipdb.set_trace()
        
        if user:
            return user
        else:
            # new_user = User(username = username)
            # session.add(new_user)
            # session.commit()
            print(f"User {username} has been created!")
            time.sleep(1)
            
            
            

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

    def __repr__(self):
        return f"\n<Meal"\
            + f"id = {self.id}, "\
            + f"food_name = {self.food_name}, "\
            + f"category = {self.category}, "\
            + f"calorie = {self.calorie}, "\
            + f"user_id = {self.user_id}, "\
            + ">"

