from flask import Flask, render_template, request, redirect
from models import db,StudentModel

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
    
app.run(host='localhost', port=5000)