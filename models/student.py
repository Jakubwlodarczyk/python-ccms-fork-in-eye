from main import db
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind=db)
session = Session()


class Student(db.Model):
    """
    Class representing student.
    Reads data from database.
    """
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    surname = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    status = db.Column(db.String)
    card = db.Column(db.String)
    team = db.Column(db.String)

    def __init__(self, name, surname, email, password, status='student', card=None, team=None):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.status = status
        self.card = card
        self.team = team

    def __repr__(self):
        return '{} {} {} {} {} {} {} {}'.format(self.id, self.name, self.surname, self.email, self.password,
                                                self.status, self.card, self.team)

    @staticmethod
    def add_student(name, surname, email):
        password = name.lower()
        status = 'student'
        student = Student(name=name, surname=surname, email=email, password=password, status=status, team=None,
                          card=None)
        db.session.add(student)
        db.session.commit()

    @staticmethod
    def edit_student(student_id, name, surname, email):
        student = db.session.query(Student).get(student_id)
        student.name = name
        student.surname = surname
        student.email = email
        db.session.commit()

    @staticmethod
    def remove_student(student_id):
        student = db.session.query(Student).get(student_id)
        db.session.delete(student)
        db.session.commit()
        

    @staticmethod
    def add_attendance_to_student(attendances_obj_list):
        """
        Returns attendances of select students.
        :param table_name
        """
        for student in Student.student_list:
            for attendance in attendances_obj_list:
                if attendance.id == student.id:
                    student.attendance_list.append(attendance)


    def view_grades(self):
        '''
        Allows to view grades for all student's assignments.
        '''
        my_submiss = []
        for sub in Submission.submission_list:
            if sub.student_id == self.id:
                my_submiss.append(sub)
        return my_submiss


    def check_attendence(self, data):
        """
        change attendance of students
        """
        table = []
        for row in data:
            if row.id == self.id:
                table.append([row.data, row.status])
        return table

    @staticmethod
    def count_days():
        dates = []
        conn = sqlite3.connect("database.db")
        with conn:
            c = conn.cursor()
            days = c.execute("SELECT * FROM attendance;")

            for day in days.fetchall():
                if day[1] not in dates:
                    dates.append(day[1])
            conn.commit()

        return len(dates)

    @staticmethod
    def student_presence(attendance_list, all_students):

        for day in attendance_list:
            Student.counted_days += 1
            for student in all_students:
                if day.status == 80 and day.id == student.id:
                    student.late += 1

                if day.status == 100 and day.id == student.id:
                    student.present += 1

                if day.status == 0 and day.id == student.id:
                    student.absent += 1
        return all_students

    @staticmethod
    def current_score(all_students):
        for student in all_students:
            points = 0
            points += (student.present * 100)
            points += (student.late * 80)

            student.score = (points / Student.count_days())
