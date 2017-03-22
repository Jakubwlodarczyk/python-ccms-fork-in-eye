from main import db
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind=db)
session = Session()


class Assignments(db.Model):
    """
    Class Assignments
    handle assignments objects (assignment list)
    """
    __tablename__ = 'assignments'
    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    start_date = db.Column(db.String, nullable=False)
    end_date = db.Column(db.String, nullable=False)
    assignment_name = db.Column(db.String, nullable=False)
    link = db.Column(db.String, nullable=False)

    def __init__(self, start_date, end_date, assignment_name, link):
        self.start_date = str(start_date)
        self.end_date = str(end_date)
        self.assignment_name = str(assignment_name)
        self.link = link

    def __repr__(self):
        return '{} {} {} {}'.format(self.start_date, self.end_date, self.assignment_name, self.link)

    @staticmethod
    def add_assignment(start_date, end_date, assignment_name, link):
        assignment = Assignments(start_date=start_date, end_date=end_date, assignment_name=assignment_name, link=link)
        db.session.add(assignment)
        db.session.commit()

    @staticmethod
    def get_all():
        """ Return a list of objects """
        return db.session.query(Assignments).all()
