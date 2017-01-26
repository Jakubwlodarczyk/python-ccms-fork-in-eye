from student import *
from user import *
from submission import *
import sys


class MentorMenu:
    """
    Handles navigation menu after logging as mentor.
    """
    @staticmethod
    def handle_menu():
        """
        It doesnt return anything, just handle menu for mentor
        """
        while True:
            title = 'Mentor menu'
            list_options = ['Check the list of students', 'Add an assignment',
                            'Grade an assignment submitted by students', 'Check attendance of students',
                            'Add a student to a class', 'Remove a student from class', "Edit student's data"]
            Ui.print_menu(title, list_options, 'Log out')
            chose_option = Ui.get_inputs(["Please enter a number: "], "")

            if chose_option[0] == '1':
                # print list of students
                Ui.print_staff_list(Student.student_list, "List of students")

            elif chose_option[0] == '2':
                # add an assignment
                Assignments.add_an_assignment()

            elif chose_option[0] == '3':
                # grade assignments submitted by students
                Submission.grade_an_submission()

            elif chose_option[0] == '4':
                # check attendance of students
                pass

            elif chose_option[0] == '5':
                # add a student to a class
                Student.add_person(Student.student_list)

            elif chose_option[0] == '6':
                # remove student from class
                Student.remove_person(Student.student_list)

            elif chose_option[0] == '7':
                title = 'Students:'
                Ui.print_staff_list(Employee.employees_list, title)
                person = Employee.choose_person_to_change_data(Employee.employees_list)
                Employee.data_to_change(person)

            elif chose_option[0] == '0':
                # common.write_table_to_file('Assignments.csv')
                # common.write_table_to_file('Attendance.csv')
                # common.write_table_to_file('Manager.csv')
                # common.write_table_to_file('Mentors.csv')
                # common.write_table_to_file('Regular_employees.csv')
                # common.write_table_to_file('Student.csv')
                # common.write_table_to_file('Submissions.csv')
                Common.write_attendance_to_file('Attendance.csv', Attendance.attendances_list)
                Common.write_assignment_to_file('Assignments.csv', Assignments.assignments_list)
                sys.exit()

            else:
                Ui.print_error_message('There is no such option.')
