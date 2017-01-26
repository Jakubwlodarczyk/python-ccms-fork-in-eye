from ui import *


class Submission:

    submission_list = []

    def __init__(self, start_date, end_date, submission_name, grade, github_link, id):
        self.start_date = start_date
        self.end_date = end_date
        self.grade = grade
        self.id = id
        self.submission_name = submission_name
        self.github_link = github_link

    @classmethod
    def grade_an_submission(cls):

        Ui.print_submissions_list(Submission.submission_list, "Submission list:")
        sub_to_grade = Ui.get_inputs(['Submission name: ', 'ID: '],
                                     'Type submission name, and student ID which you want to grade: ')

        found = False
        for sub in Submission.submission_list:
            if sub.submission_name == sub_to_grade[0] and sub.id == sub_to_grade[1]:
                found = True
                if found:
                    Ui.print_error_message("Chosen submission:\n{} {} {} {} {} {}\n".format(sub.start_date,
                                                                                            sub.end_date,
                                                                                            sub.submission_name,
                                                                                            sub.grade,
                                                                                            sub.github_link,
                                                                                            sub.id))
                    sub_grade = Ui.get_inputs(['Grade: '], "Type the grade: ")
                    sub.grade = sub_grade[0]
                    Ui.print_error_message('Submission graded!')
        if not found:
            Ui.print_error_message('Wrong submission name or ID')

    @classmethod
    def create_submission_list(cls, file_path):
        submission_list = []
        with open(file_path, "r") as f:
            my_lines = f.readlines()
            for index, line in enumerate(my_lines):
                line = line.split(",")
                length = len(line) - 1
                if index + 1 == len(my_lines):
                    pass
                else:
                    line[length] = line[length][:-1]
                start_date = line[0]
                end_date = line[1]
                submission_name = line[2]
                grade = line[3]
                github_link = line[4]
                id = line[5]
                full_submission_name = cls(start_date, end_date, submission_name, grade, github_link, id)
                submission_list.append(full_submission_name)
        return submission_list


