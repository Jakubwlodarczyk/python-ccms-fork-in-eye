import sqlite3
from models.student import Student
from models.mentor import Mentor
from models.team import Team


class Model:
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
        conn.commit()
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
    def create_teams_list(cls):
        """
        Reads teams based on data from database.
        """
        conn = sqlite3.connect("database.db")
        c = conn.cursor()

        name_q = "SELECT ID, name FROM teams_list;"
        name_db = c.execute(name_q)
        conn.commit()
        teams_list = []

        for row in name_db:
            id = row[0]
            name = row[1]
            team = Team(id, name)
            teams_list.append(team)
        conn.close()
        return teams_list

    @classmethod
    def update_team_name(cls, old_name, new_name):
        """ Update team name in database """
        data = sqlite3.connect("database.db")
        cursor = data.cursor()
        cursor.execute("UPDATE teams_list SET name = '{}' WHERE name = '{}'".format(new_name, old_name))
        data.commit()
        data.close()

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
    def create_submission_list(cls):  # from database
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
    def add_team(cls, team_name):
        """ Adds new team to database """
        data = sqlite3.connect("database.db")
        cursor = data.cursor()
        cursor.execute("INSERT INTO teams_list (name) VALUES ('{}')".format(team_name))
        data.commit()
        data.close()

    @classmethod
    def remove_student_team(cls, student_id):
        """ Remove student from team"""
        data = sqlite3.connect("database.db")
        cursor = data.cursor()
        cursor.execute("UPDATE student SET team = '{}' WHERE ID = '{}'".format('none', student_id))
        data.commit()
        data.close()

    @classmethod
    def get_average(cls):
        """ Gets averages of all students """
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        data = cursor.execute("""SELECT student.ID, AVG(submission.grade)\
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
