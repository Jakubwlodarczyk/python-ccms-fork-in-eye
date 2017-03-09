class User:
    '''
    Parent class for all users to inherit from.
    '''
    def __init__(self, id, name, surname, email, password, status):
        self.id = id
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.status = status
