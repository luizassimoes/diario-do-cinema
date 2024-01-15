from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import math
import pandas as pd
from datetime import datetime
from urllib.parse import quote_plus

# class Movie():
#     def __init__(self, nome, data, nota1, nota2):
#         self.__name = nome
#         self.__date = pd.to_datetime(data, format='%d%m%Y', errors='ignore') if data != '' else '-'
#         self.__grade1 = float(nota1) if nota1 != '' else '-'
#         self.__grade2 = float(nota2) if nota2 != '' else '-'
    
#     @property
#     def name(self):
#         return self.__name
    
#     @property
#     def date(self):
#         return self.__date
    
#     @property
#     def grade1(self):
#         return self.__grade1
    
#     @property
#     def grade2(self):
#         return self.__grade2
    
#     @property
#     def avg(self):
#         if self.__date != '-':
#             return (self.__grade1 + self.__grade2) / 2
#         else:
#             return '-'
    
#     @property
#     def sd(self): #standard deviation
#         if self.__date != '-':
#             sd1 = (self.grade1 - self.avg)**2
#             sd2 = (self.grade2 - self.avg)**2
#             return math.sqrt( (sd1 + sd2) / 2 )
#         else: 
#             return '-'


# class User():
#     def __init__(self, user, password):
#         self.__username = user
#         self.__password = password
        
#     @property
#     def username(self):
#         return self.__username

     
# thiago = User('thiago', 'euamoluiza')
# luiza = User('luiza', 'euamothiago')

# users = {
#     luiza.username: luiza,
#     thiago.username: thiago
#     }

# movie1 = Movie('Voo noturno', '10-07-2022', 7.5, 7)
# movie2 = Movie('Um crime de mestre', '12-07-2022', 8.5, 8.5)
# movies = [movie1, movie2]

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
    movies = Movies.query.order_by(Movies.date).all()
    return render_template('lista.html', title='Locadora', movies=movies)

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