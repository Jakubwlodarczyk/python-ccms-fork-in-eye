from flask import Flask, render_template, request, redirect, url_for
from models.student import Student
app = Flask(__name__)

@app.route("/students")
def students_list():
    """ Shows list of students """
    students = Student.students_all()
    return render_template("show_students_list.html", students=students)


if __name__ == "__main__":
    app.run(debug=True)
