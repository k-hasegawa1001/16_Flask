# 必要なモジュールをインポートする
from pathlib import Path
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# SQLAlchemyのインスタンスを作成する
db=SQLAlchemy()

# create_app関数を作成する
def create_app():
    app = Flask(__name__)

    # アプリのコンフィグ設定をする
    app.config.from_mapping(
        SECRET_KEY="2AZSMss3p5QPbcY2hBsJ",
        SQLALCHEMY_DATABASE_URI=f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        # 実行したSQLをコンソールに表示する設定にする
        SQLALCHEMY_ECHO=True
    )

    #SQLAlchemyとアプリを連携する
    db.init_app(app)
    
    # Migrateとアプリを連携する
    Migrate(app, db)

    # dbsampleパッケージからviewsをimportする。インポート名称はdbsample_viewsとする
    from apps.dbsample import views as dbsample_views

    # dbsample_viewsのdbsampleインスタンスをアプリへ登録する。url_prefixは/dbsampleとする
    app.register_blueprint(dbsample_views.dbsample, url_prefix="/dbsample")

    return app
