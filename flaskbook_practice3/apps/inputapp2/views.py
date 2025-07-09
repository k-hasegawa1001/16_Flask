from flask import Blueprint,render_template,redirect,request

inputapp2 = Blueprint(
    "inputapp2",
    __name__,
    template_folder="templates",
    static_folder="static"
)

@inputapp2.route("/")
def index():
    return redirect("/inputapp2/page1")

@inputapp2.route("/page1")
def page1():
    return render_template("inputapp2/page1.html")

@inputapp2.route("/page2", methods=["post"])
def page2():
    image_filename = request.form["filename"]
    return render_template("/inputapp2/page2.html", filename=image_filename)