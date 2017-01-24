import sys
from user import *
#from student import *
#from employee import *
#from mentor import *
#from menager import *
#from submission import *
#from assigment import *
#from attendance import *
from ui import *


class Menu:
    pass

    @staticmethod
    def log_in():
        title = ['USER LOGIN']
        list_options = ['Enter your email']
        Ui.print_menu(title, list_options, 'exit')
        login = Ui.get_inputs(['Your email: '], "")
        user = User.get_user(login)

    def exit_program():  # save csv files
        pass

    def loading_data():  # load all data
        pass

    @classmethod
    def choose_option(cls):
        inputs = Ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
            Menu.log_in()
        elif option == "0":
            sys.exit(0)
        #else:
            #raise KeyError as error:
                #ui.print_error_message('There is no such an option')

    @classmethod
    def main_menu(cls):
        options = ["LOGIN",
                   "SOMETHING"]
        Ui.print_menu("MAIN MENU", options, "EXIT PROGRAM")

    @staticmethod
    def main():
        while True:
            Menu.main_menu()
            try:
                Menu.choose_option()
            except KeyError:
                ui.print_error_message('unknown error at main!')


if __name__ == '__main__':
    Menu.main()
