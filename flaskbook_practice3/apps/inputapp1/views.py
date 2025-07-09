from flask import Blueprint,render_template,request

inputapp1 = Blueprint(
    "inputapp1",
    __name__,
    template_folder="templates",
    static_folder="static"
)

@inputapp1.route("/page1")
def page1():
    return render_template("inputapp1/page1.html")

@inputapp1.route("/page2", methods=["post"])
def page2():
    comment = request.form["comment"]
    return render_template("inputapp1/page2.html", comment=comment)