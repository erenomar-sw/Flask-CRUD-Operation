from flask import Flask, render_template, request, redirect
from models import db,StudentModel
from werkzeug.security import generate_password_hash

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


with app.app_context(): 
    db.create_all()

@app.route('/create', methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('table_create.html')
    if request.method == 'POST':
        hobby = request.form.getlist('hobbies')
        hobbies = ','.join(map(str, hobby))
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        gender = request.form['gender']
        hobbies = hobbies
        country = request.form['country']

        students = StudentModel(
            first_name = first_name,
            last_name = last_name,
            email = email,
            password=generate_password_hash(password),
            gender = gender,
            hobbies = hobbies,
            country = country
        )

        db.session.add(students)
        db.session.commit()
        return redirect('/')
    
@app.route('/', methods = ['GET'])
def RetrievelList():
    students = StudentModel.query.all()
    return render_template('datalist.html', students = students)

@app.route('/<int:id>/delete', methods = ['GET','POST'])
def DeleteStudent(id):
    student = StudentModel.query.filter_by(id=id).first()
    if request.method == 'POST':
        if student:
            db.session.delete(student)
            db.session.commit()   
            return redirect('/')
        
    return render_template('delete.html')

@app.route('/<int:id>/edit', methods = ['GET','POST'])
def EditStudent(id):
    student = StudentModel.query.filter_by(id=id).first()
    if request.method == 'POST':        
        if student:
            db.session.delete(student)
            db.session.commit()
            hobby = request.form.getlist('hobbies')
            hobbies = ','.join(map(str, hobby))
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            email = request.form['email']
            password = request.form['password']
            gender = request.form['gender']
            hobbies = hobbies
            country = request.form['country']

            student = StudentModel(
            first_name = first_name,
            last_name = last_name,
            email = email,
            password=generate_password_hash(password),
            gender = gender,
            hobbies = hobbies,
            country = country
        )
            db.session.add(student)
            db.session.commit()
            return redirect('/')
            return f"Student with id = {id} Do Not Exist"

    return render_template('update.html', student = student)

    
app.run(host='localhost', port=5000)