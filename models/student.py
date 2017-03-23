from main import db
from sqlalchemy import and_, func
from sqlalchemy.orm import sessionmaker
from models.attendance import Attendance


Session = sessionmaker(bind=db)
session = Session()

from models.submission import *


class Student(db.Model):
    """
    Class representing student.
    Reads data from database.
    """
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    surname = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    status = db.Column(db.String)
    card = db.Column(db.String)
    team = db.Column(db.String)

    def __init__(self, name, surname, email, password, status='student', card=None, team=None):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.status = status
        self.card = card
        self.team = team

    def __repr__(self):
        return '{} {} {} {} {} {} {} {}'.format(self.id, self.name, self.surname, self.email, self.password,
                                                self.status, self.card, self.team)

    @staticmethod
    def add_student(name, surname, email):
        """ Create object of student class and add it to database"""
        password = name.lower()
        status = 'student'
        student = Student(name=name, surname=surname, email=email, password=password, status=status, team=None,
                          card=None)
        db.session.add(student)
        db.session.commit()

    @staticmethod
    def edit_student(student_id, name, surname, email):
        """ Edit object of student class and update it in database"""
        student = db.session.query(Student).get(student_id)
        student.name = name
        student.surname = surname
        student.email = email
        db.session.commit()

    @staticmethod
    def remove_student(student_id):
        """ Remove object of student class and update it in database"""
        student = db.session.query(Student).get(student_id)
        db.session.delete(student)
        db.session.commit()

    @staticmethod
    def edit_student_team_card(student_id, team, card):
        """ Edit student team, and card , and update it in database"""
        student = db.session.query(Student).filter_by(id=student_id).first()
        student.team = team
        student.card = card
        db.session.commit()

    @staticmethod
    def remove_student_team(student_id):
        """ Remove student from team, and update database """
        student = db.session.query(Student).filter_by(id=student_id).first()
        student.team = None
        db.session.commit()

    @staticmethod
    def get_all():
        """ Return a list of objects """
        return db.session.query(Student).all()

    @staticmethod
    def get_by_id(student_id):
        """ Return object of student found by ID"""
        return db.session.query(Student).get(student_id)

    @staticmethod
    def add_student_attendance(date, status, student_id):
        """ If attendance object exist (with same date and student ID) it update object status
            If object do not exist it creates new one
        """
        if status == 'Present':
            status = 100
        elif status == 'Late':
            status = 80
        else:
            status = 0
        att_obj = Attendance.get_by_date_id(date, student_id)
        if att_obj:
            att_obj.status = status
            db.session.commit()
        else:
            Attendance.add_attendance(date, status, student_id)

    @staticmethod
    def count_days():
        """ Count days of attendance """
        dates = []
        attendance = Attendance.get_all()
        for data in attendance:
            if data.date not in dates:
                dates.append(data.date)
        return len(dates)

    @classmethod
    def get_performance(cls, student_id, start_date, end_date):
        """ Gets performance of student between given dates. """

        results = db.session.query(Submission.send_date, Submission.name, Submission.grade).join\
            (Student, and_(Submission.student_id == Student.id)).filter\
            (Submission.send_date > start_date, Submission.send_date < end_date, Student.id == student_id).all()
        return results

    @staticmethod
    def get_average():
        """ Gets averages of all students """
        data = (db.session.query(Student.id, (func.round(func.avg(Submission.grade), 2)))
                .join(Submission, and_(Submission.student_id == Student.id))
                .group_by(Submission.student_id)).all()
        grades = {}
        for record in data:
            grades[record[0]] = record[1]
        return grades

        
    @staticmethod
    def show_alert():
        """ Show alert message """
        
        pass