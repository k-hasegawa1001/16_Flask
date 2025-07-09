from flask import Flask

def create_app():
    app = Flask(__name__)

    from apps.inputapp1 import views as inputapp1_views

    app.register_blueprint(inputapp1_views.inputapp1, url_prefix="/inputapp1")

    return app