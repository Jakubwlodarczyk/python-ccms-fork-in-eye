# from models.ui import Ui
# import os
# import datetime
# from models.Common import Common
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
    def create_objects_list_from_database(cls):  #, table_name): # from database
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
    def date_control():
        """
        Full checking of date correctness.
        :return:  str date (e.g. "2017-01-25")
        """
        os.system("clear")
        while True:
            os.system("clear")
            date_list = Attendance.set_date()
            if date_list == None:
                return None
            date_str = "-".join(date_list)
            if date_str > str(datetime.date.today()):
                Ui.print_message("No way my friend.")
                wait = Ui.get_inputs([""], "")
                continue
            for day in Attendance.attendances_list:
                if day.data == date_str: #  day.data == str
                    Ui.print_message("You have already checked attendance for this day.")
                    remember = True
                    wait = Ui.get_inputs([""], "")
                    Attendance.attendance_mini_menu()
            return date_str

    @staticmethod
    def check_attendance_for_day(day_str):
        """
        :param day: date (e.g. 2017-01-08)
        """
        for student in Student.student_list:
            while True:
                student_attendance = Ui.get_inputs(["Student status:\n   0 - upsent\n   1 - late\n   2 - present\n"], student)
                if Common.error_integer_handling(student_attendance[0], 2):
                    student_status = student_attendance[0]
                    if student_status == "1":
                        student_status = "80"
                    if student_status == "2":
                        student_status = "100"
                    att = Attendance(day_str, student_status, student.id)
                    student.attendance_list.append(att)
                    Attendance.attendances_list.append(att)
                    Ui.print_message("\nDone.\n")
                    break
                else:
                    continue

    @staticmethod
    def set_date():
        """
        :return: date of chosen day as list with strings (e.g. ["2017", "05", "03"]
        """

        while True:
            os.system("clear")
            options_list = Ui.get_inputs(["1 - Today\n2 - Choose another day\n0 - Go back\n"], "Please set a date:")
            if Common.error_integer_handling(options_list[0], 2):
                if options_list[0] == "0":
                    return None
                if options_list[0] == "1":
                    today = datetime.date.today()
                    today = str(today)
                    today_as_list = today.split("-")
                    date = today_as_list
                    return date
                if options_list[0] == "2":
                    while True:
                        os.system("clear")
                        options_list = Ui.get_inputs(
                            ["Year (e.g. 2017): ", "Month (e.g. 01): ", "Day (e.g. 23): "],
                            "Write date you want to change attendance: \n")
                        today = datetime.date.today()
                        today = str(today)
                        date = [options_list[0], options_list[1], options_list[2]]
                        if len(options_list[2]) < 2 or len(options_list[2]) > 2:
                            continue
                        if len(options_list[1]) < 2 or len(options_list[2]) > 2:
                            continue
                        if len(options_list[0]) < 4 or len(options_list[2]) > 4:
                            continue
                        if Common.error_integer_handling(options_list[0], 9999) and Common.error_integer_handling(options_list[1], 12) and Common.error_integer_handling(options_list[2], 31):
                            if options_list[1] == "02":
                                if Common.check_date(30, options_list[2]):
                                    return date
                                else:
                                    Ui.print_message("Can't accept this date.")
                                    wait = Ui.get_inputs([""], "")
                            if options_list[1] == "04":
                                if Common.check_date(30, options_list[2]):
                                    return date
                                else:
                                    Ui.print_message("Can't accept this date.")
                                    wait = Ui.get_inputs([""], "")
                            if options_list[1] == "06":
                                if Common.check_date(30, options_list[2]):
                                    return date
                                else:
                                    Ui.print_message("Can't accept this date.")
                                    wait = Ui.get_inputs([""], "")
                            if options_list[1] == "09":
                                if Common.check_date(30, options_list[2]):
                                    return date
                                else:
                                    Ui.print_message("Can't accept this date.")
                                    wait = Ui.get_inputs([""], "")
                            if options_list[1] == "11":
                                if Common.check_date(30, options_list[2]):
                                    return date
                                else:
                                    Ui.print_message("Can't accept this date.")
                                    wait = Ui.get_inputs([""], "")
                            if options_list[1] == "01" or options_list[1] == "03" or options_list[1] == "05" or options_list[1] == "07" or options_list[1] == "08" or options_list[1] == "10" or options_list[1] == "12":
                                return date
                        else:
                            Ui.print_message("Can't accept this date.")
                            wait = Ui.get_inputs([""], "")
                            continue
            else:
                 continue

    @staticmethod
    def choose_student():
        """
        Chooses student from Student.student_list
        :return: str: student's id
        """
        while True:
            os.system("clear")
            Ui.print_message("Which student do you want to choose?\n")
            for number, student in enumerate(Student.student_list):
                Ui.print_message("  {}: {}".format(number + 1, student))
            Ui.print_message("  0: Go back\n")
            option_list = Ui.get_inputs([""],"")
            user_option = option_list[0]
            if Common.error_integer_handling(user_option, len(Student.student_list)):
                if user_option[0] == "0":
                    return None
                for number, student in enumerate(Student.student_list):
                    if number + 1 == int(user_option):
                        return student.id

    @staticmethod
    def change_student_attendance(student_id):
        """
        Changes student's attendance of a date you choose inside
        :param student_id: str
        """
        os.system("clear")
        Ui.print_message("Please set up a date.")
        day_list = Attendance.set_date()
        try:
            day_str = "-".join(day_list)
        except:
            return
        option_list = Ui.get_inputs(["New status: "], "0 - upsent, 1 - late, 2 - present\n\n")
        if Common.error_integer_handling(option_list[0], 2):
            student_status = option_list[0]
            for studenten in Student.student_list:
                if studenten.id == student_id:
                    counter = 0
                    status = None
                    for day_obj in studenten.attendance_list:
                        if day_obj.data == day_str:
                            counter += 1
                            day_obj.status = student_status
                            status = day_obj.status
                    if counter == 0:
                        Ui.get_inputs([""], "Nothing changed. Attendance hadn't been found with such date.")
                    else:
                        Ui.get_inputs([""], "\nStudent's status has been successfully changed.\n"
                                            "Current student's status in {}: {}".format(day_str, status))

    @staticmethod
    def view_students_attendance():
        """
        Shows students attendance to school.
        """
        os.system("clear")
        Ui.print_message("...::: Students attendance\n\n")
        for student in Student.student_list:
            attendance_points = 0
            counter = 0
            for one_day_obj in student.attendance_list:
                counter += 1
                attendance_points += int(one_day_obj.status)

            if counter == 0:
                Ui.get_inputs([""], "No dates to show.")
                break
            else:
                average_attendance = attendance_points / counter
                Ui.print_message("{}: {}".format(student, average_attendance))
        Ui.get_inputs([""], "")

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

    @staticmethod
    def attendance_mini_menu():
        """
        Allows user to control what he wants to do
        """
        while True:
            os.system("clear")
            option_list = Ui.get_inputs(["1 - Check attendance\n2 - Change student's attendance\n"
                                         "3 - View students attendance\n0 - Back to main menu\n\n"],
                                        "~~Welcome in ..::ATTENDANCE::.. menu~~\n\nWhat would you "
                                        "like to do?\n\n")

            if Common.error_integer_handling(option_list[0], 3):
                if int(option_list[0]) == 1:
                    day_str = Attendance.date_control()
                    if day_str == None:
                        continue
                    Attendance.check_attendance_for_day(day_str)
                if int(option_list[0]) == 2:
                    id = Attendance.choose_student()
                    if id == None:
                        continue
                    Attendance.change_student_attendance(id)
                if int(option_list[0]) == 3:
                    Attendance.view_students_attendance()
                if int(option_list[0]) == 0:
                    os.system("clear")
                    break
