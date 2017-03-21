from models.user import User
from main import db


class Manager(User):
    """
    Class manager representing manager.
    Reads data from database.
    """
    __tablename__ = 'manager'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    surname = db.Column(db.String, nullable=False)
    email = db.Column(db.String. nullable=False)
    password = db.Column(db.String, nullable=False)
    status = db.Column(db.String)

    def __init__(self, name, surname, email, password, status, card, team):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.status = 'manager'

    def __repr__(self):
        return '{} {} {} {} {} {} {} {}'.format(self.id, self.name, self.surname, self.email, self.password,
                                                self.status)
