from ui import *
from Common import *
import sys
from employee import *
from student import *
from mentor import *


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
                   "View students' average grades",
                   'Show full statistics about students']
        while True:
            Ui.print_menu("\nWhat you want to do?", options, "Log out")
            inputs = Ui.get_inputs(["Please enter a number: "], "")
            option = inputs[0]
            if option == '1':
                # show regular employees
                title = 'Regular employees list:'
                Ui.print_table(Employee.employees_list, title)
            elif option == '2':
                # add regular employee
                Employee.add_person(Employee.employees_list)
            elif option == '3':
                # change regular employee's data
                title = 'Regular employees:'
                Ui.print_table(Employee.employees_list, title)
                person = Employee.choose_person_to_change_data(Employee.employees_list)
                if person:
                    Employee.data_to_change(person)
            elif option == '4':
                # fire a regular employee
                title = 'Regular employees list:'
                Ui.print_table(Employee.employees_list, title)
                Employee.remove_person(Employee.employees_list)
            elif option == '5':
                # show mentors
                title = 'Mentors list:'
                Ui.print_table(Mentor.mentors_list, title)
            elif option == '6':
                #  Show full statistics about mentors
                print('Show full statistics about mentors - in progress')
                #Manager.view_full_mentors_statistics()
            elif option == '7':
                # add mentor
                Mentor.add_person(Mentor.mentors_list)
            elif option == '8':
                # change mentor's data
                title = 'Mentors:'
                Ui.print_table(Mentor.mentors_list, title)
                person = Mentor.choose_person_to_change_data(Mentor.mentors_list)
                if person:
                    Mentor.data_to_change(person)
            elif option == '9':
                # fire mentor
                title = 'Mentors:'
                Ui.print_table(Mentor.mentors_list, title)
                Mentor.remove_person(Mentor.mentors_list)
            elif option == '10':
                # view student list
                title = 'Students list:'
                Ui.print_table(Student.student_list, title)
            elif option == '11':
                # view students average grade
                data = Submission.get_students_average_grades(Submission.submission_list)
                average_grades = Submission.get_name_by_id(data, Student.student_list)
                Ui.print_student_average_grades(average_grades)

            elif option == '12':
                 # Show full statistics about students
                 print('in progress too')
                 #Manager.view_full_students_statistics()
            elif option == '0':
                # Common.write_table_to_file('Mentors.csv', Mentor.mentors_list)
                # Common.write_table_to_file('Regular_employees.csv', Employee.employees_list)
                sys.exit()
            else:
                Ui.print_message('There is no such option.')
