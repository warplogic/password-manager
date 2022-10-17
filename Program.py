import sys
from CommandOptions import CommandOptions
from HelpMenu import HelpMenu
from PasswordGenerator import PasswordGenerator

class Program:
    def __init__(self) -> None:
        pass

    def run(self) -> None:
        co = CommandOptions()
        co.sort_options(sys.argv)
        
        def display_help_menu():
            menu = HelpMenu()
            menu.display()
            exit()
        
        if len(co.options) == 0 or "keyword" not in co.options:
            display_help_menu()
        
        if co.options["keyword"] == "generate":
            generator = PasswordGenerator(co.options)
            password = generator.generate()

            if "-o" in co.options or "--once" in co.options:
                print(password)
        else:
            display_help_menu()

