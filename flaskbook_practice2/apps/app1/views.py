from flask import Blueprint,render_template

app1 = Blueprint(
    "app1",
    __name__,
    template_folder="templates",
    static_folder="static"
)

@app1.route("/")
def index():
    return "hello"

@app1.route("/page1")
def page1():
    return render_template("page1.html")

@app1.route("/page2")
def page2():
    return render_template("page2.html")