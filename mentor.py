from employee import *
from user import *


class Mentor(Employee):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return "{} {} {}".format(self.name, self.surname, self.login)
