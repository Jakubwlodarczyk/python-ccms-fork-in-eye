from student import Student
# from user import User
from submission import Submission
from assignments import Assignments
from attendance import Attendance
from employee import Employee
from Common import Common
import sys
import os
from manager_menu import ManagerMenu
from ui import Ui


class MentorMenu:
    
    """
    Handles navigation menu after logging as mentor.
    """

    @staticmethod

    def handle_menu(user):
        """
        It doesnt return anything, just handle menu for mentor
        """
        list_options = ['Check the list of students',
                        'Add an assignment',
                        'Grade an assignment submitted by students',
                        'Check attendance of students',
                        'Add a student to a class',
                        'Remove a student from class',
                        "Edit student's data",
                        'Show students of specific group',
                        'Give a card to student',
                        'Add student to specific group',
                        'Show full report of students performance between provided dates']
        while True:

            
            
            os.system('clear')
        

                       
            Ui.print_message(('\n...:::Logged in as {}:::...\n').format(user))
            Ui.print_menu("What you want to do?", list_options, 'Log out')

            chose_option = Ui.get_inputs(["Please enter a number: "], "")

            if chose_option[0] == '1':
                # print list of students
                MentorMenu.show_students_data()
                Ui.get_inputs([''], "Click enter to go back")

            elif chose_option[0] == '2':
                # add an assignment to assignment list
                Assignments.add_an_assignment()
                Common.write_assignment_to_db('database.db', Assignments.assignments_list)

            elif chose_option[0] == '3':
                # grade assignments submitted by students
                Submission.grade_an_submission()
                Common.write_submission_to_db('database.db', Submission.submission_list)

            elif chose_option[0] == '4':
                # check attendance of students
                Attendance.attendance_mini_menu()
                Common.write_attendance_to_db('database.db', Attendance.attendances_list)

            elif chose_option[0] == '5':
                # add a student to a class
                Student.add_person(Student.student_list)
                Common.write_student_to_db('database.db', Student.student_list)

            elif chose_option[0] == '6':
                # remove student from class
                ManagerMenu.show_students()
                Student.remove_person(Student.student_list)
                Common.write_student_to_db('database.db', Student.student_list)

            elif chose_option[0] == '7':
                # edit students data
                ManagerMenu.show_students()
                person = Student.choose_person_to_change_data(Student.student_list)
                if person:
                    Employee.data_to_change(person)
                    Common.write_student_to_db('database.db', Student.student_list)

            elif chose_option[0] == '8':
                # show students of specific group
                stu_list = Student.student_list
                Ui.print_student_teams(stu_list)
                Ui.get_inputs([''], "Click enter to go back")

            elif chose_option[0] == '9':
                # give a card to students
                MentorMenu.show_students_data()
                person = Student.choose_person_to_change_data(Student.student_list)
                if person:
                    Student.change_student_card(person)
                    Common.write_student_to_db('database.db', Student.student_list)

            elif chose_option[0] == '10':
                # add student to specific team
                os.system('clear')
                Student.add_student_to_team()
                Common.write_student_to_db('database.db', Student.student_list)

            elif chose_option[0] == '11':
                # Show full report of students performance between provided dates
                Student.show_full_report_of_students_performance()

            elif chose_option[0] == '12':
                # Add a new team
                Student.add_team()
                Common.write_team_to_db('database.db', Student.teams_list)

            elif chose_option[0] == '0':
                sys.exit()

            else:
                Ui.print_message('There is no such option.')

    @staticmethod
    def show_students_data():
        '''
        Prepares data to display in a formatted table.
        '''
        title_list = ['ID', 'Name', 'Surname', 'Email', 'Status', 'Team', 'Card']
        title = 'Student list:'
        table = Ui.create_student_table_to_print(Student.student_list)
        Ui.print_table(table, title, title_list)
