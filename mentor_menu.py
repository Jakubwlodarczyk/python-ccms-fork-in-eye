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
                            'Add student to specific team']

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
                os.system('clear')               
                
                Ui.print_error_message('''Assign each student to the following teams(type the number): 
    (1) Fork in ear
    (2) Stepan
    (3) Rainbow unicorns
    (4) Jakkiedy                 
                ''')              

                
                is_valid = False
                while not is_valid:
                    table = Ui.get_inputs(Student.student_list, '')
                    is_need_break = False
                    for value in table:
                        if value not in ['1', '2', '3', '4']:
                            Ui.print_error_message('There is no such option, try again.')
                            is_need_break = True
                            break
                    if is_need_break:
                        continue
                    is_valid = True
                    i = 0
                    while i <= len(table)-1:
                        if table[i] == '1':
                            table[table.index('1')] = 'Fork in ear'                            
                        elif table[i] == '2':
                            table[table.index('2')] = 'Stepan'                            
                        elif table[i] == '3':
                            table[table.index('3')] = 'Rainbow unicorns'                            
                        elif table[i] == '4':
                            table[table.index('4')] = 'Jakkiedy'                            
                        Student.student_list[i].team = table[i]
                        
                        i += 1
                    

            elif chose_option[0] == '0':
                # save data to files, and exit
                Common.write_submission_to_file('Submissions.csv', Submission.submission_list)
                Common.write_students_to_file('Student.csv', Student.student_list)              
                Common.write_attendance_to_file('Attendance.csv', Attendance.attendances_list)
                Common.write_assignment_to_file('Assignments.csv', Assignments.assignments_list)                
                sys.exit()

            else:
                Ui.print_error_message('There is no such option.')
