from flask import Blueprint, render_template, request
from app.models import Student, db

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        college = request.form['college']

        student = Student(name=name, college=college)
        db.session.add(student)
        db.session.commit()

    students = Student.query.all()
    return render_template('index.html', students=students)
