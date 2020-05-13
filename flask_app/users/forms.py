from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, NumberRange
from models import User


class RegistrationForm(FlaskForm):
    name = StringField('First name', validators=[DataRequired(),Length(min=2,max=30)])
    family = StringField('Last name', validators=[DataRequired(),Length(min=2,max=30)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    budget = IntegerField('Budget', validators=[DataRequired(), NumberRange(min=1,max=1000000)])
    submit = SubmitField('Sign up')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')



class UpdatePasswordForm(FlaskForm):
    current_password = PasswordField('Current password', validators=[DataRequired()])
    new_password = PasswordField('New password', validators=[DataRequired()])
    confirm_new_password= PasswordField('Confirm password', validators=[DataRequired(), EqualTo('new_password')])
    submit = SubmitField('Изменить пароль')


class UpdateBudgetForm(FlaskForm):
    new_budget = IntegerField('Budget', validators=[DataRequired(),NumberRange(min=1,max=1000000)])
    submit = SubmitField('Изменить бюджет')