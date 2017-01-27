from user import *

class Student(User):

    student_list = []

    def __init__(self, *args, **kwargs):
        super(Student, self).__init__(*args, **kwargs)
        self.status = 'student'
        # self.attendance = attendance
        # self.id = id
        # self.student_list = []
        self.attendance_list = []

    def view_grades(self):
        pass
        # # must get the submissions list from csv, where are added students submissions
        # grades = Submission.submission_list('Submissions.csv')
        # return grades

    def submit_assignment(self):
        pass
        # print('Assignment has been submitted')
        # go to assignments list, choose assignment to be submitted, and add to submissions.csv
