from employee import *
from user import *
from ui import *
from Common import *


class Mentor(Employee):
    def __init__(self, name, surname, email, password, status, id):
        #super().__init__() dafuk?
        self.name = name
        self.surname = surname
        self.email = str(email)
        self.password = str(password)
        self.status = status
        self.id = id

    def __str__(self):
        return "{} {} {}".format(self.name, self.surname, self.login)
