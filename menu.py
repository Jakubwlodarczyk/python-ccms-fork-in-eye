import csv
import sys
from user import *
from Common import *
#from student import *
from employee import *
from mentor import *
#from menager import *
#from submission import *
#from assigment import *
#from attendance import *
from ui import *


class Menu:
    @staticmethod
    def loading_data():
        #User.create_staff_list()
        Employee.create_staff_list()
        #Mentor.create_staff_list()
        #Student.create_staff_list()
        #Manager.create_staff_list()
        #Assigment.create_staff_list()
        #Submission.create_staff_list()
        #Attendance.create_staff_list()

    @staticmethod
    def log_in():
        title = 'Sign in'
        list_options = []
        Ui.print_menu(title, list_options, 'exit')
        login = Ui.get_inputs(['Your email: ', 'Your password: '], "")
        user = Common.user_password_check(login, password, user_list)

    def exit_program():  # save csv files
        pass

    @classmethod
    def choose_option(cls):
        inputs = Ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
            Menu.log_in()
        elif option == "0":
            sys.exit(0)

    @classmethod
    def main_menu(cls):
        options = ["LOGIN",
                   "SOMETHING"]
        Ui.print_menu("MAIN MENU", options, "EXIT PROGRAM")

    @staticmethod
    def main():
        while True:
            Menu.loading_data()
            #User.get_all_users(staff_object_list, mentors_object_list, students_object_list, manager_object_list)
            Menu.main_menu()
            try:
                Menu.choose_option()
            except KeyError:
                ui.print_error_message('unknown error at main!')


if __name__ == '__main__':
    Menu.main()
