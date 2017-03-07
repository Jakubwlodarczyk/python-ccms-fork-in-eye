import sqlite3
from models.student import Student
from models.mentor import Mentor


class Model:
    @classmethod
    def students_get_all(cls):
        """
        Creates abjects based on data from database.
        :return:
        """
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        query = "SELECT id, name, surname, email, password, status, card, team FROM student;"
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
    def mentors_get_all(cls):
        """
        Creates abjects based on data from database.
        :return: list of mentors
        """
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        query = "SELECT id, name, surname, email, password, status FROM staff where status='mentor';"
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
    def create_teams_list(cls):  # from database
        """
        Reads teams based on data from database.
        """
        conn = sqlite3.connect("database.db")
        c = conn.cursor()

        name_q = "SELECT name FROM teams_list;"
        name_db = c.execute(name_q)
        conn.commit()
        teams_list = []

        for row in name_db:
            name = row[0]
            teams_list.append(name)
        conn.close()
        return teams_list
