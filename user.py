class User:
    '''
    Parent class for all users to inherit from.
    '''

    def __init__(self, name, surname, email, password):
        self.name = name
        self.surname = surname
        self.email = str(email)
        self.password = str(password)

        if name == '':
            raise ValueError('Name must not be empty.')
        if surname == '':
            raise ValueError('Surname must not be empty.')
        if email == '':
            raise ValueError('Email must not be empty.')
        if password == '':
            raise ValueError('Password must not be empty.')
