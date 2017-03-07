from models.employee import Employee


class Mentor(Employee):
    """
    Class: mentor
    parent class: Employee
    """

    mentors_list = []

    def __init__(self, id, name, surname, email, password, status ):
        Employee.__init__(self, id, name, surname, email, password, status)
        self.status = 'mentor'

    def __str__(self):
        return "{} {}".format(self.name, self.surname)
