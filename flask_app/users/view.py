from flask import render_template, url_for, flash, redirect, Blueprint
from app import db, bcrypt, login
from flask_app.users.forms import LoginForm, RegistrationForm, UpdatePasswordForm, UpdateBudgetForm
from flask_login import login_user, current_user, login_required, logout_user
from models import User


users = Blueprint('users',__name__)


@users.route('/login/', methods=['GET', 'POST'])
def login_str():
    if current_user.is_authenticated:
        return redirect(url_for('index_page.home'))
    else:    
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                print('User login now')
                return redirect(url_for('index_page.home'))
        return render_template('login.html',form = form)


@users.route('/registration/', methods=['GET','POST'])
def registration_str():
    form = RegistrationForm()
    if form.validate_on_submit():
        password_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        print(password_hash)
        user = User(name = form.name.data, family = form.family.data,email = form.email.data,password = password_hash, budget=form.budget.data)
        db.session.add(user)
        db.session.commit()
        print('user created')
        flash('Your account has been created!','success')
        return redirect(url_for('users.login_str'))
    return render_template('registration.html', form=form)


@users.route('/profile/',methods=['GET','POST'])
@login_required
def get_profile():
    name = current_user.name
    family = current_user.family
    emailAddress = current_user.email
    budget = current_user.budget
    return render_template('profile.html', first_name = name, second_name = family, email = emailAddress, budget = budget)


@users.route('/changebudget/', methods=['GET','POST'])
@login_required
def change_budget():
    form = UpdateBudgetForm()
    if form.validate_on_submit():
        current_user.budget = form.new_budget.data
        db.session.commit()
        return redirect(url_for('users.get_profile'))
    return render_template('change_budget.html', form = form)


@users.route('/changepassword/', methods=['GET','POST'])
@login_required
def change_password():
    form = UpdatePasswordForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=current_user.email).first()
        if user and bcrypt.check_password_hash(user.password, form.current_password.data):
            password_hash = bcrypt.generate_password_hash(form.new_password.data).decode('utf-8') 
            user.password = password_hash
            db.session.commit()
            logout()
            return redirect(url_for('index_page.home'))
    return render_template('change_password.html', form = form)        


@users.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('index_page.home'))                 