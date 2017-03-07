from flask import Flask, render_template, request, redirect, url_for
from models.student import Student
from models.submission import Submission
app = Flask(__name__)

@app.route("/students")
def students_list():
    """ Shows list of students """
    students = Student.students_all()
    return render_template("show_students_list.html", students=students)

@app.route("/submissions")
def submissions_list():
    """Shows list of submissions"""
    submissions = Submission.submission_all()
    return render_template("submission_table.html", submissions=submissions)



if __name__ == "__main__":
    app.run(debug=True)
