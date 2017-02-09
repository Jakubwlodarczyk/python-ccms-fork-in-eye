from ui import Ui
from Common import *
import sys
from student import *
from manager_menu import ManagerMenu
import os


class EmployeeMenu:
    '''
    Handles navigating the menu after logging in as regular Employee.
    '''
    @staticmethod
    def handle_menu():
        '''
        Allows to choose an action to perform.
        '''
        options = ["View students list", "Get toilet paper"]
        while True:
            Ui.print_menu("\nWhat you want to do?", options, "Log out")
            inputs = Ui.get_inputs(["Please enter a number: "], "")
            option = inputs[0]
            if option == '1':
                ManagerMenu.show_students()
            elif option == '2':
                os.system('clear')
                Ui.print_message('\nToilet paper has been purchased.\nCongratulations!!!!!\n\n\n:)))')
                Ui.get_inputs([''], 'Press enter to go back')

            elif option == '0':
                sys.exit()
            else:
                Ui.print_message('There is no such option.')
