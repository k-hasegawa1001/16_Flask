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