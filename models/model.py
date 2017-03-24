from models.student import *
from models.mentor import *
from models.employee import *
from models.manager import *
from main import db
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind=db)
session = Session()


class Model:
    @staticmethod
    def find_user(username, password, status):
        """
        Args:
        username: str, data from form
        password: str, data from form
        status: str, data from form
        Checks if given username and password exists in database
        Returns: person with given username and password
        """

        if status == 'student':
            try:
                student = db.session.query(Student).filter_by(email=username, password=password).first()
                return student
            except:
                return None
        elif status == 'mentor':
            try:
                student = db.session.query(Mentor).filter_by(email=username, password=password).first()
                return student
            except:
                return None
        elif status == 'employee':
            try:
                student = db.session.query(Employee).filter_by(email=username, password=password).first()
                return student
            except:
                return None
        elif status == 'manager':
            try:
                student = db.session.query(Manager).filter_by(email=username, password=password).first()
                return student
            except:
                return None
