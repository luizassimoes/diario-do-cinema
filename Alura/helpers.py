from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField, DateField, validators 
import math

from app import app

# Classes: -------------------------------------------------------------------------------------------------

class MovieForm(FlaskForm):
    name = StringField('Nome do Filme', [validators.DataRequired(), validators.Length(min=1, max=100)])
    date = DateField('Visto em?')
    grade1 = DecimalField('Nota Lu')
    grade2 = DecimalField('Nota Thi')
    submit = SubmitField('Salvar')


# Funções: -------------------------------------------------------------------------------------------------
    
def avg_sd(grade1, grade2):
    if grade1 is None:
        return None, None
    
    g1 = float(grade1)
    g2 = float(grade2)
    avg = (g1 + g2) / 2
    sd1 = (g1 - avg)**2
    sd2 = (g2 - avg)**2
    sd = math.sqrt( (sd1 + sd2) / 2 )

    return avg, sd