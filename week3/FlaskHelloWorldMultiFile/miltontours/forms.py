from wtforms import validators, form, StringField, SubmitField
from wtforms.validators import InputRequired
from flask_wtf import FlaskForm

class CheckoutForm(FlaskForm):
    firstname = StringField('First name',validators=[InputRequired()])
    surname = StringField('Surname')
    phone = StringField('phone')
    submit = SubmitField('Go!')