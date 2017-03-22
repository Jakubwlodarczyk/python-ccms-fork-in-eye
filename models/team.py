from main import db
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind=db)
session = Session()


class Team(db.Model):
    __tablename__ = 'teams_list'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String, nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return "{}".format(self.name)

    @staticmethod
    def add_team(name):
        team = Team(name=name)
        db.session.add(team)
        db.session.commit()


    @staticmethod
    def remove_team(team_id, team_name):
        team = db.session.query(Team).get(team_id)
        students_list_in_deleting_team = db.session.query(Student).filter_by(team=team_name)
        for student in students_list_in_deleting_team:
            student.team = "none"
        db.session.delete(team)
        db.session.commit()


    @staticmethod
    def edit_team(old_name, new_name):
        team = db.session.query(Team).filter_by(name=old_name)
        team.name = new_name
        db.session.commit()
