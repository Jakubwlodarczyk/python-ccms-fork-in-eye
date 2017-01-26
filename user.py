from ui import *
from Common import *
from assignments import *
from submission import *


class User:
    '''
    Parent class for all users to inherit from.
    '''
    all_users = []

    def __init__(self, name, surname, email, password, status, id):
        self.name = name
        self.surname = surname
        self.email = str(email)
        self.password = str(password)
        self.status = status
        self.id = id

        if name == '':
            raise ValueError('Name can\'t be empty.')
        if surname == '':
            raise ValueError('Surname can\'t be empty.')
        if email == '':
            raise ValueError('Email can\'t be empty.')
        if password == '':
            raise ValueError('Password can\'t be empty.')
        if status == '':
            raise ValueError('Status can\'t be empty.')
        if id == '':
            raise ValueError('ID can\'t be empty.')

    @classmethod
    def create_objects_list(cls, file_path):
        '''
        Arg: file_path.
        Creates list of person objects from csv file.
        '''
        object_list = []
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
        return object_list

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
        for people in cls.all_users:
            # person as single object
            for person in people:
                if person.email == email and person.password == password:
                    return person

    def edit_name(self, new_name):
        '''
        Allows to change person object's attribute.
        '''
        self.name = new_name
        Ui.print_error_message("\nName has been changed.\n")

    def edit_surname(self, new_surname):
        '''
        Allows to change person object's attribute.
        '''
        self.surname = new_surname
        Ui.print_error_message("\nSurname has been changed.\n")

    def edit_email(self, new_email):
        '''
        Allows to change person object's attribute.
        '''
        self.email = new_email
        Ui.print_error_message("\nEmail has been changed.\n")

    def edit_password(self, new_password):
        '''
        Allows to change person object's attribute.
        '''
        self.password = new_password
        Ui.print_error_message("\nPassword has been changed.\n")

    @classmethod
    def add_person(cls, object_list):
        '''
        Arg: object_list - list of objects (students, mentors etc.).
        Function allows to add new person object to a list of given type of objects.
        Returns updated list of objects.
        '''
        data = Ui.get_inputs(['Name: ', 'Surname: ', 'email: ', 'Password: ', 'Status: '], "Please provide informations:")
        id = '11111111'  # HAVE TO CHANGE IT TO RANDOMLY GENERATED

        new_person = cls(data[0], data[1], data[2], data[3], data[4], id)
        object_list.append(new_person)

    @classmethod
    def remove_person(cls, object_list):
        '''
        Arg: object_list - list of objects (student, mentors etc.).
        Allows to remove person object from list of given objects.
        Returns updated list of objects.
        '''
        to_remove = Ui.get_inputs(['-> '], "Enter ID of person you want to fire:")
        for person in object_list:
            if person.id == to_remove[0]:
                object_list.remove(person)
