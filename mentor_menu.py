from student import *
from user import *
from submission import *
from attendance import *
from employee import Employee
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
                            'Add a student to a class', 'Remove a student from class', "Edit student's data",
                            "Show students of specific group"]
            Ui.print_menu(title, list_options, 'Log out')
            chose_option = Ui.get_inputs(["Please enter a number: "], "")

            if chose_option[0] == '1':
                # print list of students
                Ui.print_student_table(Student.student_list, "List of students")

            elif chose_option[0] == '2':
                # add an assignment to assignment list
                Assignments.add_an_assignment()

            elif chose_option[0] == '3':
                # grade assignments submitted by students
                Submission.grade_an_submission()

            elif chose_option[0] == '4':
                # check attendance of students
                Attendance.attendance_mini_menu()

            elif chose_option[0] == '5':
                # add a student to a class
                Student.add_person(Student.student_list)

            elif chose_option[0] == '6':
                # remove student from class
                Ui.print_student_table(Student.student_list, "List of students")
                Student.remove_person(Student.student_list)

            elif chose_option[0] == '7':
                # edit students data
                Ui.print_student_table(Student.student_list, "List of students")
                person = Student.choose_person_to_change_data(Student.student_list)
                if person:
                    Employee.data_to_change(person)
                else:
                    pass

            elif chose_option[0] == '8':
                # show students of specific group
                Ui.print_student_teams()
                pass

            elif chose_option[0] == '0':
                # save data to files, and exit
                Common.write_submission_to_file('Submissions.csv', Submission.submission_list)
                Common.write_table_to_file('Student.csv', Student.student_list)
                Common.write_attendance_to_file('Attendance.csv', Attendance.attendances_list)
                Common.write_assignment_to_file('Assignments.csv', Assignments.assignments_list)
                sys.exit()

            else:
                Ui.print_error_message('There is no such option.')
