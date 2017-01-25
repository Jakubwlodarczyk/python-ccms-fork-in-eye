from user import User
from submission import Submission

class Student(User):

    submission = Submission()

    def __init__(self, *args, **kwargs):
        super(Student, self).__init__(*args, **kwargs)
    
   
        # self.attendance = attendance
        # self.id = id
        # self.student_list = []


    def view_grades(self):
        
        # must get the submissions list from csv, where are added students submissions
        grades = self.submission.submission_list('Submissions.csv')
        return grades
    def submit_assignment(self, assignment):
        
        print('Assignment has been submitted')
        # go to assignments list, choose assignment to be submitted, and add to submissions.csv
        
   
student = Student('name', 'surname', 'email', 'password', 'status', 'id')

for i in student.view_grades():
    print(', '.join(i))
    


   


