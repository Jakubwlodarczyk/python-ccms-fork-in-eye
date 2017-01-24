from ui import Ui


class Assignments:
    """

    """
    assignments_list = []

    def __init__(self, start_date, end_date, assignment_name):
        self.start_date = str(start_date)  # sample date "01.01.2017"
        self.end_date = str(end_date)
        self.assignment_name = str(assignment_name)  # sample name "OOP_SI_exercise"

    def view_assignment_list(self):
        pass

    @classmethod
    def add_an_assignment(cls, assignment_input):
        pass
