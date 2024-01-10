from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy
import math
import pandas as pd

class Movie():
    def __init__(self, nome, data, nota1, nota2):
        self.__name = nome
        self.__date = pd.to_datetime(data, format='%d%m%Y', errors='ignore') if data != '' else '-'
        self.__grade1 = float(nota1) if nota1 != '' else '-'
        self.__grade2 = float(nota2) if nota2 != '' else '-'
    
    @property
    def name(self):
        return self.__name
    
    @property
    def date(self):
        return self.__date
    
    @property
    def grade1(self):
        return self.__grade1
    
    @property
    def grade2(self):
        return self.__grade2
    
    @property
    def avg(self):
        if self.__date != '-':
            return (self.__grade1 + self.__grade2) / 2
        else:
            return '-'
    
    @property
    def sd(self): #standard deviation
        if self.__date != '-':
            sd1 = (self.grade1 - self.avg)**2
            sd2 = (self.grade2 - self.avg)**2
            return math.sqrt( (sd1 + sd2) / 2 )
        else: 
            return '-'


class User():
    def __init__(self, user, password):
        self.__username = user
        self.__password = password
        
    @property
    def username(self):
        return self.__username

     
thiago = User('thiago', 'euamoluiza')
luiza = User('luiza', 'euamothiago')

users = {
    luiza.username: luiza,
    thiago.username: thiago
    }

movie1 = Movie('Voo noturno', '10-07-2022', 7.5, 7)
movie2 = Movie('Um crime de mestre', '12-07-2022', 8.5, 8.5)
movies = [movie1, movie2]

app = Flask(__name__)
app.secret_key = 'LuEThi_Filminhos'

@app.route('/')
def index():
    return render_template('lista.html', title='Locadora', movies=movies)

@app.route('/processing_new', methods=['POST',])
def processing_new():
    movie = request.form['movie']
    date = request.form['date']
    grade1 = request.form['grade1']
    grade2 = request.form['grade2']
    film = Movie(movie, data=date, nota1=grade1, nota2=grade2)
    movies.append(film)
    return redirect(url_for('index'))

@app.route('/new')
def new():
    return render_template('novo.html', title='Novo filme')

app.run(debug=True)