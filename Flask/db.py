from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///students.db"
# app.config['SQLALCHEMY_TRACK_MODIFACATIONS'] = False


# Create SQLAlchemy Object
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email=db.Column(db.String(100), unique=True, nullable=False)
    
    
@app.route('/add')
def add_student():
    student = Student(name="Sachin", email="sachinbelbase@gmail.com")
    db.session.add(student)
    db.session.commit()
    return "Student added to our database"

@app.route("/student")
def list_student():
    students = Student.query.all()
    return "<br>".join([f"{s.id}. Name: {s.name} and Email: {s.email}" for s in students])

@app.route("/")
def home():
    return render_template("db.html")

if __name__ =="__main__":
    with app.app_context():
        db.create_all()
    
    app.run(debug=True)