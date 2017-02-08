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
        not_valid = True

        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
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
                if line[5][-1] == '\n':
                    line[5] = line[5][:-1]
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
    def create_students_list(cls, file_path):
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
                if line[5][-1] == '\n':
                    line[5] = line[5][:-1]
                name = line[0]
                surname = line[1]
                email = line[2]
                password = line[3]
                status = line[4]
                id = line[5]
                team = line[6]
                card = line[7]
                full_name = cls(name, surname, email, password, status, id, team, card)
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
            option = Ui.get_inputs(["Enter person ID or 'q' to go back: "], "Whose data you want to change?")
            if option[0] == 'q':
                choosing = False
            else:
                Ui.print_error_message('No id match.')
            for person in object_list:
                if option[0] == person.id:
                    return person


    @classmethod
    def data_to_change(cls, person):
        '''
        Handles choosing which data to change.
        '''
        choosing = True
        while choosing:
            Ui.print_data_list('Data list: ')
            choice = Ui.get_inputs(["Enter a number or 'q' to go back: "], 'Which data do you want to edit?')
            if choice[0] == '1':
                return cls.edit_name(person)
            elif choice[0] == '2':
                return cls.edit_surname(person)
            elif choice[0] == '3':
                return cls.edit_email(person)
            elif choice[0] == 'q':
                choosing = False
            else:
                Ui.print_error_message('There is no such option.')
                time.sleep(3)

    @classmethod
    def edit_name(cls, person):
        '''
        Allows to change person object's attribute.
        '''
        new_name = Ui.get_inputs(['Enter new name: '], " ")
        if not new_name[0]:
            Ui.print_error_message("\nName cannot be empty.\n")
        else:
            person.name = new_name[0]
            Ui.print_error_message("\nName has been changed.\n")

    @classmethod
    def edit_surname(cls, person):
        '''
        Allows to change person object's attribute.
        '''
        new_surname = Ui.get_inputs(['Enter new surname: '], " ")
        if not new_surname[0]:
            Ui.print_error_message("\nSurname cannot be empty.\n")
        else:
            person.surname = new_surname[0]
            Ui.print_error_message("\nSurname has been changed.\n")

    @classmethod
    def edit_email(cls, person):
        '''
        Allows to change person object's attribute.
        '''
        new_email = Ui.get_inputs(['Enter new email: '], " ")
        if not nem_email[0]:
            Ui.print_error_message('email cannot be empty.')
        else:
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
        if data[0] == '' or data[1] == '' or data[2] =='' or data[3] == '':
            Ui.print_error_message("\nValue can't be empty")
        elif '@' and '.' not in data[2]:
            Ui.print_error_message("Enter proper email format")
        else:
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
                Ui.print_error_message("Person removed")
        return object_list
