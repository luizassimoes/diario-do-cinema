from flask import render_template, request, redirect, session, flash, url_for
from sqlalchemy import desc
import pandas as pd
from datetime import datetime

from app import app, db
from model.movies import *
from helpers import avg_sd, MovieForm


@app.route('/') # movies')
def movie_index():
    movies_query = db.session.query(Movies).order_by(desc(Movies.date)).all()
    return render_template('movie_index.html', title='Diário do Cinema', movies=movies_query)

@app.route('/new')
def new():
    form = MovieForm()
    return render_template('new.html', title='Novo filme', form=form)

@app.route('/processing_new', methods=['POST',])
def processing_new():
    form = MovieForm(request.form)

    movie  = form.name.data
    date   = form.date.data if form.date.data else None
    grade1 = float(form.grade1.data) if form.grade1.data else None 
    grade2 = float(form.grade2.data) if form.grade2.data else None 
    image  = request.files['image'].read() if request.files['image'] else None     # O read faz a leitura dos Bytes da imagem 
    avg, sd = avg_sd(grade1=grade1, grade2=grade2)
    new_movie = Movies(name=movie, date=date, grade1=grade1, grade2=grade2, image=image, avg=avg, sd=sd)
    db.session.add(new_movie)
    db.session.commit()
    
    return redirect(url_for('movie_index'))

@app.route('/to-watch')
def to_watch():
    movies_query = db.session.query(Movies).order_by(desc(Movies.date)).all()
    return render_template('to_watch.html', title='Locadora', movies=movies_query)

@app.route('/edit/<int:id>')
def edit(id):
    movie = Movies.query.filter_by(id=id).first()
    form = MovieForm()
    form.name.data = movie.name
    form.date.data = movie.date
    form.grade1.data = movie.grade1
    form.grade2.data = movie.grade2

    return render_template('edit.html', title='Editar o filme', movie=movie, form=form)

@app.route('/processing_edit', methods=['POST',])
def processing_edit():
    form = MovieForm()

    if form.validate_on_submit():
        movie        = Movies.query.filter_by(id=request.form['id']).first()
        movie.name   = form.name.data
        movie.date   = form.date.data
        movie.grade1 = form.grade1.data
        movie.grade2 = form.grade2.data
        movie.image  = request.files['image'].read() if request.files['image'].read() else None

        avg, sd = avg_sd(grade1=movie.grade1, grade2=movie.grade2)
        movie.avg = avg
        movie.sd = sd

        db.session.add(movie)
        db.session.commit()

    return redirect(url_for('movie_index'))

@app.route('/delete/<int:id>')
def delete(id):
    Movies.query.filter_by(id=id).delete()
    db.session.commit()
    flash('Filme deletado :(')
    return redirect(url_for('movie_index'))