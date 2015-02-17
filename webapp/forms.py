from flask.ext.wtf import Form
from wtforms import TextField, IntegerField, DateField, SubmitField, validators
import datetime


class SenialForm(Form):
    identificador = IntegerField('Identificador', [validators.DataRequired(),
                                                   validators.NumberRange(min=1, max=9999,
                                                                          message='Fuera de Rango')])
    descripcion = TextField('Descripción', [validators.DataRequired()])
    fecha = DateField('Fecha Adquisción', [validators.DataRequired()],
                      format='%d-%m-%Y', default=datetime.date.today())

    adquirir = SubmitField('Adquirir')
