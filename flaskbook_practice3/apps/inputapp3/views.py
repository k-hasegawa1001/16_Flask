from flask import Blueprint,render_template,request,redirect

inputapp3 = Blueprint(
    "inputapp3",
    __name__,
    template_folder="templates",
    static_folder="static"
)

@inputapp3.route("/")
def index():
    return redirect("/inputapp3/page1")

@inputapp3.route("/page1")
def page1():
    return 