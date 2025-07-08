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

@app1.route("/page/<int:page>")
def page(page):
    if page == 1:
        return render_template("app1/page1.html")
    elif page == 2:
        return render_template("app1/page2.html")
    else:
        return "ページ番号誤り"