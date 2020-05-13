from flask import render_template, redirect, url_for, Blueprint
from expense.forms import SetExpenseForm
from app import db
from flask_login import current_user
from models import Expense
from sqlalchemy import extract
from datetime import datetime


index_page = Blueprint('index_page', __name__)

@index_page.route("/", methods=['GET','POST'])
@index_page.route("/main/", methods=['GET', 'POST'] )
def home():
    form = SetExpenseForm()
    if form.validate_on_submit():
        expense = Expense(name = form.nameExpense.data, amount = form.sum.data, author = current_user)
        db.session.add(expense)
        db.session.commit()
        print('Расход добававлен')
        return redirect(url_for('index_page.home'))
    if current_user.is_authenticated:
        print('Пользователь авторизован')
        summa = 0
        delsumma = 0
        expenses = db.session.query(Expense).filter(Expense.id_user == current_user.get_id(), extract('month',Expense.created_date) == datetime.today().month, extract('year', Expense.created_date) == datetime.today().year).order_by(Expense.created_date.desc()).all()
        for sumExpense in expenses:
            summa = summa + sumExpense.amount
        budget = current_user.budget
        delsumma = budget - summa
        print(expenses)
        return render_template('home_is_authenticated.html', expenses=expenses, budget = budget, form = form, summa = summa, delsumma = delsumma)
    else:
        print('Пользователь не авторизован')
        return render_template('main.html')


@index_page.route('/about/')
def get_about():
    return render_template('about.html')        