from main import db
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=db)
session = Session()


class Mentor(db.Model):
    """ Class handle mentors objects, reads from database """
    __tablename__ = 'mentor'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    status = db.Column(db.String)

    def __init__(self, name, surname, email, password, status):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.status = status

    def __repr__(self):
        return '{} {} {} {} {} {}'.format(self.id, self.name, self.surname, self.email, self.password, self.status)

    @staticmethod
    def add_mentor(name, surname, email):
        """
        Adds new mentor to database.
        """
        password = name.lower()
        status = 'mentor'
        mentor = Mentor(name=name, surname=surname, email=email, password=password, status=status)
        db.session.add(mentor)
        db.session.commit()

    @staticmethod
    def edit_mentor(mentor_id, name, surname, email):
        """
        Edits mentors data.
        """
        mentor = db.session.query(Mentor).get(mentor_id)
        mentor.name = name
        mentor.surname = surname
        mentor.email = email
        db.session.commit()

    @staticmethod
    def remove_mentor(mentor_id):
        """
        Removes mentor from database.
        """
        mentor = db.session.query(Mentor).get(mentor_id)
        db.session.delete(mentor)
        db.session.commit()
