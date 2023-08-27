

from prettycli import bright_green
from models import User, Food
from simple_term_menu import TerminalMenu
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import time

engine = create_engine("sqlite:///data.db")
Session = sessionmaker(bind=engine)
session = Session()

class CLI():

    def __init__(self):
        current_user = None 
        current_user_id = 0
        current_user_calorie = 0
        current_user_target_calorie = 0 
        current_user_fname = None
        current_user_lname = None
        current_user_weight = 0 
        current_user_activity = 0 
        current_user_goal = None 
        activity = 0

    def start(self):
        self.clear_screen(44)
        
        options = ["Login","Create Username","Exit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

        if options[menu_entry_index] == "Login":
            self.handle_existing_user()
        if options[menu_entry_index] == "Create Username":
            self.handle_new_user()
        if options[menu_entry_index] == "Exit":
            self.exit()


    
        #HANDLE EXISTING USER
    def handle_existing_user(self):
        username = input("Enter your username:\n")
        user = User.find_username(username)
        
        
        if user:
            self.clear_screen(44)
            print(f"Welcome back {username}!")

            
            
            self.current_user = user.username
            self.current_user_id = user.id
            self.current_user_fname = user.first_name
            self.current_user_lname = user.last_name
            self.current_user_weight = user.weight
            self.current_user_activity = user.activity_level
            self.current_user_goal = user.goal
            self.current_user_target_calorie = user.target_calorie
            self.current_user_calorie=0
            self.activity = user.activity_level
            self.user_interface()


        else:
            print("User not found. Please create one.")
            time.sleep(2)
            self.start()


    #HANDLE NEW USER FUNCTION
    def handle_new_user(self):
        username = input("Enter a unique username:\n")
        user = User.find_or_create_username(username)
        if user:
            self.clear_screen(44)
            print("User already in used! please login.")
            time.sleep(2)
            self.start()


        else:
            self.clear_screen(44)
            print(f"\nHi! {username}!\n\nLet's get started!")
            self.current_user = username
            time.sleep(1)
            self.clear_screen(3)
            self.user_fname_lname()


    #USER FNAME AND LNAME FUNCTION
    def user_fname_lname(self):
            self.current_user_fname = input("Enter first name:\n")
            self.current_user_lname = input("\nEnter last name:\n")
            self.user_weight()

    #USER WEIGHT FUNCTION
    def user_weight(self):
            weight = input("\nPlease enter your weight:\n")
            self.current_user_weight = weight

            time.sleep(1)
            self.user_activity_level()
        
    #USER ACTIVITY LEVEL FUNCTION
    def user_activity_level(self):
        self.clear_screen(44)
        print("Enter your activity level:\n\n1 - Sedentary \n2 - Lightly - Active \n3 - Active \n4 - Very Active\n\n")
        options = ["1","2","3","4"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

        if options[menu_entry_index] == "1":
            self.current_user_activity = 1
            self.activity = -4

            time.sleep(1)
            self.user_goal()
        if options[menu_entry_index] == "2":
            self.current_user_activity = 2
            self.activity = -2

            time.sleep(1)
            self.user_goal()
        if options[menu_entry_index] == "3":
            self.current_user_activity = 3
            self.activity = 0

            time.sleep(1)
            self.user_goal()
        if options[menu_entry_index] == "4":
            self.current_user_activity = 4
            self.activity = 4

            time.sleep(1)
            self.user_goal()

    #USER GOAL FUNCTION
    def user_goal(self):
        self.clear_screen(44)
        print("What is your goal:\n\n1 - Lose Weight\n2 - Maintain Weight\n3 - Gain Weight\n\n")
        options = ["1","2","3"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        
        if options[menu_entry_index] == "1":
            self.current_user_goal = "Lose Weight"
            self.current_user_target_calorie = int(self.current_user_weight) * (13 + self.activity)
            self.current_user_calorie = 0 
            self.save_user_data()        
        if options[menu_entry_index] == "2":
            self.current_user_goal = "Maintain Weight"
            self.current_user_target_calorie = int(self.current_user_weight) * (15 + self.activity)
            self.current_user_calorie = 0
            self.save_user_data() 
        if options[menu_entry_index] == "3":
            self.current_user_goal = "Gain Weight"
            self.current_user_target_calorie = int(self.current_user_weight) * (17 + self.activity)
            self.current_user_calorie = 0
            self.save_user_data() 
 # CHECK ALL Values has been assigned before adding in to the table
    
    #SAVE THE USER DATA
    def save_user_data(self):
        username = self.current_user
        first_name = self.current_user_fname
        last_name = self.current_user_lname
        weight = self.current_user_weight
        activity_level = self.current_user_activity
        goal = self.current_user_goal
        target_calorie = self.current_user_target_calorie
        current_calorie=0

        new_user = User(username=username,first_name=first_name,last_name=last_name,weight=weight,activity_level=activity_level,goal = goal,target_calorie=target_calorie,current_calorie=current_calorie)
        session.add(new_user)
        session.commit()

        print("Registration Complete!")

        getUser = session.query(User).filter_by(username=self.current_user)
        self.current_user_id = getUser[0].id

    #USER INTERFACE
    def user_interface(self):
        

        self.clear_screen(44)
        self.display_calorie()
        options = ["Start Tracking","Update Weight","Update Goal","Update Activtiy Level","Exit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

        if options[menu_entry_index] == "Start Tracking":
            self.track_food()
        if options[menu_entry_index] == "Update Weight":
            self.update_weight()
        if options[menu_entry_index] == "Update Goal":
            self.update_goal()
        if options[menu_entry_index] == "Update Activtiy Level":
            self.update_activity_level()
        if options[menu_entry_index] == "Exit":
            self.exit()
            
    #HANDLE FOOD TRACKING
    def track_food(self):
        
        self.clear_screen(44)
        self.display_calorie()
        
        search_food = input("Enter the food name:")
        food = Food.find_food(search_food)
        
        
        if food:

            # import ipdb; ipdb.set_trace()
            food_name = food[0]["name"]
            calorie = food[0]["calories"]
            user_id = self.current_user_id

            print("1 - Breakfast","2 - Lunch","3 - Dinner")
            options = ["1","2","3"]
            terminal_menu = TerminalMenu(options)
            menu_entry_index = terminal_menu.show()

            if options[menu_entry_index] == "1":
             category = 1
            if options[menu_entry_index] == "2":
                category = 2
            if options[menu_entry_index] == "3":
                category = 3

            self.current_user_target_calorie -= calorie
            self.current_user_calorie += calorie

            add_food = Food(food_name=food_name,category=category,calorie=calorie,user_id=user_id)
            session.add(add_food)
            session.commit()
            print(f"Your {search_food} is added!")
            time.sleep(2)
            self.user_interface()

        else:
            print("Sorry, that food is not on the list. Please try again.")
            time.sleep(2)
            self.clear_screen(44)
            self.track_food()

    #DISPLAY CALORIE INTAKE AND TARGET
    def display_calorie(self):

        print(f"You have {self.current_user_target_calorie} calorie/s left.")
        print(f"Your current calorie intake is {self.current_user_calorie}.\n")
        self.clear_screen(4)
    
    #UPDATE USER WEIGHT
    def update_weight(self):
        updated_weight = input("Please enter updated weight:")
        self.current_user_weight = updated_weight

        User.update_user_weight(self.current_user,updated_weight)
        print(f"Weight updated to {updated_weight}!")
        time.sleep(1)
        self.user_interface()
    
    #UPDATE USER GOAL
    def update_goal(self):
        print("Let's update your goal!")
        print("What is your current goal:\n\n1 - Lose Weight\n2 - Maintain Weight\n3 - Gain Weight\n\n")
        options = ["1","2","3"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        
        if options[menu_entry_index] == "1":
            self.current_user_goal = "Lose Weight"
            self.current_user_target_calorie = int(self.current_user_weight) * (13 + self.activity)
            User.update_user_goal(self.current_user,self.current_user_goal)

        if options[menu_entry_index] == "2":
            self.current_user_goal = "Maintain Weight"
            self.current_user_target_calorie = int(self.current_user_weight) * (15 + self.activity)
            User.update_user_goal(self.current_user,self.current_user_goal)

        if options[menu_entry_index] == "3":
            self.current_user_goal = "Gain Weight"
            self.current_user_target_calorie = int(self.current_user_weight) * (17 + self.activity)
            User.update_user_goal(self.current_user,self.current_user_goal)
            
        print(f"User goal is updated to {self.current_user_goal}")
        time.sleep(1)
        self.user_interface()

    def update_activity_level(self):
        print("Let's update your activity level!\n")
        print("What is your current activity level:\n\n1 - Sedentary \n2 - Lightly - Active \n3 - Active \n4 - Very Active\n\n")
        options = ["1","2","3","4"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        how_active = None

        if options[menu_entry_index] == "1":
            self.current_user_activity = 1
            self.activity = -4
            how_active = "Sedentary"
            User.update_user_activity_level(self.current_user,self.current_user_activity)

        if options[menu_entry_index] == "2":
            self.current_user_activity = 2
            self.activity = -2
            how_active = "Lightly Active"
            User.update_user_activity_level(self.current_user,self.current_user_activity)

        if options[menu_entry_index] == "3":
            self.current_user_activity = 3
            self.activity = 0
            how_active = "Active"
            User.update_user_activity_level(self.current_user,self.current_user_activity)

        if options[menu_entry_index] == "4":
            self.current_user_activity = 4
            self.activity = 4
            how_active = "Very Active"
            User.update_user_activity_level(self.current_user,self.current_user_activity)

        print(f"User activity level is updated to {how_active}")
        time.sleep(1)
        self.user_interface()
        
        
        
        time.sleep(1)
        self.user_interface()
    def exit(self):
        print("Consistency is the KEY! See ya!")
        self.clear_screen(44)

    def clear_screen(self, lines):
        print("\n"*lines)

    
app = CLI()
app.start()