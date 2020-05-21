from models import Expense
from app import db
from sqlalchemy import extract
from datetime import datetime


"""Получает список расхода пользователя за месяц"""

def get_list_expense_users(id_user):
    expenses = db.session.query(Expense).filter(
        Expense.id_user == id_user,\
        extract('month',Expense.created_date) == datetime.today().month,\
        extract('year', Expense.created_date) == datetime.today().year)\
        .order_by(Expense.created_date.desc()).all()
    return expenses