

from prettycli import bright_green
from  models import User, Food
from simple_term_menu import TerminalMenu
import time


class CLI():

    def __init__(self):
        current_user = None
        current_user_calorie = 0
        current_user_target_calorie = 0
        current_user_weight = 0
        current_user_activity = 0
        current_user_goal = 0

    def start(self):
        self.clear_screen(44)
        options = ["Login","Exit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

        if options[menu_entry_index] == "Login":
            self.handle_login()
        else:
            self.exit()

    def handle_login(self):
        username = input("Enter your username:\n")
        user = User.find_by_username(username)
        if user:
            print(f"\nHi! {user}!\n\nLet's get started!")
            self.current_user = user

            time.sleep(1)
            self.clear_screen(44)
            self.user_weight()
        else:
            print("Invalid Username")

    def user_weight(self):
            weight = input("\nPlease enter your weight:\n")
            self.current_user_weight = weight

            time.sleep(1)
            self.user_activity_level()
        
    def user_activity_level(self):
        self.clear_screen(44)
        print("Enter your activity level:\n1 - Sedentary \n2 - Lightly - Active \n3 - Active \n4 - Very Active")
        options = ["1","2","3","4"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

        if options[menu_entry_index] == "1":
            self.user_activity_level = 1
        if options[menu_entry_index] == "2":
            self.user_activity_level = 2
        if options[menu_entry_index] == "3":
            self.user_activity_level = 3
        if options[menu_entry_index] == "4":
            self.user_activity_level = 4

    def exit(self):
        print("Consistency is the KEY! See ya!")

    def clear_screen(self, lines):
        print("\n"*lines)

app = CLI()
app.start()