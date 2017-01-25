from Common import *


class Submission:

    submission_list = []

    def __init__(self, start_date, end_date, submission_name, grade, github_link, id):
        self.start_date = start_date
        self.end_date = end_date
        self.grade = grade
        self.id = id
        self.submission_name = submission_name
        self.github_link = github_link

    # def make_a_submission(self):
    #     pass
    #
    # def grade_an_submission(self):
    #     pass
