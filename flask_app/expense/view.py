from flask import Blueprint, render_template, redirect, url_for, abort
from flask_login import  current_user, login_required
from sqlalchemy import extract
from models import Expense
from app import db
from datetime import datetime

expense_module = Blueprint('expense_module', __name__)


@login_required
@expense_module.route("/", methods=['POST','GET'])
def get_list_expenses():
    expenses = db.session.query(Expense).filter(Expense.id_user == current_user.get_id(), extract('month',Expense.created_date) == datetime.today().month, extract('year', Expense.created_date) == datetime.today().year).order_by(Expense.created_date.desc()).all()
    return render_template('list_expenses.html', expenses = expenses)


@login_required
@expense_module.route("/<int:id_expense>/delete", methods=['POST','GET'])
def delete_expense(id_expense):
    expense = Expense.query.get_or_404(id_expense)
    if expense.id_user == int(current_user.get_id()):
        db.session.delete(expense)
        db.session.commit()
        return redirect(url_for('expense_module.get_list_expenses'))
    else:
        abort(403)