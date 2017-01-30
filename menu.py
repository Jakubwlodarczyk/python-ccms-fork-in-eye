import csv
import getpass
import sys
from user import *
from Common import *
from student import *
from employee import *
from mentor import *
from manager import *
from submission import *
#from assignments import *
#from attendance import *
from assignments import *
from attendance import *
from ui import *
from manager_menu import *
from mentor_menu import *
from student_menu import *
# from employee_menu import *
from employee_menu import *



class Menu:
    @staticmethod
    def loading_data():
        '''
        Creates objects from csv and then a list of all users to loop through for login and password validation.
        '''
        Employee.employees_list = Employee.create_objects_list('Regular_employees.csv')
        Mentor.mentors_list = Mentor.create_objects_list('Mentors.csv')
        Submission.submission_list = Submission.create_submission_list('Submissions.csv')
        Student.student_list = Student.create_objects_list('Student.csv')
        Manager.manager_list = Manager.create_objects_list('Manager.csv')
        User.all_users = [Employee.employees_list,
                          Mentor.mentors_list,
                          Student.student_list,
                          Manager.manager_list]
        
        Assignments.assignments_list = Assignments.create_assignments_list('Assignments.csv')
        Attendance.attendance_list = Attendance.create_attendance_list('Attendance.csv')

    @classmethod
    def log_in(cls):
        '''
        Handles logging in as user based on given email and password.
        Redirects to specific submenu.
        '''
        login = Ui.get_inputs(['Please enter your email: '], "")
        password = []
        passw = getpass.getpass('Enter pass: ')
        password.append(passw)
        user = User.user_password_check(login[0], password[0])

        if not user:
            Ui.print_error_message('Invalid login or password. Please try again. ')
        elif user:
            Ui.print_error_message('\nHello, ' + user.name + '!\n')
            if user.status == 'manager':
                ManagerMenu.handle_menu()
            elif user.status == 'employee':
                EmployeeMenu.handle_menu()
            elif user.status == 'mentor':
                MentorMenu.handle_menu()
            elif user.status == 'student':
                StudentMenu.handle_menu(user)
        return None

    @classmethod
    def choose_option(cls):
        '''
        Allows user to log in or exit program.
        '''
        inputs = Ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
            Menu.log_in()
        elif option == "0":
            sys.exit(0)
        else:
            Ui.print_error_message('There is no such option.')

    @classmethod
    def main_menu(cls):
        '''
        Handles redirecting to printing menu options.
        '''
        options = ["SIGN IN"]
        Ui.print_menu("\tMAIN MENU", options, "EXIT PROGRAM")

    @staticmethod
    def main():
        while True:
            Menu.loading_data()
            Menu.main_menu()
            try:
                Menu.choose_option()
            except KeyError:
                ui.print_error_message('Unknown error at main!')


if __name__ == '__main__':
    Menu.main()
