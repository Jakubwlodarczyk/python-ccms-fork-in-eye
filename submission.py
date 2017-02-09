from ui import *
import sqlite3


class Submission:
    """
    class Submission
    handle submissions objects (submissions list)
    """

    submission_list = []

    def __init__(self, send_date, grade, name, github_link, student_id):
        self.send_date = send_date
        self.grade = grade
        self.student_id = student_id
        self.name = name
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
                    Ui.print_error_message("Chosen submission:\n{} {} {} {} {} {}\n".format(sub.send_date,
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
    def create_objects_list_from_database(cls, table_name):# from database
        """
        Creates abjects based on data from database.
        :param file_path:
        :return:
        """

        conn = sqlite3.connect("database.db")
        c = conn.cursor()

        name_q = "SELECT send_date, grade, name, github_link, student_id FROM submission;"
        name_db = c.execute(name_q)
        conn.commit()

        # submission_list = []
        for row in name_db:
            send_date = row[0]
            grade = row[1]
            name = row[2]
            github_link = row[3]
            student_id = row[4]

            full_name = cls(send_date, grade, name, github_link, student_id)
            Submission.submission_list.append(full_name)

        conn.close()

        # return Submission.submission_list

    @classmethod
    def get_students_average_grades(cls, submission_list):
        '''
        Returns a dictionary with students average grades.
        '''
        student_grades = {}
        for submission in submission_list:
            if submission.student_id not in student_grades:
                student_grades[submission.student_id] = [int(submission.grade)]
            else:
                student_grades[submission.student_id] += [int(submission.grade)]

        for key, val in student_grades.items():
            student_grades[key] = round((sum(val)/len(str(val))), 2)

        return student_grades

    @classmethod
    def get_name_by_id(cls, student_grades, student_list):
        '''
        Returns name of student based on given id.
        '''
        print(student_list)

        average_grades = {}
        for key in student_grades:
            for student in student_list:
                print(student.id)
                print(student.name)
                if key == student.id:
                    average_grades[key] = [student.name, student.surname, student_grades[key]]
        # RETURNS EMPTY DICTIONARY WHYYYYYYYYYY
        return average_grades
