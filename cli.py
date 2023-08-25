

from prettycli import bright_green
from  models import User, Food
from simple_term_menu import TerminalMenu
import time


class CLI():

    def __init__(self):
        current_user = None

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
        username = input("Enter your username:\n\n")
        user = User.find_by_username(username)
        print(f"Hi! {user}!")

    def exit(self):
        print("Consistency is the KEY! See ya!")

    def clear_screen(self, lines):
        print("\n"*lines)

app = CLI()
app.start()