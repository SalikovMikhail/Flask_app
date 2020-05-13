from flask import Flask
from flask_app.config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
#app = Flask(__name__)
#app.config.from_object(Configuration)
db = SQLAlchemy()
bcrypt = Bcrypt()
login = LoginManager()


    #инициализация приложения
def create_app(config_class = Configuration):    
    app = Flask(__name__)
    app.config.from_object(Configuration)
    
    db.init_app(app)
    bcrypt.init_app(app)
    login.init_app(app)

    from flask_app.users.view import users
    from flask_app.index_page.view import index_page
    from flask_app.expense.view import expense_module

    app.register_blueprint(users, url_prefix='/user')
    app.register_blueprint(index_page)
    app.register_blueprint(expense_module, url_prefix='/expense')
    
    return app