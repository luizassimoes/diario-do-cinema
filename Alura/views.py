from flask import render_template, request, redirect, session, flash, url_for
from app import app, db
import math
import pandas as pd
from datetime import datetime
from model.movies import *
from model.calculations import *

@app.route('/')
def index():
    movies_query = db.session.query(Movies, Calculations).outerjoin(Calculations, Movies.id == Calculations.id).all()
    return render_template('lista.html', title='Locadora', movies=movies_query)

@app.route('/new')
def new():
    return render_template('novo.html', title='Novo filme')

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

@app.route('/edit')
def edit():
    return render_template('edit.html', title='Editar o filme')

@app.route('/processing_edit', methods=['POST',])
def processing_edit():
    pass