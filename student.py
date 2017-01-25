from user import User


class Student(User):
    def __init__(self, attendance, id)
     User.__init__(self, name, surname, email, password)
        self.attendance = attendance
        self.id = id

    def submit an assignment(self, assignment):
        pass
        print('Assignment has been submitted')

    def view my grades(self, grades):
        pass


    # zmiana nazwy z submit assighnent na sent submission
    # ta metoda musi otworzyc plik csv submissions ale
    # przy otwieraniu nie usuwac wszystkiego, tylko dopisywac
    # pozniej zapisac w tym pliku csv to, co wymaga submission csv

    