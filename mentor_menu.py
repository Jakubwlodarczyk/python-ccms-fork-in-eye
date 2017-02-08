from student import Student
from user import *
from submission import *
from attendance import *
from employee import Employee
import sys
import os


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
                            "Show students of specific group", "Give a card to student", 'Add student to specific group']

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

            elif chose_option[0] == '8':
                # show students of specific group
                stu_list = Student.student_list
                Ui.print_student_teams(stu_list)

            elif chose_option[0] == '9':
                 # give a card to students
                Ui.print_student_table(Student.student_list, "List of students")
                person = Student.choose_person_to_change_data(Student.student_list)
                if person:
                    Student.change_student_card(person)
            
            elif chose_option[0] == '10':
                os.system('clear')   
                Student.add_student_team()            
                
                
                    


            elif chose_option[0] == '0':
                # save data to files, and exit
                Common.write_submission_to_file('Submissions.csv', Submission.submission_list)
                Common.write_students_to_file('Student.csv', Student.student_list)              
                Common.write_attendance_to_file('Attendance.csv', Attendance.attendances_list)
                Common.write_assignment_to_file('Assignments.csv', Assignments.assignments_list)                
                sys.exit()

            else:
                Ui.print_message('There is no such option.')
