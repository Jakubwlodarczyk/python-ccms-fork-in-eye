from ui import *
from Common import *
import sys
from menu import *


class StudentMenu:
    options = ["View all employees list",
               "Edit employees' data",
               "Fire an employee",
               "View mentors list",
               "Edit mentors' data",
               "Fire a mentor",
               "View students list"]

    while True:
        Ui.print_menu("What you want to do?", options, "Log out")
        inputs = Ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == '1':
            # view all employees list
            pass
        elif option == '2':
            # edit employees data
            pass
        elif option == '3':
            # fire a employee
            pass
        elif option == '4':
            # view mentors list
            pass
        elif option == '5':
            # edit employees data
            pass
        elif option == '6':
            # fire a employee
            pass
        elif option == '7':
            # fire a employee
            pass
        elif option == '0':
            #common.write_table_to_file('Mentors.csv')
            #common.write_table_to_file('Regular_employees.csv')
            sys.exit()
        else:
            Ui.print_error_message('There is no such option.')