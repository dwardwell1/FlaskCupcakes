from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Email, Optional, URL


class AddCakeForm(FlaskForm):
    flavor = StringField('Flavor', validators=[
        InputRequired(message="Cupcake flavor can't be blank")])
    size = StringField('Size', validators=[
        InputRequired(message="Cupcake Sizecan't be blank")])
    rating = FloatField('Rating', validators=[
        InputRequired(message="Cupcake rating can't be blank")])
    image = StringField('Image URL', validators=[Optional(),
                                                 URL()])
