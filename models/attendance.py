from main import db
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind=db)
session = Session()


class Attendance(db.Model):
    """ Class handle Attendance objects read from database"""
    __tablename__ = 'attendance'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    date = db.Column(db.String)
    status = db.Column(db.Integer)
    student_id = db.Column(db.Integer)

    def __init__(self, date, status, student_id):
        self.date = date
        self.status = status
        self.student_id = student_id

    def __repr__(self):
        return '{} {} {}'.format(self.date, self.status, self.student_id)

    @staticmethod
    def add_attendance(date, status, student_id):
        """ Create an attendance object and add to database """
        attendance = Attendance(date=date, status=status, student_id=student_id)
        db.session.add(attendance)
        db.session.commit()

    @staticmethod
    def get_all():
        """ Return a list of objects """
        return db.session.query(Attendance).all()

    @staticmethod
    def get_by_date_id(date, student_id):
        """ Return an object of attendance, found by ID """
        return db.session.query(Attendance).filter(Attendance.date == date, Attendance.student_id == student_id).first()
