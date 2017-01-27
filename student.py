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

    @classmethod
    def view_grades(cls):

        # print(submission)

    #     self.attendance_list = []

    # def view_grades(self):
    #     pass

        # # must get the submissions list from csv, where are added students submissions

        submission_list = Submission.submission_list

        # self.submission_list = Submission.submission_list

        for sub in submission_list:
            print('Assignment name: {}, Grade: {}.'.format(sub.submission_name, sub.grade))

        # for submission in cls.submission_list:
        #     print('Assignment name: {}, Grade: {}.'.format(submission.submission_name, submission.grade))

    @classmethod
    def submit_assignment(cls):

        print('Choose the number from the following assignments: ')

        # for n, assignment in enumerate(Assignments.assignments_list):
        #     print(n+1, ', '.join(assignment))
        choose = int(input('Type the chosen number here: '))
        ass = Assignments.assignments_list

        assignment_list = []
        for i in ass:
            print(i.start_date)
            assignment_list.append([i.start_date, i.end_date, i.assignment_name, '0', 'git_trololo', 'id_4'])
        print(assignment_list)
        if choose <= len(assignment_list):

            chosen_one = assignment_list[choose-1]
            submission_obj = Submission(chosen_one[0], chosen_one[1], chosen_one[2],
                                chosen_one[3], chosen_one[4], chosen_one[5])


            print(submission_obj.id)

            Common.write_submission_to_file('Submissions.csv', submission_obj)
                # sub = Submission(start_date, end_date, name, 0, 'trololo', 11 )
                # print(sub.submission_name, sub.github_link)
            print('Your assignment was succesfully submitted')
        else:
            print('invalid value')

