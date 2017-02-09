from ui import *
from Common import *
import sys
from employee import *
from student import *
from mentor import *
from manager import Manager


class ManagerMenu:
    '''
    Handles navigating the menu after logging in as Manager.
    '''
    @staticmethod
    def handle_menu():
        '''
        Allows to choose an action to perform.
        '''
        options = ["View regular employees list",
                   "Add an employee",
                   "Edit employees' data",
                   "Fire an employee",
                   "View mentors list",
                   'Show the full statistics about mentors',
                   "Add a mentor",
                   "Edit mentors' data",
                   "Fire a mentor",
                   "View students list",
                   "View students' grades",
                   'Show full statistics about students']
        while True:
            Ui.print_menu("\nWhat you want to do?", options, "Log out")
            inputs = Ui.get_inputs(["Please enter a number: "], "")
            option = inputs[0]
            if option == '1':
                ManagerMenu.show_regular_employees()
            elif option == '2':
                Employee.add_person(Employee.employees_list)
            elif option == '3':
                # change regular employee's data
                ManagerMenu.show_regular_employees()
                person = Employee.choose_person_to_change_data(Employee.employees_list)
                if person:
                    Employee.data_to_change(person)
            elif option == '4':
                ManagerMenu.show_regular_employees()
                Employee.remove_person(Employee.employees_list)
            elif option == '5':
                ManagerMenu.show_mentors()
            elif option == '6':
                #  Show full statistics about mentors
                ManagerMenu.show_mentors()
            elif option == '7':
                Mentor.add_person(Mentor.mentors_list)
            elif option == '8':
                # change mentor's data
                ManagerMenu.show_mentors()
                person = Mentor.choose_person_to_change_data(Mentor.mentors_list)
                if person:
                    Mentor.data_to_change(person)
            elif option == '9':
                # fire mentor
                ManagerMenu.show_mentors()
                Mentor.remove_person(Mentor.mentors_list)
            elif option == '10':
                # view student list
                ManagerMenu.show_students()
            elif option == '11':
                # view students grades
                data = Submission.get_students_average_grades(Submission.submission_list)
                average_grades = Submission.get_name_by_id(data, Student.student_list)
                Ui.print_student_average_grades(average_grades)
            elif option == '12':
                # Show full statistics about students
                data = Submission.get_students_average_grades(Submission.submission_list)
                average_grades = Submission.get_name_by_id(data, Student.student_list)
                table = Student.get_full_statistics_about_students(Student.student_list, average_grades)
                title_list = ['ID', 'Name', 'Surname', 'Email', 'Team', 'Average', 'Card']
                title = 'FULL STATISTICS ABOUT STUDENTS'
                Ui.print_table(table, title, title_list)
            elif option == '0':
                Common.write_staff_to_file('database.db', Mentor.mentors_list)
                Common.write_staff_to_file('database.db', Manager.manager_list)
                Common.write_staff_to_file('database.db', Employee.employees_list)
                sys.exit()
            else:
                Ui.print_error_message('There is no such option.')

    @staticmethod
    def show_regular_employees():
        title = 'Regular employees list:'
        title_list = ['ID', 'Name', 'Surname', 'Email', 'Status']
        table = Ui.create_person_table_to_print(Employee.employees_list)
        Ui.print_table(table, title, title_list)

    @staticmethod
    def show_mentors():
        title = 'Mentors list:'
        title_list = ['ID', 'Name', 'Surname', 'Email', 'Status']
        table = Ui.create_person_table_to_print(Mentor.mentors_list)
        Ui.print_table(table, title, title_list)

    @staticmethod
    def show_students():
        title = 'Student list:'
        title_list = ['ID', 'Name', 'Surname', 'Email', 'Status']
        table = Ui.create_person_table_to_print(Student.student_list)
        Ui.print_table(table, title, title_list)
