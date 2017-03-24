from main import db
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind=db)
session = Session()


from models.student import *


class Submission(db.Model):
    """
    class Submission
    Reads data from database.
    """
    __tablename__ = 'submission'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    send_date = db.Column(db.String, nullable=False)
    grade = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String, nullable=False)
    github_link = db.Column(db.String, nullable=False)
    student_id = db.Column(db.String, nullable=False)

    def __init__(self, send_date, grade, name, github_link, student_id):
        self.send_date = send_date
        self.grade = grade
        self.student_id = student_id
        self.name = name
        self.github_link = github_link

    def __repr__(self):
        return "{} {} {} {} {}".format(self.send_date, self.grade, self.name, self.github_link, self.student_id)

    @staticmethod
    def add_submission(send_date, grade, name, github_link, student_id):
        """ Create object of submission class and update it in database """
        submission = Submission(send_date=send_date, grade=grade, name=name,
                                github_link=github_link, student_id=student_id)
        list_of_subm = db.session.query(Submission).all()
        for subm in list_of_subm:
            if submission.name == subm.name:
                if submission.student_id == subm.student_id:
                    return False
        db.session.add(submission)
        db.session.commit()
        return True

    @staticmethod
    def submit_as_team(user_id):
        """ Return list of students with the same team as 'user_id' team """
        same_team = []
        student_searched = db.session.query(Student).get(user_id)  # student with needed id
        students = Student.get_all()  # list of all students
        for student in students:
            if student.team == student_searched.team:
                same_team.append(student)
        return same_team

    @staticmethod
    def get_all():
        """ Return a list of objects """
        return db.session.query(Submission).all()

    @staticmethod
    def upgrade_grade(my_grade, my_id, submission_name):
        """
        Upgrade grade in db
        """
        list_of_subm = db.session.query(Submission).all()
        for submission in list_of_subm:
            if submission.student_id == int(my_id):
                if submission.name == submission_name:
                    submission.grade = my_grade
                    db.session.commit()

    @classmethod
    def get_sub_distinct(cls):
        """
        get distinct list of submissions
        """
        return db.session.query(cls.name).distinct()
