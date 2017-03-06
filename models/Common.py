import random
import string
from ui import *
import sqlite3


class Common:

    @classmethod
    def write_staff_to_file(cls, file_name, obj_list):  # for staff
        """
        Writes object list into a DB file.

        Args:
            file_name (str): name of file to write to
            table: list of lists to write to a file

        Returns:
            None
        """
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        for obj in obj_list:
            if obj.status == "mentor":
                query = "DELETE FROM `staff` WHERE `status` = 'mentor';"
                c.execute(query)
            elif obj.status == "employee":
                query = "DELETE FROM `staff` WHERE `status` = 'employee';"
                c.execute(query)
            elif obj.status == "manager":
                query = "DELETE FROM `staff` WHERE `status` = 'manager';"
                c.execute(query)

        for index, obj in enumerate(obj_list):
            params = [obj.name, obj.surname, obj.email, obj.password, obj.status, obj.id]
            c.execute("INSERT INTO staff (name, surname, email, password, status, staff_id) VALUES (?, ?, ?, ?, ?, ?)", params)
            conn.commit()

        conn.close()

    @classmethod
    def write_student_to_db(cls, file_name, obj_list):
        """
        Writes object list into a DB file.

        Args:
            obj_list: list students objects
            file_name (str): name of file to write to
        Returns:
            None
        """
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        query = "DELETE FROM `student`;"
        c.execute(query)

        for obj in obj_list:
            params = [obj.name, obj.surname, obj.email, obj.password, obj.status, obj.card, obj.team, obj.id]
            c.execute("INSERT INTO student (name, surname, email, password, status, card, team, student_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", params)
            conn.commit()

        conn.close()

    @classmethod
    def write_assignment_to_db(cls, file_name, obj_list):
        """
        Writes object list into a DB file.

        Args:
            obj_list: list of assignment objects
            file_name (str): name of file to write to
            table: list of lists to write to a file
        Returns:
            None
        """

        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        query = "DELETE FROM `assignements`;"
        c.execute(query)

        for obj in obj_list:
            params = [obj.start_date, obj.end_date, obj.assignment_name]
            c.execute("INSERT INTO assignements (start_date, end_date, name, link) VALUES (?, ?, ?)", params)
            conn.commit()

        conn.close()

    @classmethod
    def write_attendance_to_db(cls, file_name, obj_list):
        """
        Writes object list into a DB file.

        Args:
            file_name (str): name of file to write to
            table: list of lists to write to a file

        Returns:
            None
        """
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        query = "DELETE FROM `attendance`;"
        c.execute(query)

        for obj in obj_list:
            params = [obj.data, obj.status, obj.id]
            c.execute("INSERT INTO attendance (date, status, student_id) VALUES (?, ?, ?)", params)
            conn.commit()

        conn.close()

    @classmethod
    def write_submission_to_db(cls, file_name, obj_list):
        """
        Writes object list into a DB file.

        Args:
            file_name (str): name of file to write to
            table: list of lists to write to a file

        Returns:
            None
        """
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        query = "DELETE FROM `submission`;"
        c.execute(query)

        for obj in obj_list:
            params = [obj.send_date, obj.name, obj.grade, obj.github_link, obj.student_id]
            c.execute("INSERT INTO submission (send_date, grade, name, github_link, student_id) VALUES (?, ?, ?, ?, ?)", params)
            conn.commit()
        conn.close()

    @classmethod
    def write_team_to_db(cls, file_name, teams_list):
        """
    Writes object list into a DB file.

    Args:
        file_name (str): name of file to write to
        table: list of lists to write to a file

    Returns:
        None
    """
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        query = "DELETE FROM `teams_list`;"
        c.execute(query)

        for team in teams_list:
            c.execute("INSERT INTO teams_list (name) VALUES (?)", [team])
            conn.commit()
        conn.close()

    @staticmethod
    def error_integer_handling(chosen_option, value_of_possible_options):
        """
        :param chosen_option: user's input.
        :param value_of_possible_options: how many options users could take? Don't count 0 - exit
        :return: True or False. Will be useful to control while loop in other part of program. If True, continue program.
        """
        try:
            int(chosen_option)
            if int(chosen_option) < 0 or int(chosen_option) > value_of_possible_options:
                raise ValueError
        except TypeError:
            print("Wrong input.")
            m = Ui.get_inputs([""], "")
            return False
        except ValueError:
            print("It must be integer between 1 and " + str(value_of_possible_options) + " or 0. Press enter to try again.")
            m = Ui.get_inputs([""], "")
            return False
        return True

    @staticmethod
    def check_date(max_day, user_day):
        """
        :param max_day: int (e.g. 30)
        :param user_day: str (e.g. 32)
        :return: True (if
        """

        try:
            if int(user_day) > max_day:
                raise ValueError
            return True
        except ValueError:
            return False

    @staticmethod
    def generate_random_id(table):
        """
        Generates random and unique string. Used for id/key generation.
        """
        characters = [['!', '@', '#', '$', '%', '^', '&', '*'], [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]]
        characters.append(list(string.ascii_uppercase))
        characters.append(list(string.ascii_lowercase))
        generated = ''
        is_unique = False
        id_table = []
        for element in table:
            id_table.append(element)

        while not is_unique:
            is_unique = True
            for i in range(2):
                generated += str(characters[0][random.randint(0, len(characters[0])-1)])
                generated += str(characters[1][random.randint(0, len(characters[1])-1)])
                generated += str(characters[2][random.randint(0, len(characters[2])-1)])
                generated += str(characters[3][random.randint(0, len(characters[3])-1)])
            if generated in id_table:
                is_unique = False

        return generated
