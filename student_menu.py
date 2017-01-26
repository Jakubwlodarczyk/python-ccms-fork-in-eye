from ui import *
from Common import *
import sys
# from menu import *
from student import *
from submission import *
import os


class StudentMenu:

    @staticmethod
    def handle_menu():
        options = ['View grades', "Submit an assignment", 'View attandence', 'Exit']


        while True:
            Ui.print_menu("What you want to do?", options, "Log out")
            inputs = Ui.get_inputs(["Please enter a number: "], "")
            option = inputs[0]
            
            
            if option == '1':
               # Student.view_grades()       
                # for i in Submission.submission_list:
                #     print(i.grade)
                # # submission = Submission.submission_list
                os.system('clear')
                Student.view_grades()   



            elif option == '2':
                
                os.system('clear')
                Student.submit_assignment()
                



                
                
                
                
            
            elif option == '3':
                # fire a employee
                pass
            elif option == '4':
                # view mentors list
                pass
            elif option == '5':
                # edit employees data
                pass
            elif option == '6':
                # fire a employee
                pass
            elif option == '7':
                # fire a employee
                pass
            elif option == '0':
                #common.write_table_to_file('Mentors.csv')
                #common.write_table_to_file('Regular_employees.csv')
                sys.exit()
            else:
                Ui.print_error_message('There is no such option.')


