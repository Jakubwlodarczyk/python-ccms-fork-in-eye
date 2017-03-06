from flask import Flask, render_template, request, redirect, url_for
from models.student import Student
from models.assignments import Assignments
app = Flask(__name__)

@app.route("/students")
def students_list():
    """ Shows list of students """
    students = Student.students_all()
    return render_template("show_students_list.html", students=students)


@app.route("/assignments")
def assignments_list():
    """ Shows list of students """
    assignments = Assignments.assignments_all()
    return render_template("show_assignments.html", assignments=assignments)


if __name__ == "__main__":
    app.run(debug=True)
