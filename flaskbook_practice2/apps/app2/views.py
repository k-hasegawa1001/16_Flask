from flask import Blueprint,render_template

app2 = Blueprint(
    "app2",
    __name__,
    template_folder="templates",
    static_folder="static"
)

@app2.route("/")
def index():
    return "こんにちは"

@app2.route("/page1")
def page1():
    return render_template("app2/page1.html")