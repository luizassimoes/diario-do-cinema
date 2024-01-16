from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import math
import pandas as pd
from datetime import datetime
from urllib.parse import quote_plus

app = Flask(__name__)
app.secret_key = 'LuEThi_Filminhos'

senha = 'lss003@MySQL'
app.config['SQLALCHEMY_DATABASE_URI'] = \
           '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
               SGBD = 'mysql+mysqlconnector',
               usuario = 'root',
               senha = quote_plus(senha),
               servidor = 'localhost',
               database = 'lu_e_thi'
           )
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    date = db.Column(db.DateTime)
    grade1 = db.Column(db.DECIMAL(10, 1))
    grade2 = db.Column(db.DECIMAL(10, 1))

    def __repr__(self):
        return '<Name %r>' % self.name

class Calculations(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    avg = db.Column(db.DECIMAL(10, 2))
    sd = db.Column(db.DECIMAL(10, 2))
    
    def __repr__(self):
        return '<Name %r>' % self.name

@app.route('/')
def index():
    movies_query = db.session.query(Movies, Calculations).outerjoin(Calculations, Movies.id == Calculations.id).all()
    return render_template('lista.html', title='Locadora', movies=movies_query)

@app.route('/processing_new', methods=['POST',])
def processing_new():
    movie = request.form['movie']
    date = None if request.form['date'] == '' else request.form['date'] 
    grade1 = None if request.form['grade1'] == '' else float(request.form['grade1'])
    grade2 = None if request.form['grade2'] == '' else float(request.form['grade2'])

    if date != None:
        date = datetime.strptime(date, '%d/%m/%Y')
        avg = (grade1 + grade2) / 2
        sd1 = (grade1 - avg)**2
        sd2 = (grade2 - avg)**2
        sd = math.sqrt( (sd1 + sd2) / 2 )

        new_calculations = Calculations(name=movie, avg=avg, sd=sd)
        db.session.add(new_calculations)
        db.session.commit()
    
    new_movie = Movies(name=movie, date=date, grade1=grade1, grade2=grade2)
    db.session.add(new_movie)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/new')
def new():
    return render_template('novo.html', title='Novo filme')

app.run(debug=True)