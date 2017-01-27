from ui import *
from Common import *
import sys
from student import *
from submission import *
import os


class StudentMenu:
    @staticmethod
    def handle_menu():
        '''
        Allows to choose an action to perform.
        '''
        options = ['View grades', "Submit an assignment"]
        while True:

            Ui.print_menu("What you want to do?", options, 'Exit')

            inputs = Ui.get_inputs(["Please enter a number: "], "")

            option = inputs[0]

            if option == '1':
                os.system('clear')
                Student.view_grades()

            elif option == '2':
                os.system('clear')
                Student.submit_assignment()

            elif option == '0':
                sys.exit()
            else:
                Ui.print_error_message('There is no such option.')
