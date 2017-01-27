
from user import *
from assignments import *
from ui import *
from Common import *
from submission import *
import sys
import os


class Student(User):

    student_list = []

    def __init__(self, *args, **kwargs):
        super(Student, self).__init__(*args, **kwargs)
        self.status = 'student'
        self.attendance_list = []
        self.submission_list = Submission.submission_list

    def __str__(self):
        return "{} {}".format(self.name, self.surname)

    @classmethod
    def view_grades(cls):
        '''
        Allows to view grades for all student's assignments.
        '''
        Ui.print_submissions(Submission.submission_list)

    @classmethod
    def submit_assignment(cls):
        '''
        Allows student to submit chosen assignment
        '''
        Ui.print_error_message('''\nSorry, this method is not avialable yet.\n\nOur team is working on it as you read this!\n\nStay tuned!\n\n''')
