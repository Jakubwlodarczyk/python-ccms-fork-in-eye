from ui import *


class Submission:
    """
    class Submission
    handle submissions objects (submissions list)
    """

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
        """
        method change the argument (grade) of object from submissions list
        """
        Ui.print_submissions_list(Submission.submission_list, "Submission list:")
        sub_to_grade = Ui.get_inputs(['Submission name: ', 'ID: '],
                                     'Type submission name, and student ID which you want to grade: \n')

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
        """
        reads the file with data, and creates the list of objects
        :param file_path: the path to file
        :return: (list) list of objects of submissions
        """
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
                if line[5][-1] == '\n':
                    line[5] = line[5][:-1]
                start_date = line[0]
                end_date = line[1]
                submission_name = line[2]
                grade = line[3]
                github_link = line[4]
                id = line[5]
                full_submission_name = cls(start_date, end_date, submission_name, grade, github_link, id)
                submission_list.append(full_submission_name)
        return submission_list

    @classmethod
    def get_students_average_grades(cls, submission_list):
        '''
        Returns a dictionary with students average grades.
        '''

        student_grades = {}
        for submission in submission_list:
            if submission.id not in student_grades:
                student_grades[submission.id] = [int(submission.grade)]
            else:
                student_grades[submission.id] += [int(submission.grade)]

        for key, val in student_grades.items():
            student_grades[key] = (sum(val)/(len(val)))

        return student_grades


    @classmethod
    def get_name_by_id(cls, student_grades, student_list):
        '''
        Returns name of student based on given id.
        '''
        average_grades = {}
        for key in student_grades:
            for student in student_list:
                if key == student.id:
                    average_grades[key] = [student.name, student.surname, student_grades[key]]
                    # print("{} {} {}".format(key, student.name + " " + student.surname, ))
        return average_grades



        # id_and_grades = []
        # for key, value in student_grades.items():
