from flask import Blueprint, render_template, request

# Blueprintでinputapp1アプリを生成する
inputapp2 = Blueprint(
    "inputapp2",
    __name__,
    template_folder="templates",
    static_folder="static",
)

# page1
@inputapp2.route("/page1") # /inputapp2/page1 の /inputapp2 は app.py url_prefixで指定する
def page1():
    return render_template("inputapp2/page1.html")

# page2
@inputapp2.route("/page2", methods=["POST"])
def page2():
    # フォームから送信されたcommentの値を取得する
    input_val = request.form["image_file"]

    return render_template("inputapp2/page2.html", image_file=input_val)
