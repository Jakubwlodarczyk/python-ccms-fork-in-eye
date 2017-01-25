from user import User


class Student(User):

    student_list = []

    def __init__(self, *args, **kwargs):
        super(Student, self).__init__(*args, **kwargs)

    @staticmethod
    def submit_an_assignment(self):
        pass

    @staticmethod
    def view_my_grades(self):
        pass
