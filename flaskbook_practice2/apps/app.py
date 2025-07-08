from flask import Flask

def create_app():
    app = Flask(__name__)

    from apps.app1 import views as app1_views
    from apps.app2 import views as app2_views

    app.register_blueprint(app1_views.app1, url_prefix="/app1")
    app.register_blueprint(app2_views.app2, url_prefix="/app2")

    return app