from student import *
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
                Ui.print_table(Student.student_list, "List of students")
                Student.remove_person(Student.student_list)

            elif chose_option[0] == '7':
                # edit students data
                Ui.print_table(Student.student_list, "List of students")
                person = Student.choose_person_to_change_data(Student.student_list)
                if person:
                    Employee.data_to_change(person)
                else:
                    pass

            elif chose_option[0] == '8':
                os.system('clear')               
                
                Ui.print_error_message('''Assign each student to the following teams(type the number): 
    (1) Fork in ear
    (2) Stepan
    (3) Rainbow unicorns
    (4) Jakkiedy                 
                ''')              
                # chosen = Ui.get_inputs(Student.student_list, '')            
                # [1, 1, 1, 1]

                for student in Student.student_list:
                    choice = input('Assign student {} to the team (type the number):'.format(str(student)))
                    if choice == '1':
                        student.team = 'Fork in ear'                        
                    elif choice == '2':
                        student.team  = 'Stepan'                        
                    elif choice == '3':
                        student.team  = 'Rainbow unicorns'                        
                    elif choice == '4':
                        student.team  = 'Jakkiedy'
                    else:
                        Ui.print_error_message('There is no such option, try again.')
                        break
                       
                
                # while True:
                #     i = 0
                # # for chose in chosen:
                #     # if i in ['1', '2', '3', '4']:
                #     if chosen[i] == '1':
                #         chosen[chosen.index('1')] = 'Fork in ear'
                #         break
                #     elif chosen[i] == '2':
                #         chosen[chosen.index('2')] = 'Stepan'
                #         break
                #     elif chosen[i] == '3':
                #         chosen[chosen.index('3')] = 'Rainbow unicorns'
                #         break
                #     elif chosen[i] == '4':
                #         chosen[chosen.index('4')] = 'Jakkiedy'
                #         break
                #     else:
                #         Ui.print_error_message('There is no such option, try again.')
                #         break

                    # for chose in chosen:
                    #     if chose in ['1', '2', '3', '4']:
                #     i += 1
                # x = 0  
                # while x <= len(Student.student_list)-1:   
                #     Student.student_list[x].team = chosen[x]                    
                #     x += 1
                        # else:
                        #                          
                   
                
                
            


                
                

            elif chose_option[0] == '0':
                # save data to files, and exit
                Common.write_submission_to_file('Submissions.csv', Submission.submission_list)
                Common.write_students_to_file('Student.csv', Student.student_list)
              
                Common.write_attendance_to_file('Attendance.csv', Attendance.attendances_list)
                Common.write_assignment_to_file('Assignments.csv', Assignments.assignments_list)
                
                sys.exit()

            else:
                Ui.print_error_message('There is no such option.')
