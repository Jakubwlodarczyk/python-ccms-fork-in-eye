
from main import db
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind=db)
session = Session()

class Submission(db.Model):
    """
    class Submission
    Reads data from database.
    """

    __tablename__ = 'submission'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    start_date = db.Column(db.String, nullable=False) 
    grade = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String, nullable=False)
    github_link = db.Column(db.String, nullable=False)
    student_id = db.Column(db.String, nullable=False)

    submission_list = []

    def __init__(self, send_date, grade, name, github_link, student_id):
        self.send_date = send_date
        self.grade = grade
        self.student_id = student_id
        self.name = name
        self.github_link = github_link

    def __repr__(self):
        return "{} {} {} {} {}".format(self.start_date, 
        self.grade, self.name, self.github_link, self.student_id)


    @staticmethod
    def add_submission(send_date, grade, name, github_link, student_id):
        submission = Submission(send_date=send_date, grade=grade, name=name,
        github_link=github_link, student_id=student_id)
        submission_list = db.session.query(Submission)
        db.session.add(submission_list)
        db.session.commit()




    # @classmethod
    # def add_submission(cls, submission):

    #     data = sqlite3.connect("database.db")
    #     cursor = data.cursor()

        
    #     for sub in submission_list:
    #         if sub.name == submission.name:
    #             if sub.student_id == submission.student_id:
    #                 return False


        # cursor.execute("INSERT INTO submission (send_date, grade, name, github_link, student_id) VALUES (?, ?, ?, ?, ?)",
        # [submission.send_date, submission.grade, submission.name, submission.github_link, submission.student_id])
        # data.commit()
        # data.close()
        # return True


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


Submission.add_submission('fjkdsa', 'fdkaj', 'fkjdsja', 'fjka', 'l')