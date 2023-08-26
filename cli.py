

from prettycli import bright_green
from  models import User, Food
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
        current_user_calorie = 0
        current_user_target_calorie = 0 
        current_user_fname = None
        current_user_lname = None
        current_user_weight = 0 
        current_user_activity = 0 
        current_user_goal = 0 
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

    #USER INTERFACE
    def user_interface(self):
        print("User Interface")
        import ipdb; ipdb.set_trace()
        
    #HANDLE EXISTING USER
    def handle_existing_user(self):
        username = input("Enter your username:\n")
        user = User.find_username(username)
        
        
        if user:
            self.clear_screen(44)
            print(f"Welcome back {username}!")

            self.current_user = user.username
            self.current_user_fname = user.first_name
            self.current_user_lname = user.last_name
            self.current_user_weight = user.weight
            self.current_user_activity = user.activity_level
            self.current_user_goal = user.goal
            self.current_user_target_calorie = user.target_calorie
            self.current_calorie=0

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
            self.current_user_goal = 1
            self.current_user_target_calorie = int(self.current_user_weight) * (13 + self.activity)
            self.current_user_calorie = 0 
            self.save_user_data()        
        if options[menu_entry_index] == "2":
            self.current_user_goal = 2
            self.current_user_target_calorie = int(self.current_user_weight) * (15 + self.activity)
            self.current_user_calorie = 0
            self.save_user_data() 
        if options[menu_entry_index] == "3":
            self.current_user_goal = 3
            self.current_user_target_calorie = int(self.current_user_weight) * (17 + self.activity)
            self.current_user_calorie = 0
            self.save_user_data() 
 # CHECK ALL Values has been assigned before adding in to the table
    

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


    def exit(self):
        print("Consistency is the KEY! See ya!")
        self.clear_screen(44)

    def clear_screen(self, lines):
        print("\n"*lines)

    
app = CLI()
app.start()