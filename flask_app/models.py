from app import db, login
from datetime import datetime
from flask_login import UserMixin
#Модели в бl



#TO DO доделать модели БД
class User(db.Model,UserMixin):
    """Таблица  пользователя"""
    __tablename__='Users'
    id = db.Column(db.Integer(), primary_key = True )
    name = db.Column(db.String(30), nullable = False )
    family = db.Column(db.String(30))
    email = db.Column(db.String(255), unique = True, nullable = False)
    password = db.Column(db.String(32), nullable = False)
    budget = db.Column(db.Integer, nullable = False)
    expenses = db.relationship('Expense' ,backref = 'author', lazy=True)

    def __repr__(self):
        return "name {}, email {}, budget {}".format(self.name,self.email,self.budget)


class Expense(db.Model):
    """Таблица расходов"""
    __tablename__='Expense'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(40), nullable = False)
    amount = db.Column(db.Integer, nullable = False)
    created_date = db.Column(db.DateTime,index = True, default = datetime.now())
    id_user = db.Column(db.Integer,db.ForeignKey('Users.id'))

    def __repr__(self):
        return "name {}, amount {}, id user {}, created date {}".format(self.name,self.amount,self.id_user,self.created_date)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))