from flask import Blueprint, render_template, request

# Blueprintでinputapp1アプリを生成する
inputapp1 = Blueprint(
    "inputapp1",
    __name__,
    template_folder="templates",
    static_folder="static",
)

# page1
@inputapp1.route("/page1") # /inputapp1/page1 の /inputapp1 は app.py url_prefixで指定する
def page1():
    return render_template("inputapp1/page1.html")

# page2
@inputapp1.route("/page2", methods=["POST"])
def page2():
    # フォームから送信されたcommentの値を取得する
    comment_val = request.form["comment"]

    return render_template("inputapp1/page2.html", comment=comment_val)
