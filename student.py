from user import User
from assignments import Assignments
from ui import Ui
from Common import Common
from submission import Submission
import sys
import os
import datetime
import sqlite3


class Student(User):

    student_list = []
    teams_list = []
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
    def create_teams_list(cls):  # from database
        """
        Reads teams based on data from database.
        :param table_name
        """
        conn = sqlite3.connect("database.db")
        c = conn.cursor()

        name_q = "SELECT name FROM teams_list;"
        name_db = c.execute(name_q)
        conn.commit()

        for row in name_db:
            name = row[0]
            Student.teams_list.append(name)
        conn.close()

    @staticmethod
    def add_team():
        os.system("clear")
        name = Ui.get_inputs(" ", 'Type a name of a new team: \n')
        Student.teams_list.append(name[0])
        wait = Ui.get_inputs(" ", '\nTeam has been added succesfully.\n')
        os.system("clear")

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
        return my_submiss

    def submit_assignment(self):
        """
        allow student to submit an assignment as a team or alone
        """
        students = Student.student_list
        Ui.print_message('Choose the number from the following assignments: \n')
        for n, assignment in enumerate(Assignments.assignments_list):
            Ui.print_message(str(n+1) + '. ' + str(assignment))
        choose = input('Type the chosen number here: ')
        assign = Assignments.assignments_list
        assignment_list = []
        choose_val = input('Type the submission link: ')
        if choose_val == '':
            Ui.print_message('Submission link is empty')
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
            Ui.print_message('''
            Choose the following option:\n
            (1) Submit assignment as a team
            (2) Submit assignment by myself
                        ''')
            submit_option = input('Type the number: ')
            if submit_option == '1':
                for student in students:
                    if student.team == self.team:
                        assignment_list = []
                        assignment_list.append([datetime.date.today(), '0', i.assignment_name, choose_val, student.id])
                        print(assignment_list)
                        submission_obj = Submission(chosen_one[0], chosen_one[1], chosen_one[2], chosen_one[3], student.id)
                        Submission.submission_list.append(submission_obj)
            elif submit_option == '2':
                submission_obj = Submission(chosen_one[0], chosen_one[1], chosen_one[2], chosen_one[3], chosen_one[4])
                Submission.submission_list.append(submission_obj)
            else:
                Ui.print_message('Invalid value')
            os.system('clear')
            Ui.print_message('Your assignment was succesfully submitted\n')
            return Submission.submission_list
        else:
            os.system('clear')
            Ui.print_message('Invalid number')

    def check_attendence(self, data):
        """
        change attendance of students
        """
        table = []
        for row in data:
            if row.id == self.id:
                table.append([row.data, row.status])
        return table

    @classmethod
    def change_student_card(cls, person):
        """
        change a student card
        :param person: chosen student to change a card
        """
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
    def add_student_to_team(cls):
        student_list = Student.student_list
        for student in student_list:
            print("""ID: {} \t {} {} {}\n""".format(student.id, student.name, student.surname, student.team))
        choosen_student = User.choose_person_to_change_data(student_list)
        print(choosen_student)
        teams = Student.teams_list
        for index, team in enumerate(teams):
            print(index, team)
        chosen = input('Choose team: ')
        if chosen in teams:
            choosen_student.team = chosen
            print('Chosen student: {} join to {}! Yeah.'.format(choosen_student, choosen_student.team))
        else:
            print('No match!')

    @classmethod
    def get_full_statistics_about_students(cls, student_list, average_grades):
        '''
        Returns table with all information about student.
        '''
        stats = []

        for student in student_list:
            record = [student.id, student.name,
                      student.surname, student.email,
                      student.team, 'no record', student.card]
            stats.append(record)
            for key in average_grades:
                if key == student.id:
                    record[-2] = (str(average_grades[key][2]))
        return stats

    @staticmethod
    def show_full_report_of_students_performance():
        """
        method asks for input to get specific date,
        and creates a list of students performance in specific period of time
        """
        os.system('clear')
        st_end_date = Ui.get_inputs(['Start date (yyyy-mm-dd): ', 'End date (yyyy-mm-dd): '], "Type the values")
        list_of_performance = []
        conn = sqlite3.connect("database.db")
        with conn:
            c = conn.cursor()
            db = c.execute("SELECT submission.send_date, submission.name, student.name, student.surname, submission.grade\
                         FROM submission\
                         INNER JOIN student\
                         ON submission.student_id=student.student_id\
                         WHERE submission.send_date BETWEEN (?) AND (?)\
                         ORDER BY student.surname ASC;", (st_end_date[0], st_end_date[1]))
            conn.commit()
            print(db)
        for row in db:
            list_of_performance.append(row)
        title_of_table = 'FULL REPORT OF STUDENTS PERFORMANCE:'
        top_of_table = ('SUB. SEND DATE', 'SUB. NAME', 'STUDENT NAME', 'SURNAME', 'GRADE')
        list_of_performance.insert(0, top_of_table)
        Ui.print_full_report_of_students_performance(list_of_performance, title_of_table)
