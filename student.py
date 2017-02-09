from user import *
from assignments import *
from ui import *
from Common import *
from submission import *
import sys
import os
import datetime
import sqlite3


class Student(User):

    student_list = []


    # submission_list = Submission.submission_list






    def __init__(self, name, surname, email, password, status, id, team="none", card="none"):
            User.__init__(self, name, surname, email, password, status, id)
            self.status = 'student'
            self.attendance_list = []
            # self.submission_list = Submission.submission_list
            self.team = team
            self.card = card


    def __str__(self):
        return "{} {} ".format(self.name, self.surname)

    @classmethod
    def create_objects_list_from_database(cls, table_name):  # from database
        """
        Creates abjects based on data from database.
        :param file_path:
        :return:
        """

        conn = sqlite3.connect("database.db")
        c = conn.cursor()

        name_q = "SELECT name, surname, email, password, status, card, team, student_id FROM student;"
        name_db = c.execute(name_q)
        conn.commit()

        student_list = []

        for row in name_db:
            name = row[0]
            surname = row[1]
            email = row[2]
            password = row[3]
            status = row[4]
            card = row[5]
            team = row[6]
            student_id = row[7]

            full_name = cls(name, surname, email, password, status, student_id, team, card)
            student_list.append(full_name)

        conn.close()

        return student_list

    @staticmethod
    def add_attendance_to_student(attendances_obj_list):
        for student in Student.student_list:
            for attendance in attendances_obj_list:
                if attendance.id == student.id:
                    student.attendance_list.append(attendance)


    def view_grades(self):
        '''
        Allows to view grades for all student's assignments.

        '''
        my_submiss = []
        for sub in Submission.submission_list:
            if sub.student_id == self.id:
                my_submiss.append(sub)
        Ui.print_submissions(my_submiss)

    def submit_assignment(self):

        Ui.print_message('Choose the number from the following assignments: \n')
        for n, assignment in enumerate(Assignments.assignments_list):
            Ui.print_message(str(n+1) + '. ' + str(assignment))
        choose = input('Type the chosen number here: ')
        assign = Assignments.assignments_list

        assignment_list = []
        choose_val = input('Type the submission link: ')
        for i in assign:
            assignment_list.append([datetime.date.today(), '0', i.assignment_name, choose_val, self.id])

        if not choose.isnumeric():
            os.system('clear')
            Ui.print_message('\nChosen value must be a number')
            return
        if int(choose) <= len(assignment_list):  # value condition
            chosen_one = assignment_list[int(choose)-1]
            for submiss in Submission.submission_list:
                if submiss.name == chosen_one[2] and submiss.student_id == chosen_one[4]:  # condition for assignment being submitted
                    os.system('clear')
                    Ui.print_message('Assignment is already submitted\n')
                    return

            submission_obj = Submission(chosen_one[0], chosen_one[1], chosen_one[2], # object of new submission is created
                                chosen_one[3], chosen_one[4])

# send_date, grade, name, github_link, student_id
            Submission.submission_list.append(submission_obj)
            os.system('clear')
            Ui.print_message('Your assignment was succesfully submitted\n')

            return Submission.submission_list

        else:
            os.system('clear')

            Ui.print_message('Invalid number')

    def check_attendence(self, data):
        table = []
        for row in data:
            if row.id == self.id:
                table.append([row.data, row.status])
        return table


    @classmethod
    def change_student_card(cls, person):
        os.system('clear')
        Ui.print_message("Chosen student: {} {}".format(person, person.card))
        Ui.print_message("What card you want to give:\n"
                               "1. GREEN\n"
                               "2. YELLOW\n"
                               "3. RED\n"
                               "4. None")
        chose_card = Ui.get_inputs([''], "")
        while True:
            if chose_card[0] == '1':
                person.card = "Green"
                break
            elif chose_card[0] == '2':
                person.card = "Yellow"
                print(person.card)
                break
            elif chose_card[0] == '3':
                person.card = "Red"
                break
            elif chose_card[0] == '4':
                person.card = "None"
                break
            else:
                Ui.print_message('Wrong input!')

    @classmethod
    def add_student_team(cls):
        Ui.print_message('''Assign each student to the following teams(type the number):
        (1) Fork in ear
        (2) Stepan
        (3) Rainbow unicorns
        (4) Jakkiedy
                    ''')


        is_valid = False
        while not is_valid:
            table = Ui.get_inputs(Student.student_list, '')
            is_need_break = False
            for value in table:
                if value not in ['1', '2', '3', '4']:
                    Ui.print_message('There is no such option, try again.')
                    is_need_break = True
                    break
            if is_need_break:
                continue
            is_valid = True
            i = 0
            while i <= len(table)-1:
                if table[i] == '1':
                    table[table.index('1')] = 'Fork in ear'
                elif table[i] == '2':
                    table[table.index('2')] = 'Stepan'
                elif table[i] == '3':
                    table[table.index('3')] = 'Rainbow unicorns'
                elif table[i] == '4':
                    table[table.index('4')] = 'Jakkiedy'
                Student.student_list[i].team = table[i]

                i += 1
    @classmethod
    def get_full_statistics_about_students(cls):

        pass
