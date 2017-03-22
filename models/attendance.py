from main import db
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind=db)
session = Session()


class Attendance(db.Model):
    __tablename__ = 'attendance'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    date = db.Column(db.String)
    status = db.Column(db.Integer)
    student_id = db.Column(db.Integer)

    def __init__(self, date, status, student_id):
        self.date = date
        self.status = status
        self.student_id = student_id

