from flask import Flask

# 実習2-1
# create_app関数を作成する
def create_app():
    app = Flask(__name__)

    # 実習2-1
    # app1パッケージからviewsをimportする
    from apps.app1 import views as app1_views
    # app1_viewsをアプリへ登録する
    app.register_blueprint(app1_views.app1, url_prefix="/app1")

    # 実習2-5
    # app2パッケージからviewsをimportする
    from apps.app2 import views as app2_views
    # app2_viewsをアプリへ登録する
    app.register_blueprint(app2_views.app2, url_prefix="/app2")

    return app
