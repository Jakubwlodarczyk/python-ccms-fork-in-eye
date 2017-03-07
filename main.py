from flask import Flask, render_template, request, redirect, url_for
from models.student import Student
from models.attendance import Attendance

app = Flask(__name__)

@app.route("/students")
def students_list():
    """ Shows list of students """
    students = Student.students_get_all()
    return render_template("show_students_list.html", students=students)


@app.route("/students-attendance")
def students_attendance():
    students_bad = Student.students_get_all() #it's from database
    attendances = Attendance.create_objects_list_from_database()
    students = Student.student_presence(attendances, students_bad)
    counted_days = Student.count_days()  #Student.counted_days
    Student.current_score(students)

    return render_template("student_show_attendence.html", students=students, attendances=attendances, counted_days = counted_days)

if __name__ == "__main__":
    app.run(debug=True)
