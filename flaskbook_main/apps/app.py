from flask import Flask
from flask_login import LoginManager # type: ignore
from flask_migrate import Migrate # type: ignore
from flask_sqlalchemy import SQLAlchemy # type: ignore
from flask_wtf.csrf import CSRFProtect # type: ignore
from apps.config import config

db = SQLAlchemy()
csrf = CSRFProtect()

# LoginManagerをインスタンス化する
login_manager = LoginManager()
# login_view属性に未ログイン時にリダイレクトするエンドポイントを指定する
login_manager.login_view = "auth.signup"
# login_message属性にログイン後に表示するメッセージを指定する
# ここでは何も表示しないよう空を指定する
login_manager.login_message = ""

def create_app(config_key):
    app = Flask(__name__)
    app.config.from_object(config[config_key])

    csrf.init_app(app)

    db.init_app(app)

    Migrate(app,db)

    # login_managerをアプリケーションと連携する
    login_manager.init_app(app)

    from apps.crud import views as crud_views

    app.register_blueprint(crud_views.crud, url_prefix="/crud")

    # これから作成するauthパッケージからviewsをimportする
    from apps.auth import views as auth_views

    # register_blueprintを使いviewsのauthをアプリへ登録する
    app.register_blueprint(auth_views.auth, url_prefix="/auth")

    return app