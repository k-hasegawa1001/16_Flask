from flask import Flask

def create_app():
    app = Flask(__name__)

    from apps.app1 import views as app1_views

    app.register_blueprint(app1_views.app1, url_prefix="/app1")

    return app