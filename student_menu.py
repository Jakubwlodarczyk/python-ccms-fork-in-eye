from ui import *
from Common import *
import sys
from student import *
from submission import *
from attendance import *
import os
import time


class StudentMenu:
    @staticmethod
    def handle_menu(user):
        '''
        Allows to choose an action to perform.
        '''
        options = ['View grades', "Submit an assignment", 'View attandence']

        while True:

            Ui.print_menu("What you want to do?", options, 'Exit')
            inputs = Ui.get_inputs(["Please enter a number: "], "")
            option = inputs[0]
            if option == '1':
                os.system('clear')
                user.view_grades()
                # Student.view_grades()
            elif option == '2':
                os.system('clear')
                user.submit_assignment()
            elif option == '3':
                data = Attendance.attendance_list
                table = user.check_attendence(data)
                Ui.print_error_message('Data, Status:')
                for row in table:
                    Ui.print_error_message(': '.join(row))
            elif option == '0':
                Common.write_submission_to_file('Submissions.csv', Submission.submission_list)
                sys.exit()
                Ui.print_error_message('There is no such option.')
