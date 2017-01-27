from ui import *

from Common import *

import sys

# from menu import *

from student import *

from submission import *

import os


class StudentMenu:

    @staticmethod
    def handle_menu():
        '''
        Allows to choose an action to perform.
        '''

        options = ['View grades', "Submit an assignment", 'View attandence', 'Exit']

        while True:

            Ui.print_menu("What you want to do?", options, "Log out")

            inputs = Ui.get_inputs(["Please enter a number: "], "")

            option = inputs[0]

            if option == '1':

                os.system('clear')
                Student.view_grades()

            elif option == '2':

                os.system('clear')
                Student.submit_assignment()
