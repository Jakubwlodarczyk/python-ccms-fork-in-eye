from ui import Ui
import os
import datetime
from Common import Common
from student import Student


class Attendance:
    """
    Creates objects of student's attendance. Each object is a separate day.
    """
    attendances_list = []

    def __init__(self, data, status, id=None):
        self.data = data
        self.status = status
        self.id = id

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
            date_str = "-".join(date_list)
            if date_str > str(datetime.date.today()):
                Ui.print_error_message("No way my friend.")
                wait = Ui.get_inputs([""], "")
                continue
            for day in Attendance.attendances_list:
                if day.data == date_str: #  day.data == str
                    Ui.print_error_message("You have already checked attendance for this day.")
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
                    object = Attendance(day_str, student_status)
                    student.attendance_list.append(object)
                    Attendance.attendances_list.append(object)
                    Ui.print_error_message("\nDone.\n")
                    break
                else:
                    continue

    @staticmethod
    def set_date():
        """
        :return: date of chosen day as list with strings (e.g. ["2017", "05", "03"]
        """
        date = None
        while True:
            os.system("clear")
            options_list = Ui.get_inputs(["1 - Today\n2 - Choose another day\n0 - Go back\n"], "Please set a date:")
            if Common.error_integer_handling(options_list[0], 2):
                if options_list[0] == "0":
                    Attendance.attendance_mini_menu()
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
                            ["Year (e.g. 2017): ", "Month (e.g. 01): ", "Day (e.g. 23): "], "Write date you \
want to change attendance: \n")
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
                                    Ui.print_error_message("Can't accept this date.")
                                    wait = Ui.get_inputs([""], "")
                            if options_list[1] == "04":
                                if Common.check_date(30, options_list[2]):
                                    return date
                                else:
                                    Ui.print_error_message("Can't accept this date.")
                                    wait = Ui.get_inputs([""], "")
                            if options_list[1] == "06":
                                if Common.check_date(30, options_list[2]):
                                    return date
                                else:
                                    Ui.print_error_message("Can't accept this date.")
                                    wait = Ui.get_inputs([""], "")
                            if options_list[1] == "09":
                                if Common.check_date(30, options_list[2]):
                                    return date
                                else:
                                    Ui.print_error_message("Can't accept this date.")
                                    wait = Ui.get_inputs([""], "")
                            if options_list[1] == "11":
                                if Common.check_date(30, options_list[2]):
                                    return date
                                else:
                                    Ui.print_error_message("Can't accept this date.")
                                    wait = Ui.get_inputs([""], "")
                            if options_list[1] == "01" or options_list[1] == "03" or options_list[1] == "05" or options_list[1] == "07" or options_list[1] == "08" or options_list[1] == "10" or options_list[1] == "12":
                                return date
                        else:
                            Ui.print_error_message("Can't accept this date.")
                            wait = Ui.get_inputs([""], "")
                            continue
            else:
                 continue
            date = [options_list[0], options_list[1], options_list[2]]
            wait = Ui.get_inputs([""], "")
            return date

    @staticmethod
    def choose_student():
        """
        Chooses student from Student.student_list
        :return: str: student's id
        """
        while True:
            os.system("clear")
            Ui.print_error_message("Which student do you want to choose?\n")
            for number, student in enumerate(Student.student_list):
                Ui.print_error_message("  {}: {}".format(number + 1, student))
            Ui.print_error_message("  0: Go back\n")
            option_list = Ui.get_inputs([""],"")
            user_option = option_list[0]
            if Common.error_integer_handling(user_option, len(Student.student_list)):
                if user_option[0] == "0":
                    Attendance.attendance_mini_menu()
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
        Ui.print_error_message("Please set up a date.")
        day_list = Attendance.set_date()
        day_str = "-".join(day_list)
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
                        Ui.get_inputs([""], "\nStudent's status has been successfully changed.\nCurrent student's \
status in {}: {}".format(day_str, status))

    @staticmethod
    def view_students_attendance():
        """
        Shows students attendance to school.
        """
        os.system("clear")
        Ui.print_error_message("...::: Students attendance\n\n")
        for student in Student.student_list:
            attendance_points = 0
            counter = 0
            for one_day_obj in student.attendance_list:
                counter += 1
                if one_day_obj.status == "1":
                    attendance_points += 80
                if one_day_obj.status == "2":
                    attendance_points += 100

            if counter == 0:
                Ui.get_inputs([""], "No dates to show.")
                Attendance.attendance_mini_menu()
            else:
                average_attendance = attendance_points / counter
                Ui.print_error_message("{}: {}".format(student, average_attendance))
        Ui.get_inputs([""], "")

    @staticmethod
    def attendance_mini_menu():
        """
        Allows user to control what he wants to do
        """
        while True:
            os.system("clear")
            option_list = Ui.get_inputs(["1 - Check attendance\n2 - Change student's attendance\n\
3 - View students attendance\n0 - Back to main menu\n\n"], "~~Welcome in ..::ATTENDANCE::.. menu~~\n\nWhat would you\
like to do?\n\n")
            if Common.error_integer_handling(option_list[0], 3):
                if int(option_list[0]) == 1:
                    day_str = Attendance.date_control()
                    Attendance.check_attendance_for_day(day_str)
                if int(option_list[0]) == 2:
                    id = Attendance.choose_student()
                    Attendance.change_student_attendance(id)
                if int(option_list[0]) == 3:
                    Attendance.view_students_attendance()
                if int(option_list[0]) == 0:
                    os.system("clear")
                    break # PASTE HERE LINK TO MY MENU (OR NOT)



# Student.student_list.append(Student("Krzysiek","Dzioba","krzysztof.dzioba.93@gmail.com","maslo","student","id7sdg54($)"))
# Student.student_list.append(Student("Krzysiffffek","Dzioba","krzysztof.dzioba.93@gmail.com","maslo","student","iderg754($)"))
# Student.student_list.append(Student("Krsdfszysiek","Dzioba","krzysztof.dzioba.93@gmail.com","maslo","student","iderwg54($)"))
# Attendance.attendance_mini_menu()




