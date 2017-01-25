from menu import *
from ui import *
from Common import *
import sys

class ManagerMenu(Menu):
    '''
    Handles navigating the menu after logging in as Manager.
    '''
    def handle_menu():
        '''
        Allows to choose an action to perform.
        '''
        options = ["View regular employees list",
                   "Add an employee",
                   "Edit employees' data",
                   "Fire an employee",
                   "View mentors list",
                   "Add a mentor",
                   "Edit mentors' data",
                   "Fire a mentor",
                   "View students list"]
        while True:
            Ui.print_menu("What you want to do?", options, "Log out")
            inputs = Ui.get_inputs(["Please enter a number: "], "")
            option = inputs[0]
            if option == '1':
                title = 'Regular employees list:'
                Ui.print_staff_list(Employee.employees_list, title)
            elif option == '2':
                User.add_person(Employee.employees_list)
            elif option == '3':
                # edit employees data
                pass
            elif option == '4':
                User.remove_person(Employee.employees_list)
                pass
            elif option == '5':
                # view mentors list
                pass
            elif option == '6':
                User.add_person(Mentor.mentors_list)
            elif option == '7':
                # edit mentor's data
                pass
            elif option == '8':
                # fire mentor
                pass
            elif option == '9':
                # view student list
                pass
            elif option == '0':
                #common.write_table_to_file('Mentors.csv')
                #common.write_table_to_file('Regular_employees.csv')
                sys.exit()
            else:
                Ui.print_error_message('There is no such option.')
