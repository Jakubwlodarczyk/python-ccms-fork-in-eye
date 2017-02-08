from user import *
from assignments import *
from ui import *
from Common import *
from submission import *


import sys
import os


class Student(User):

    student_list = []

    # submission_list = Submission.submission_list

    def __init__(self, *args, **kwargs):
        super(Student, self).__init__(*args, **kwargs)
        self.status = 'student'
        self.attendance_list = []
        # self.submission_list = Submission.submission_list     

    def __str__(self):
        return "{} {}".format(self.name, self.surname)

    def view_grades(self):
        '''
        Allows to view grades for all student's assignments.

        '''   
        my_submiss = []   
        for sub in Submission.submission_list:
            if sub.id == self.id:
                my_submiss.append(sub)
       
        Ui.print_submissions(my_submiss)  

    def submit_assignment(self):

        print('Choose the number from the following assignments: \n')
        for n, assignment in enumerate(Assignments.assignments_list):
            print(str(n+1) + '. ' + str(assignment))
        choose = input('Type the chosen number here: ')  
        assign = Assignments.assignments_list

        assignment_list = []
        choose_val = input('Type the submission link: ')
        for i in assign:
            assignment_list.append([i.start_date, i.end_date, i.assignment_name, '0', choose_val, self.id])

        if not choose.isnumeric():
            os.system('clear')
            print('\nChosen value must be a number')
            return 
       
        if int(choose) <= len(assignment_list):  # value condition
            chosen_one = assignment_list[int(choose)-1]
            for submiss in Submission.submission_list:
                if submiss.submission_name == chosen_one[2] and submiss.id == chosen_one[5]:  # condition for assignment being submitted
                    os.system('clear') 
                    print('Assignment is already submitted\n')
                    return
            
            submission_obj = Submission(chosen_one[0], chosen_one[1], chosen_one[2], # object of new submission is created
                                chosen_one[3], chosen_one[4], chosen_one[5])

            Submission.submission_list.append(submission_obj) 
            os.system('clear')            
            print('Your assignment was succesfully submitted\n')
            return Submission.submission_list
        
        else:
            os.system('clear')
            print('Invalid number')


    def check_attendence(self, data):
        table = []
        for row in data:
            if row.id == self.id:
                table.append([row.data, row.status])
        return table

    

        
        
