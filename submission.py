from Common import *


class Submission:

    # submission_list = []

    def __init__(self):
        self.sub_list = []
        # def __init__(self, grade, student_id, assignment_name):
        # self.grade = grade
        # self.student_it = student_id
        # self. assignment_name = assignment_name

    def submission_list(self, filepath):
        # funkcja zwraca instancje obiektu
        submis_list = Common.get_table_from_file(filepath)
        return submis_list

    def make_a_submission(self):
        pass

    def grade_an_submission(self):
        pass
