from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, NumberRange, ValidationError
from models import User


class RegistrationForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired(),Length(min=2,max=30)])
    family = StringField('Фамилимя', validators=[DataRequired(),Length(min=2,max=30)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    confirm_password = PasswordField('Повторите пароль', validators=[DataRequired(), EqualTo('password')])
    budget = IntegerField('Бюджет', validators=[DataRequired(), NumberRange(min=1,max=1000000)])
    submit = SubmitField('Зарегистрироваться')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Пользователь с данным адресом электронной почты уже существует')

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')



class UpdatePasswordForm(FlaskForm):
    current_password = PasswordField('Текущий пароль', validators=[DataRequired()])
    new_password = PasswordField('Новый пароль', validators=[DataRequired()])
    confirm_new_password= PasswordField('Повторите новый пароль', validators=[DataRequired(), EqualTo('new_password')])
    submit = SubmitField('Изменить пароль')


class UpdateBudgetForm(FlaskForm):
    new_budget = IntegerField('Бюджет', validators=[DataRequired(),NumberRange(min=1,max=1000000)])
    submit = SubmitField('Изменить бюджет')