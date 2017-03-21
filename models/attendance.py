import sqlite3
from main import db


class Attendance(db.Model):
    __tablename__ = 'attendance'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    date = db.Column(db.String)
    status = db.Column(db.Integer)
    student_id = db.Column(db.Integer)

    def __init__(self, date, status, student_id):
        self.date = date
        self.status = status
        self.student_id = student_id

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
