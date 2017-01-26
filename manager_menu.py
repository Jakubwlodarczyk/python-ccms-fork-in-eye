from Common import *
import sys


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
                   "Add a mentor",
                   "Edit mentors' data",
                   "Fire a mentor",
                   "View students list"]
        while True:
            Ui.print_menu("What you want to do?", options, "Log out")
            inputs = Ui.get_inputs(["Please enter a number: "], "")
            option = inputs[0]
            if option == '1':
                # show regular employees
                title = 'Regular employees list:'
                Ui.print_staff_list(Employee.employees_list, title)
            elif option == '2':
                # add regular employee
                Employee.add_person(Employee.employees_list)
            elif option == '3':
                # edit employees data
                pass
            elif option == '4':
                # fire a regular employee
                Employee.remove_person(Employee.employees_list)
            elif option == '5':
                # show mentors
                title = 'Mentors list:'
                Ui.print_staff_list(Mentor.mentors_list, title)
            elif option == '6':
                # add mentor
                Mentor.add_person(Mentor.mentors_list)
            elif option == '7':
                # edit mentor's data
                pass
            elif option == '8':
                # fire mentor
                Mentor.remove_person(Mentor.mentors_list)
            elif option == '9':
                # view student list
                title = 'Students list:'
                Ui.print_staff_list(Student.student_list, title)
            elif option == '0':
                #common.write_table_to_file('Mentors.csv')
                #common.write_table_to_file('Regular_employees.csv')
                sys.exit()
            else:
                Ui.print_error_message('There is no such option.')
