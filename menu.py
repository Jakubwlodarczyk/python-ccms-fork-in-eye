import sys
from user import *
from student import *
from employee import *
from mentor import *
from menager import *
from submission import *
from assigment import *
from attendance import Attendace
from ui import Ui


class Menu:
    pass

    @staticmethod
    def log_in():
        Ui.print_menu()
        login = UI.get_inputs('your_login')
        user = User.get_inputs(login)
        password = UI.get_inputs('your password')

    def exit_program():  # save csv files
        pass

    def loading_data():  # load all data
        pass

    @classmethod
    def choose_option(cls):
        inputs = UI.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
            log_in()
        elif option == "0":
            sys.exit(0)
        else:
            raise KeyError as error:
                ui.print_error_message('There is no such an option')

    @classmethod
    def main_menu(cls):
        options = ["LOGIN",
                   "SOMETHING"]
        ui.print_menu("MAIN MENU", options, "EXIT PROGRAM")

    @staticmethod
    def main():
        while True:
            main_menu()
            try:
                choose_option()
            except KeyError as error:
                ui.print_error_message('unknown error at main!')


if __name__ == '__main__':
    main()
