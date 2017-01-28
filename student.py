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
        self.submission_list = Submission.submission_list


     
        
        
   
    # def view_grades(cls):
        
       

    #     cls.submission_list = Submission.submission_list
       
    #     # self.submission_list = Submission.submission_list
        
    #     for sub in submission_list: 
    #         print('Assignment name: {}, Grade: {}.'.format(sub.submission_name, sub.grade))
        
        # for submission in cls.submission_list:
        #     print('Assignment name: {}, Grade: {}.'.format(submission.submission_name, submission.grade))
        
    def __str__(self):
        return "{} {}".format(self.name, self.surname)


    @classmethod
    def view_grades(cls):
        '''
        Allows to view grades for all student's assignments.
        '''
        Ui.print_submissions(Submission.submission_list)


    
    def submit_assignment(self):


        print('Choose the number from the following assignments: ')

        for n, assignment in enumerate(Assignments.assignments_list):
            print(str(n+1) + '. ' + str(assignment))
        choose = input('Type the chosen number here: ')  # choose is a string
        ass = Assignments.assignments_list

        assignment_list = []
        
        for i in ass:
            assignment_list.append([i.start_date, i.end_date, i.assignment_name, '0', 'git_trololo', self.id])
       
        if int(choose) <= len(assignment_list) and choose.isnumeric():  #condition
            chosen_one = assignment_list[int(choose)-1]
            
            submission_obj = Submission(chosen_one[0], chosen_one[1], chosen_one[2], #object of new submission is created
                                chosen_one[3], chosen_one[4], chosen_one[5])
    
            Submission.submission_list.append(submission_obj)             
            print('Your assignment was succesfully submitted')
            return Submission.submission_list
        
        else:
            print('invalid value')


        # '''
        # Allows student to submit chosen assignment
        # '''
        # Ui.print_error_message('''\nSorry, this method is not avialable yet.\n\nOur team is working on it as you read this!\n\nStay tuned!\n\n''')


