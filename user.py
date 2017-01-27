from ui import *
from Common import *
from assignments import *
from submission import *
import time


class User:
    '''
    Parent class for all users to inherit from.
    '''
    all_users = []

    def __init__(self, name, surname, email, password, status, id):
        '''
        Initializing an object with data validation.
        '''
        try:
            self.name = name
            if not self.name:
                raise ValueError
        except ValueError:
            Ui.print_error_message("Name can't be empty")

        try:
            self.surname = surname
            if not self.surname:
                raise ValueError
        except ValueError:
            Ui.print_error_message("Surname can't be empty")

        try:
            self.email = email
            if not self.email:
                raise ValueError
            if '@' not in self.email or '.' not in self.email:
                raise KeyError
        except KeyError:
            Ui.print_error_message('Please use proper email format')
        except ValueError:
            Ui.print_error_message("Email can't be empty")

        try:
            self.password = str(password)
            if not self.password:
                raise ValueError
        except ValueError:
            Ui.print_error_message("Password can't be empty")

        self.status = status  # status is overwritten by each child class
        self.id = id  # id is randomly generated when adding a new person

    @classmethod
    def create_objects_list(cls, file_path):
        '''
        Arg: file_path.
        Creates list of person objects from csv file.
        '''
        object_list = []
        with open(file_path, "r") as f:
            my_lines = f.readlines()
            for index, line in enumerate(my_lines):
                line = line.split(",")
                length = len(line) - 1
                if index + 1 == len(my_lines):
                    pass
                else:
                    line[length] = line[length][:-1]
                name = line[0]
                surname = line[1]
                email = line[2]
                password = line[3]
                status = line[4]
                id = line[5]
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

    @classmethod
    def choose_person_to_change_data(cls, object_list):
        '''
        Handles choosing person to change his or her data.
        '''
        choosing = True
        while choosing:
            option = Ui.get_inputs(['Enter person ID or 0 to go back: '], "Whose data you want to change?")
            for person in object_list:
                if option[0] == person.id:
                    return person
            Ui.print_error_message('No id match.')
            if option[0] == '0':
                choosing = False

    @classmethod
    def data_to_change(cls, person):
        '''
        Handles choosing which data to change.
        '''
        choosing = True
        while choosing:
            Ui.print_data_list('Data list:')
            choice = Ui.get_inputs(['Enter a number: '], 'Which data you want to edit?')
            if choice[0] == '1':
                return cls.edit_name(person)
            elif choice[0] == '2':
                return cls.edit_surname(person)
            elif choice[0] == '3':
                return cls.edit_email(person)
            else:
                Ui.print_error_message('There is no such option.')
                time.sleep(3)

    @classmethod
    def edit_name(cls, person):
        '''
        Allows to change person object's attribute.
        '''
        new_name = Ui.get_inputs(['Enter new name: '], " ")
        person.name = new_name[0]
        Ui.print_error_message("\nName has been changed.\n")

    @classmethod
    def edit_surname(cls, person):
        '''
        Allows to change person object's attribute.
        '''
        new_surname = Ui.get_inputs(['Enter new surname: '], " ")
        person.surname = new_surname[0]
        Ui.print_error_message("\nSurname has been changed.\n")

    @classmethod
    def edit_email(cls, person):
        '''
        Allows to change person object's attribute.
        '''
        new_email = Ui.get_inputs(['Enter new email: '], " ")
        person.email = new_email[0]
        Ui.print_error_message("\nEmail has been changed.\n")

    @classmethod
    def edit_password(cls, person):
        '''
        Allows to change person object's attribute.
        '''
        choosing = True
        while choosing:
            new_password = Ui.get_inputs(['Enter new password: '], " ")
            confirm_password = Ui.get_inputs(['Enter password again: '], " ")

            if new_password[0] == confirm_password[0]:
                person.email = new_password[0]
                Ui.print_error_message("\nPassword has been changed.\n")
            else:
                Ui.print_error_message("\nEntered passwords are not identical.\n")

    @classmethod
    def add_person(cls, object_list):
        '''
        Arg: object_list - list of objects (students, mentors etc.).
        Function allows to add new person object to a list of given type of objects.
        Returns updated list of objects.
        '''
        data = Ui.get_inputs(['Name: ', 'Surname: ',
                             'email: ', 'Password: ', 'Status: '],
                             "Please provide informations:")
        id = Common.generate_random_id(object_list)
        new_person = cls(data[0], data[1], data[2], data[3], data[4], id)
        object_list.append(new_person)

        return object_list

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
        return object_list
