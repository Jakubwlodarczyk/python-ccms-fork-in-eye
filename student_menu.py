from ui import *
from Common import *
import sys
from student import *
from submission import *
from attendance import *
import os
import time


class StudentMenu:

    def handle_menu(user):
        '''
        Allows to choose an action to perform.
        '''
        options = ['View grades', "Submit an assignment", 'View attandence']

        while True:
            # os.system('clear')
            Ui.print_message(' '*32 + 'Logged in as {}\n\n'.format(user))

            Ui.print_menu("What do you want to do?", options, 'Exit')
            inputs = Ui.get_inputs(["Please enter a number: "], "")
            option = inputs[0]
            if option == '1':
                os.system('clear')
                submissions = user.view_grades()
                table = Ui.create_submission_table_to_print(submissions)
                title = ('\nYour submissions:\n')
                title_list = ['Submission name', 'Grade']
                Ui.print_table(table, title, title_list)
            elif option == '2':
                os.system('clear')
                user.submit_assignment()
            elif option == '3':
                data = Attendance.attendances_list
                for i in data:
                    print(data)
                table = user.check_attendence(data)
                os.system('clear')
                Ui.print_message('\n ...::: Data, Status :::...\n')
                for row in table:
                    Ui.print_message("{}: {}%".format(row[0], str(row[1])))
                print("\n")
            elif option == '0':
                Common.write_submission_to_db('database.db', Submission.submission_list)
                sys.exit()
                Ui.print_message('There is no such option.')
