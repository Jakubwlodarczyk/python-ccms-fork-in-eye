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
    def add_attendance_to_student(attendances_obj_list):
        """
        Returns attendances of select students.
        :param table_name
        """
        for student in Student.student_list:
            for attendance in attendances_obj_list:
                if attendance.id == student.id:
                    student.attendance_list.append(attendance)

    def view_grades(self):
        '''
        Allows to view grades for all student's assignments.
        '''
        my_submiss = []
        for sub in Submission.submission_list:
            if sub.student_id == self.id:
                my_submiss.append(sub)
        return my_submiss

    def check_attendence(self, data):
        """
        change attendance of students
        """
        table = []
        for row in data:
            if row.id == self.id:
                table.append([row.data, row.status])
        return table

    @staticmethod
    def count_days():
        dates = []
        attendance = Attendance.get_all()
        for data in attendance:
            if data.date not in dates:
                dates.append(data.date)
        return len(dates)

    @staticmethod
    def student_presence(attendance_list, all_students):
        for day in attendance_list:
            Student.counted_days += 1
            for student in all_students:
                if day.status == 80 and day.id == student.id:
                    student.late += 1

                if day.status == 100 and day.id == student.id:
                    student.present += 1

                if day.status == 0 and day.id == student.id:
                    student.absent += 1
        return all_students

    @staticmethod
    def current_score(all_students):
        for student in all_students:
            points = 0
            points += (student.present * 100)
            points += (student.late * 80)

            student.score = (points / Student.count_days())


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