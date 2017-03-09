from models.student import Student
import sqlite3


class Attendance:
    """
    Creates objects of student's attendance. Each object is a separate day.
    """
    attendances_list = []

    def __init__(self, data, status, id=None):
        self.data = data
        self.status = status
        self.id = id

    def __str__(self):
        remember = ""
        remember_status = None

        if self.status == "1":
            remember_status = 80
        elif self.status == "2":
            remember_status = 100

        for student in Student.student_list:
            if student.id == self.id:
                remember = student
        return "{} {} {}".format(remember, self.data, remember_status)

    @classmethod
    def create_objects_list_from_database(cls):
        """
        Creates abjects based on data from database.
        :param file_path:
        :return:
        """
        conn = sqlite3.connect("database.db")
        c = conn.cursor()

        attendances_list = []
        name_q = "SELECT date, status, student_id FROM attendance;"
        name_db = c.execute(name_q)
        conn.commit()

        for row in name_db:
            date = row[0]
            status = row[1]
            student_id = row[2]

            full_name = cls(date, status, student_id)
            attendances_list.append(full_name)

        conn.close()
        return attendances_list

    @staticmethod
    def student_presence(student_obj):
        """
        :param student_obj: student object
        :return: tuple with counted presence
        """
        present = 0
        late = 0
        absent = 0

        for day in student_obj.attendance_list:
            if day.status == "1":
                late += 1
            if day.status == "2":
                present += 1
            if day.status == "0":
                absent += 1

        return present, late, absent
