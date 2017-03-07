from flask import Flask, render_template, request, redirect, url_for
from models.model import Model
from models.student import Student
from models.submission import Submission
from models.assignments import Assignments

app = Flask(__name__)


@app.route("/students")
def students_list():
    """ Shows list of students """
    students = Model.students_get_all()
    return render_template("show_students_list.html", students=students)


@app.route("/mentors")
def mentors_list():
    """ Shows list of mentors """
    mentors = Model.mentors_get_all()
    return render_template("show_mentors_list.html", mentors=mentors)


@app.route("/submissions")
def submissions_list():
    """Shows list of submissions"""
    submissions = Submission.submission_all()
    return render_template("submission_table.html", submissions=submissions)


@app.route("/teams")
def teams_list():
    """ Shows list of teams"""

    teams = Model.create_teams_list()
    students = Model.students_get_all()

    return render_template("teams.html", teams=teams, students=students)


@app.route("/assignments")
def assignments_list():
    """ Shows list of students """
    assignments = Assignments.assignments_all()
    return render_template("show_assignments.html", assignments=assignments)


@app.route("/add_student", methods=['POST', "GET"])
def add_student():
    """ Add student to database """
    if request.method == "GET":
        return render_template("add.html")
    if request.method == "POST":
        person = []
        person.append([request.form["fname"], request.form["lname"], 
        request.form["student_email"]])
        Model.save_new_student(person)
        students = Model.students_get_all()
        return render_template("show_students_list.html", students=students)

if __name__ == "__main__":
    app.run(debug=True)
