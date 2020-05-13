from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange

class SetExpenseForm(FlaskForm):
    sum = IntegerField('Сумма', validators=[DataRequired(), NumberRange(min=1,max=1000000)])
    nameExpense = StringField('Название расхода', validators=[DataRequired(),Length(min=1,max=40)])
    submit = SubmitField('Добавить')