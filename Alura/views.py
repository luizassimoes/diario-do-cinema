from flask import render_template, request, redirect, session, flash, url_for
from sqlalchemy import desc
import math
import pandas as pd
from datetime import datetime

from app import app, db
from model.movies import *
from model.calculations import *

def avg_sd(grade1, grade2):
    g1 = float(grade1)
    g2 = float(grade2)
    avg = (g1 + g2) / 2
    sd1 = (g1 - avg)**2
    sd2 = (g2 - avg)**2
    sd = math.sqrt( (sd1 + sd2) / 2 )
    return avg, sd


@app.route('/')
def index():
    movies_query = db.session.query(Movies, Calculations).outerjoin(Calculations, Movies.id == Calculations.id).order_by(desc(Movies.date)).all()
    return render_template('list.html', title='Locadora', movies=movies_query)

@app.route('/new')
def new():
    return render_template('new.html', title='Novo filme')

@app.route('/processing_new', methods=['POST',])
def processing_new():
    movie = request.form['name']
    date = None if request.form['date'] == '' else request.form['date'] 
    grade1 = None if request.form['grade1'] == '' else float(request.form['grade1'])
    grade2 = None if request.form['grade2'] == '' else float(request.form['grade2'])

    if date != None:
        date = datetime.strptime(date, '%d/%m/%Y')
        avg, sd = avg_sd(grade1=grade1, grade2=grade2)

        new_calculations = Calculations(name=movie, avg=avg, sd=sd)
        db.session.add(new_calculations)
        db.session.commit()
    
    new_movie = Movies(name=movie, date=date, grade1=grade1, grade2=grade2)
    db.session.add(new_movie)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/edit/<int:id>')
def edit(id):
    movie = Movies.query.filter_by(id=id).first()
    return render_template('edit.html', title='Editar o filme', movie=movie)

@app.route('/processing_edit', methods=['POST',])
def processing_edit():
    movie = Movies.query.filter_by(id=request.form['id']).first()
    movie.name = request.form['name']
    movie.date = datetime.strptime(request.form['date'], '%d/%m/%Y')
    movie.grade1 = request.form['grade1']
    movie.grade2 = request.form['grade2']

    avg, sd = avg_sd(grade1=movie.grade1, grade2=movie.grade2)
    calculus = Calculations.query.filter_by(id=request.form['id']).first()
    calculus.avg = avg
    calculus.sd = sd

    db.session.add(movie)
    db.session.commit()
    db.session.add(calculus)
    db.session.commit()

@app.route('/delete/<int:id>')
def delete(id):
    Movies.query.filter_by(id=id).delete()
    Calculations.query.filter_by(id=id).delete()
    db.session.commit()
    flash('Filme deletado :(')
    return redirect(url_for('index'))


    return redirect(url_for('index'))