from main import db
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind=db)
session = Session()
from models.student import *

class Team(db.Model):
    """Student's teams"""
    __tablename__ = 'teams_list'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "{}".format(self.name)

    @staticmethod
    def add_team(name):
        """Add a new team"""
        team = Team(name=name)
        db.session.add(team)
        db.session.commit()


    @staticmethod
    def remove_team(team_id):
        """Remove a team"""
        team = db.session.query(Team).get(team_id)
        students_list_in_deleting_team = db.session.query(Student).filter_by(team=team.name)
        for student in students_list_in_deleting_team:
            student.team = None
        db.session.delete(team)
        db.session.commit()


    @staticmethod
    def edit_team(team_id, new_name):
        """Edit team's name"""
        team = db.session.query(Team).get(team_id)
        students_in_team = db.session.query(Student).filter_by(team=team.name)
        team.name = new_name
        for student in students_in_team:
            student.team = new_name
        db.session.commit()

    @staticmethod
    def get_all():
        """ Return a list of objects """
        return db.session.query(Team).all()

    @staticmethod
    def get_by_id(team_id):
        """Get a team by it's id"""
        return db.session.query(Team).get(team_id)
