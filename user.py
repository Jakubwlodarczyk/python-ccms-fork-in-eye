class User:
    '''
    Parent class for all users to inherit from.
    '''

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

    def get_all_users(staff_object_list, mentors_object_list, students_object_list, manager_object_list):
        '''
        Creates a list of all users to loop through for login and password validation.
        '''
        all_users = [staff_object_list, mentor_object_list, students_list, manager_object_list]
        return all_users
