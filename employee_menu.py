from ui import Ui
from Common import *
import sys
from student import *


class EmployeeMenu:
    '''
    Handles navigating the menu after logging in as regular Employee.
    '''
    @staticmethod
    def handle_menu():
        '''
        Allows to choose an action to perform.
        '''
        options = ["View students list"]
        while True:
            Ui.print_menu("\nWhat you want to do?", options, "Log out")
            inputs = Ui.get_inputs(["Please enter a number: "], "")
            option = inputs[0]
            if option == '1':
                # show student list
                title = 'Students list:'
                Ui.print_table(Student.student_list, title)
            elif option == '0':
                #SAVE
                sys.exit()
            else:
                Ui.print_message('There is no such option.')

