

from prettycli import bright_green
from  models import User, Food
from simple_term_menu import TerminalMenu
import time


class CLI():

    def __init__(self):
        current_user = None #Done
        current_user_calorie = 0
        current_user_target_calorie = 0 #Done
        current_user_weight = 0 #Done
        current_user_activity = 0 #Done
        current_user_goal = 0 #Done
        activity = 0

    def start(self):
        self.clear_screen(44)
        options = ["Login","Create Username","Exit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

        if options[menu_entry_index] == "Login":
            self.handle_login()
        if options[menu_entry_index] == "Create Username":
            self.handle_new_user()
        else:
            self.exit()

    def handle_new_user(self):
        username = input("Enter a unique username:\n")
        user = User.find_or_create_username(username)
        if user:
            self.clear_screen(44)
            print("User already in used! please login")
            time.sleep(2)
            self.start()
            # print(f"\nHi! {user}!\n\nLet's get started!")
            # self.current_user = user

            # time.sleep(1)
            # self.clear_screen(44)
            # self.user_weight()
        else:
            self.clear_screen(44)
            print(f"\nHi! {user}!\n\nLet's get started!")
            self.current_user = user

            time.sleep(2)
            self.clear_screen(3)
            self.user_weight()

    def user_weight(self):
            weight = input("\nPlease enter your weight:\n")
            self.current_user_weight = weight

            time.sleep(1)
            self.user_activity_level()
        
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

    def user_goal(self):
        self.clear_screen(44)
        print("What is your goal:\n\n1 - Lose Weight\n2 - Maintain Weight\n3 - Gain Weight\n\n")
        options = ["1","2","3"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

        if options[menu_entry_index] == "1":
            self.current_user_goal = 1
            self.current_user_target_calorie = int(self.current_user_weight) * (13 + self.activity)

        if options[menu_entry_index] == "2":
            self.current_user_goal = 2
            self.current_user_target_calorie = int(self.current_user_weight) * (15 + self.activity)

        if options[menu_entry_index] == "3":
            self.current_user_goal = 3
            self.current_user_target_calorie = int(self.current_user_weight) * (17 + self.activity)
        
        import ipdb; ipdb.set_trace()


    def user_interface(self):
        pass

 

    def exit(self):
        print("Consistency is the KEY! See ya!")
        self.clear_screen(44)

    def clear_screen(self, lines):
        print("\n"*lines)

    
app = CLI()
app.start()