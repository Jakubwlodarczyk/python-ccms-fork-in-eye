#from ui import Ui
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
            if sub.name == sub_to_grade[0] and sub.student_id == sub_to_grade[1]:
                found = True
                if found:
                    Ui.print_message("Chosen submission:\n{} {} {} {} {}\n".format(sub.send_date,
                                                                                   sub.name,
                                                                                   sub.grade,
                                                                                   sub.github_link,
                                                                                   sub.student_id))
                    sub_grade = Ui.get_inputs(['Grade: '], "Type the grade: ")
                    sub.grade = sub_grade[0]
                    Ui.print_message('Submission graded!')
        if not found:
            Ui.print_message('Wrong submission name or ID')

    @classmethod
    def submission_all(cls):
        """
        Creates abjects based on data from database.
        :param table_name : name of table
        """
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        name_q = "SELECT send_date, grade, name, github_link, student_id FROM submission;"
        name_db = c.execute(name_q)
        conn.commit()
        submission_list = []

        for row in name_db:
            send_date = row[0]
            grade = row[1]
            name = row[2]
            github_link = row[3]
            student_id = row[4]
            full_name = cls(send_date, grade, name, github_link, student_id)
            submission_list.append(full_name)

        conn.close()
        return submission_list

    def get_by_id(cls, id):
        """ Retrieves submission item with given id from database.
        Args:
            id(int): item id
        Returns:
            Submission: submission object with a given id
        """
        data = sqlite3.connect('database.db')
        cursor = data.cursor()
        data = cursor.execute("SELECT ID FROM submission WHERE ID='{}'".format(id))
        for row in data:
            ID = row[0]
            submission_id = cls(ID)
        data.close()
        return submission_id


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
            student_grades[key] = round((sum(val)/len(val)), 2)
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

        return average_grades