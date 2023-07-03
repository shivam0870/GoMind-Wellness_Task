from app import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    college = db.Column(db.String(100))

    def __init__(self, name, college):
        self.name = name
        self.college = college
