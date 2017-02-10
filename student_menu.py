from ui import Ui
from Common import Common
import sys
from student import Student
from submission import Submission
from attendance import Attendance
import os


class StudentMenu:
    """
    handle navigation menu after logging in as student
    """
    @staticmethod
    def handle_menu(user):
        '''
        Allows to choose an action to perform.
        '''
        options = ['View grades', "Submit an assignment", 'View attandence']

        while True:

            Ui.print_message(('\n...:::Logged in as {}:::...\n').format(user))
            Ui.print_menu("What do you want to do?", options, 'Exit')
            inputs = Ui.get_inputs(["Please enter a number: "], "")
            option = inputs[0]

            if option == '1':
                StudentMenu.show_grades(user)

            elif option == '2':
                os.system('clear')
                user.submit_assignment()

            elif option == '3':
                StudentMenu.show_attendance(user)

            elif option == '0':
                Common.write_submission_to_db('database.db', Submission.submission_list)
                sys.exit()
            else:
                Ui.print_message('There is no such option.')

    def show_grades(user):
        '''
        Prepares data to display in a formatted table.
        '''
        submissions = user.view_grades()
        table = Ui.create_submission_table_to_print(submissions)
        title = ('\nYour submissions:\n')
        title_list = ['Submission name', 'Grade']
        Ui.print_table(table, title, title_list)

    @staticmethod
    def show_attendance(user):
        '''
        Prepares data to display in a formatted table.
        '''
        data = Attendance.attendances_list
        table = user.check_attendence(data)
        title = 'Your attendance'
        title_list = ['Date', 'Attendance [%]']
        Ui.print_table(table, title, title_list)
