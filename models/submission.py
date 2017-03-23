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
    send_date = db.Column(db.String, nullable=False)
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
        return "{} {} {} {} {}".format(self.send_date,
        self.grade, self.name, self.github_link, self.student_id)

    @staticmethod
    def add_submission(send_date, grade, name, github_link, student_id):
        submission = Submission(send_date=send_date, grade=grade, name=name,
                                github_link=github_link, student_id=student_id)
        db.session.add(submission)
        db.session.commit()

