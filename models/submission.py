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
