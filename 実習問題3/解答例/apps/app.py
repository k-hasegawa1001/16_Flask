from flask import Flask

# 実習3-1
# create_app関数を作成する
def create_app():
    app = Flask(__name__)

    # flashを使用するため、SECRET_KEYを追加する
    app.config["SECRET_KEY"] = "2AZSMss3p5QPbcY2hBsJ"

    # 実習3-1
    # inputapp1パッケージからviewsをimportする
    from apps.inputapp1 import views as inputapp1_views
    # inputapp1_viewsをアプリへ登録する
    app.register_blueprint(inputapp1_views.inputapp1, url_prefix="/inputapp1")

    # 実習3-2
    # inputapp2パッケージからviewsをimportする
    from apps.inputapp2 import views as inputapp2_views
    # inputapp2_viewsをアプリへ登録する
    app.register_blueprint(inputapp2_views.inputapp2, url_prefix="/inputapp2")

    # 実習3-3
    # inputapp3パッケージからviewsをimportする
    from apps.inputapp3 import views as inputapp3_views
    # inputapp3_viewsをアプリへ登録する
    app.register_blueprint(inputapp3_views.inputapp3, url_prefix="/inputapp3")

    return app
