import getpass
import sys
import os
import time
from user import User
from student import Student
from employee import Employee
from mentor import Mentor
from manager import Manager
from submission import Submission
from assignments import Assignments
from attendance import Attendance
from ui import Ui
from manager_menu import ManagerMenu
from mentor_menu import MentorMenu
from student_menu import StudentMenu
from employee_menu import EmployeeMenu


class Menu:
    @staticmethod
    def loading_people():
        '''
        Creates objects from DB and then a list of all users to loop through for login and password validation.
        '''
        staff_tuple = User.create_objects_list_from_database('staff')
        Mentor.mentors_list = staff_tuple[0]
        Manager.manager_list = staff_tuple[1]
        Employee.employees_list = staff_tuple[2]
        Student.student_list = Student.create_objects_list_from_database('student')
        User.all_users = [Employee.employees_list,
                          Mentor.mentors_list,
                          Student.student_list,
                          Manager.manager_list]

    @staticmethod
    def loading_data():
        '''
        Creates objects from DB and then a list of all users to loop through for login and password validation.
        '''
        Assignments.assignments_list = Assignments.create_objects_list_from_database('assignements')
        Attendance.attendances_list = Attendance.create_objects_list_from_database('attendance')
        Submission.create_objects_list_from_database('submission')
        Student.add_attendance_to_student(Attendance.attendances_list) # add attendance obj to a specific student
        Student.create_teams_list()

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
            Ui.print_message('Invalid login or password. Please try again. ')
        elif user:
            os.system('clear')
            Ui.print_message('\nHello, ' + user.name + '!\n')
            time.sleep(2)
            if user.status == 'manager':
                Menu.loading_data()
                ManagerMenu.handle_menu(user)
            elif user.status == 'employee':
                Menu.loading_data()
                EmployeeMenu.handle_menu(user)
            elif user.status == 'mentor':
                Menu.loading_data()
                MentorMenu.handle_menu(user)
            elif user.status == 'student':
                Menu.loading_data()
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
            Ui.print_message('There is no such option.')

    @classmethod
    def main_menu(cls):
        '''
        Handles redirecting to printing menu options.
        '''
        options = ["SIGN IN"]
        Ui.print_menu("\tMAIN MENU", options, "EXIT PROGRAM")

    @staticmethod
    def main():
        os.system('clear')
        Menu.loading_people()
        while True:
            Menu.main_menu()
            try:
                Menu.choose_option()
            except KeyError:
                Ui.print_message('Unknown error at main!')


if __name__ == '__main__':
    Menu.main()
