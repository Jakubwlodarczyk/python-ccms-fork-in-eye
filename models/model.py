import sqlite3
from models.student import Student
from models.mentor import Mentor
from models.team import Team
from models.submission import Submission
from models.user import User



class Model:
    @classmethod
    def find_user(cls, username, password, status):
        """
        Args:
        username: str, data from form
        password: str, data from form
        status: str, data from form
        Checks if given username and password exists in database
        Returns: person with given username and password
        """
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        staff = ['mentor', 'manager', 'employee']
        if status in staff:
            query = """SELECT id, name, surname, email, password, status\
                        FROM staff WHERE status='{}' AND email='{}' AND password='{}';""".format(status, username, password)
            data = c.execute(query)
            try:
                for row in data:
                    id = row[0]
                    name = row[1]
                    surname = row[2]
                    email = row[3]
                    password = row[4]
                    status = row[5]
                    person = User(id, name, surname, email, password, status)
                return person
            except:
                return None
        else:
            query = """SELECT id, name, surname, email, password, status, card, team\
                        FROM student WHERE email='{}' AND password='{}';""".format(username, password)
            data = c.execute(query)
            try:
                for row in data:
                    id = row[0]
                    name = row[1]
                    surname = row[2]
                    email = row[3]
                    password = row[4]
                    status = row[5]
                    card = row[6]
                    team = row[7]
                    person = Student(id, name, surname, email, password, status, card, team)
                return person
            except:
                return None

    @classmethod
    def students_get_all(cls):
        """
        Creates abjects based on data from database.
        :return: list of students
        """
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        query = "SELECT ID, name, surname, email, password, status, card, team FROM student;"
        name_db = c.execute(query)
        students_list = []
        for row in name_db:
            id = row[0]
            name = row[1]
            surname = row[2]
            email = row[3]
            password = row[4]
            status = row[5]
            card = row[6]
            team = row[7]
            full_name = Student(id, name, surname, email, password, status, card, team)
            students_list.append(full_name)
        conn.close()
        return students_list

    @classmethod
    def get_student_by_id(cls, id):
        """ Retrieves student with given id from database.
        Args:
            id(int): person id
        Returns:
            person with a given id
        """
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        query = ("SELECT * FROM student WHERE ID={};".format(id))
        selected_by_id = c.execute(query)
        conn.commit()
        for atr in selected_by_id:
            id = atr[0]
            name = atr[1]
            surname = atr[2]
            email = atr[3]
            password = atr[4]
            status = atr[5]
            card = atr[6]
            team = atr[7]

            selected = Student(id, name, surname, email, password, status, card, team)
        return selected

    @classmethod
    def update_student_data(cls, student_id, new_name, new_surname, new_email):
        """ Updates student's data in the database.db """
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        query = ("UPDATE student SET name='{}', surname = '{}', email='{}' WHERE ID={}".format(new_name, new_surname,
                                                                                               new_email, student_id))
        update = c.execute(query)
        conn.commit()
        conn.close()

    @classmethod
    def delete_student(cls, student_id):
        """ Removes student from the database """
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        query = ("DELETE FROM student WHERE ID ={};".format(student_id))
        database = c.execute(query)
        conn.commit()
        conn.close()

    @classmethod
    def add_new_mentor(cls, name, surname, email):
        """ Adds new mentor to database """
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        query = ("INSERT INTO staff (name, surname, email, password, status ) values ('{}', '{}', '{}', 'password','mentor' )".format(name, surname, email))
        database = c.execute(query)
        conn.commit()
        conn.close()

    @classmethod
    def mentors_get_all(cls):
        """
        Creates abjects based on data from database.
        :return: list of mentors
        """
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        query = "SELECT ID, name, surname, email, password, status FROM staff where status='mentor';"
        name_db = c.execute(query)
        conn.commit()
        mentors_list = []
        for row in name_db:
            id = row[0]
            name = row[1]
            surname = row[2]
            email = row[3]
            password = row[4]
            status = row[5]
            full_name = Mentor(id, name, surname, email, password, status)
            mentors_list.append(full_name)
        conn.close()
        return mentors_list

    @classmethod
    def update_mentor_data(cls, mentor_id, new_name, new_surname, new_email):
        """ Updates mentor's data in the database.db """
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        query = ("UPDATE staff SET name='{}', surname = '{}', email='{}' WHERE status='mentor' AND ID={}".format(new_name, new_surname, new_email, mentor_id))
        update = c.execute(query)
        conn.commit()
        conn.close()

    @classmethod
    def get_mentor_by_id(cls, id):
        """ Retrieves mentor with given id from database.
        Args:
            id(int): person id
        Returns:
            person with a given id
        """
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        query = ("SELECT * FROM staff WHERE status='mentor' AND ID={} ;".format(id))
        selected_by_id = c.execute(query)
        conn.commit()
        for atr in selected_by_id:
            id = atr[0]
            name = atr[1]
            surname = atr[2]
            email = atr[3]
            password = atr[4]
            status = atr[5]

            selected = Mentor(id, name, surname, email, password, status)
        return selected

    @classmethod
    def delete_mentor(cls, mentor_id):
        """ Removes mentor from the database """
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        query = ("DELETE FROM staff WHERE status='mentor' AND ID ={};".format(mentor_id))
        database = c.execute(query)
        conn.commit()
        conn.close()


    @classmethod
    def save_new_student(cls, students):
        """
        save new student to the database.
        """
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        for student in students:
            status = 'student'
            params = [student[0], student[1], student[0], status, student[2]]
        c.execute("INSERT INTO student (name, surname, password, status, email) VALUES (?, ?, ?, ?, ?);", params)
        conn.commit()
        conn.close()

    @classmethod
    def submission_list_distinct(cls):  # from database
        """
        Reads teams based on data from database.
        """
        conn = sqlite3.connect("database.db")
        c = conn.cursor()

        name_q = "SELECT DISTINCT name FROM submission;"
        name_db = c.execute(name_q)
        conn.commit()
        sub_list = []

        for row in name_db:
            sub_list.append(row[0])
        conn.close()
        return sub_list



    @classmethod
    def create_submission_list(cls):  # from database
        """
        Reads teams based on data from database.
        """
        conn = sqlite3.connect("database.db")
        c = conn.cursor()

        name_q = "SELECT * FROM submission;"
        name_db = c.execute(name_q)

        conn.commit()
        sub_list = []

        for row in name_db:
            submission = Submission(row[1], row[2], row[3], row[4], row[5])
            sub_list.append(submission)
        conn.close()
        return sub_list


    @classmethod
    def remove_student_team(cls, student_id):
        """ Remove student from team"""
        data = sqlite3.connect("database.db")
        cursor = data.cursor()
        cursor.execute("UPDATE student SET team = '{}' WHERE ID = '{}'".format('none', student_id))
        data.commit()
        data.close()

    @classmethod
    def add_submission(cls, submission):




        data = sqlite3.connect("database.db")
        cursor = data.cursor()
        submission_list = cls.create_submission_list()
        print(submission.name)
        print(submission.student_id)
        for sub in submission_list:
            if sub.name == submission.name:
                if sub.student_id == submission.student_id:
                    return False

        cursor.execute("INSERT INTO submission (send_date, grade, name, github_link, student_id) VALUES (?, ?, ?, ?, ?)",
        [submission.send_date, submission.grade, submission.name, submission.github_link, submission.student_id])
        data.commit()
        data.close()
        return True


    @classmethod
    def get_average(cls):
        """ Gets averages of all students """
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        data = cursor.execute("""SELECT student.ID, ROUND(AVG(submission.grade), 2)\
                                 FROM student\
                                 JOIN submission\
                                 WHERE submission.student_id=student.ID\
                                 GROUP BY submission.student_id;""")
        grades = {}
        for record in data:
            grades[record[0]] = record[1]
        conn.close()
        return grades

    @classmethod
    def get_performance(cls, student_id, start, end):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        data = cursor.execute("""SELECT submission.send_date, submission.name, submission.grade\
                                 FROM submission\
                                 INNER JOIN student\
                                 ON submission.student_id=student.id\
                                 WHERE submission.send_date BETWEEN '{}' AND '{}' AND student.id =='{}'\
                                 ORDER BY student.surname ASC;""".format(start, end, student_id))
        performance = []
        for record in data:
            performance.append(list(record))

        conn.close()
        if performance:
            return performance

    @classmethod
    def update_students_team(cls, student_id, team, card):
        """ Updates student team, and card in database """
        data = sqlite3.connect("database.db")
        cursor = data.cursor()
        cursor.execute("UPDATE student SET team = '{}', card = '{}'WHERE ID = '{}'".format(team, card, student_id))
        data.commit()
        data.close()

    @classmethod
    def update_grades(cls, student_id, grade):
        """ Updates submissions names in database"""
        data = sqlite3.connect("database.db")
        cursor = data.cursor()
        cursor.execute("UPDATE submission SET grade = '{}' WHERE student_id = '{}'".format(grade, student_id))
        data.commit()
        data.close()


    @staticmethod
    def create_attendance(values, chosen_date, ids): # values = list, date = str (2017-03-15), ids = list
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        status_id_dict = {}
        correct_values_list = []
        for value in values:
            if value == "Present":
                correct_values_list.append(100)
            if value == "Late":
                correct_values_list.append(80)
            if value == "Absent":
                correct_values_list.append(0)

        dates = []
        dates_obj = c.execute('SELECT date FROM attendance;')
        for date in dates_obj:
            if date[0] not in dates:
                dates.append(date[0])

        for student_id, value in enumerate(correct_values_list):
            status_id_dict[ids[student_id]] = value

        if chosen_date in dates:
            for student_id, value in status_id_dict.items():
                c.execute('UPDATE attendance SET status = {} WHERE date = "{}" AND student_id = {};'.format(value, chosen_date, student_id))
        else:
            for student_id, value in status_id_dict.items():
                c.execute('INSERT INTO attendance (date, status, student_id) VALUES ("{}", {}, {});'.format(chosen_date,
                                                                                                            value,
                                                                                                            student_id))

        conn.commit()
        conn.close()
