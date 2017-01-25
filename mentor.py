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

    @classmethod
    def create_objects_list(cls):
        mentors_list = []
        with open(file_path, "r") as f:
            for line in f:
                line = line.split(",")
                lenght = len(line) - 1
                line[lenght] = line[lenght][:-2]
                name = line[0]
                surname = line[1]
                email = line[2]
                password = line[3]
                status = line[4]
                id = line[5]
                full_name = name + "_" + surname
                full_name = cls(name, surname, email, password, status, id)
                object_list.append(full_name)
        return mentors_list

    @classmethod
    def create_assignments_list(cls):
        assignment_list = []
        with open(file_path, "r") as f:
            for line in f:
                line = line.split(",")
                length = len(line) - 1
                line[length] = line[length][:-2]
                start_date = line[0]
                end_date = line[1]
                assignment_name = line[2]
                full_assignment_name = cls(start_date, end_date, assignment_name)
                assignment_list.append(full_assignment_name)
        return assignment_list

    @classmethod
    def create_submission_list(cls):
        submission_list = []
        with open(file_path, "r") as f:
            for line in f:
                line = line.split(",")
                length = len(line) - 1
                line[length] = line[length][:-2]
                start_date = line[0]
                end_date = line[1]
                submission_name = line[2]
                grade = line[3]
                github_link = line[4]
                id = line[5]
                full_submission_name = cls(start_date, end_date, submission_name, grade, github_link, id)
                submission_list.append(full_submission_name)
        return submission_list

    @classmethod
    def user_password_check(cls, email, password):
        '''
        Args:
        email(login) from inputs.
        password from inputs.
        Checks if given user exists.
        Checks if password for given user is correct.
        '''
        # people as list of objects
        # all_users is list containing all the objects
        for people in cls.mentors_list:
            # person as single object
            for person in people:
                if person.email == email and person.password == password:
                    return person

    def edit_name(self, new_name):
        self.name = new_name
        Ui.print_error_message("\nName has been changed.\n")

    def edit_surname(self, new_surname):
        self.surname = new_surname
        Ui.print_error_message("\nSurname has been changed.\n")

    def edit_email(self, new_email):
        self.email = new_email
        Ui.print_error_message("\nSurname has been changed.\n")

    def edit_password(self, new_password):
        self.password = new_password
        Ui.print_error_message("\nPassword has been changed.\n")

    @classmethod
    def add_person(cls, mentors_list):
        data = Ui.get_inputs(['Name: ', 'Surname: ', 'email: ', 'Password: ', 'Status: '], "Please provide informations:")
        id = '11111111'
        new_person = User(data[0], data[1], data[2], data[3], data[4], id)
        mentors.append(new_person)

    @classmethod
    def remove_person(cls, mentors_list):
        to_remove = Ui.get_inputs(['-> '], "Enter ID of person you want to fire:")
        for person in mentors_list:
            if person.id == to_remove[0]:
                mentors_list.remove(person)

new = Mentor('ika', 'grabon', 'ika@ika', 'bla', 'mentor', '2222')
print(Mentor.name)
