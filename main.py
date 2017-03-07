from flask import Flask, render_template, request, redirect, url_for
from models.model import Model
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


if __name__ == "__main__":
    app.run(debug=True)
