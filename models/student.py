from models.user import User
import sqlite3


class Student(User):
    """
    Class Student
    Parent class: User
    """

    teams_list = []
    counted_days = 0

    def __init__(self, id, name, surname, email, password, status, card="none", team="none",):
            User.__init__(self, id, name, surname, email, password, status)
            self.status = 'student'
            self.attendance_list = []
            self.team = team
            self.card = card
            self.present = 0
            self.late = 0
            self.absent = 0
            self.score = 0

    def __str__(self):
        return "{}".format(self.name)

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
