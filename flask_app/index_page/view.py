from flask import render_template, redirect, url_for, Blueprint
from expense.forms import SetExpenseForm
from app import db
from models import Expense
from flask_login import current_user
from sqlalchemy import extract
from flask_app.expense.utils import get_list_expense_users

index_page = Blueprint('index_page', __name__)
"""Blueprint index_page"""
"""Вывод главной страницы и другой справочной информации приложения"""
"""Создание пункта расхода пользователя, сделано на главной странице для удобства пользователя"""


@index_page.route("/", methods=['GET','POST'])
@index_page.route("/main/", methods=['GET', 'POST'] )
def home():
    form = SetExpenseForm()
    if form.validate_on_submit():
        expense = Expense(name = form.nameExpense.data, amount = form.sum.data, author = current_user)
        db.session.add(expense)
        db.session.commit()
        return redirect(url_for('index_page.home'))
    if current_user.is_authenticated:
        sum_expense = 0
        total = 0
        expenses = get_list_expense_users(current_user.get_id())
        for current_expense in expenses:
            sum_expense = sum_expense + current_expense.amount
        budget = current_user.budget
        total = budget - sum_expense
        return render_template('home_is_authenticated.html', expenses=expenses, budget = budget, form = form, sum_expense = sum_expense, total = total)
    else:
        return render_template('main.html')


@index_page.route('/about/')
def get_about():
    return render_template('about.html')        