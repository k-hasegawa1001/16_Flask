from flask import Blueprint

app1 = Blueprint(
    "app1",
    __name__,
    template_folder="templates",
    static_folder="static"
)

@app1.route("/")
def index():
    return "hello"