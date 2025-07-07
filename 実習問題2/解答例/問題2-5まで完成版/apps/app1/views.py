from flask import Blueprint, render_template

# 実習2-1
# Blueprintでapp1アプリを生成する
app1 = Blueprint(
    "app1",
    __name__,
    template_folder="templates",
    static_folder="static",
)

# 実習2-1
# index
@app1.route("/")
def index():
    return "hello"

# 実習2-2
# page1
@app1.route("/page1")
def page1():
    return render_template("app1/page1.html")

# 実習2-3
# page2
@app1.route("/page2")
def page2():
    return render_template("app1/page2.html")

# 実習2-4
# page
@app1.route("/page/<int:num>")
def page(num):
    if num == 1:
        return render_template("app1/page1.html")
    elif num == 2:
        return render_template("app1/page2.html")
    else:
        return "ページ番号誤り"
