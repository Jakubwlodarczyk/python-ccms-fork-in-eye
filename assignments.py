from ui import Ui


class Assignments:
    """

    """
    assignments_list = []

    def __init__(self, start_date, end_date, assignment_name):
        self.start_date = str(start_date)  # sample date "01.01.2017"
        self.end_date = str(end_date)  # sample date "01.01.2017"
        self.assignment_name = str(assignment_name)  # sample name "OOP_SI_exercise"

    def __str__(self):
        return '{} {} {}'.format(self.start_date, self.end_date, self.assignment_name)

    def view_assignment_list(self):
        pass

    @classmethod
    def add_an_assignment(cls, assignment_input):
        pass

    @classmethod
    def create_assignments_list(cls, file_path):
        assignments_list = []
        with open(file_path, "r") as f:
            for line in f:
                line = line.split(",")
                length = len(line) - 1
                line[length] = line[length][:-2]
                start_date = line[0]
                end_date = line[1]
                assignment_name = line[2]
                full_assignment_name = (start_date, end_date, assignment_name)
                assignments_list.append(full_assignment_name)
        return assignments_list
