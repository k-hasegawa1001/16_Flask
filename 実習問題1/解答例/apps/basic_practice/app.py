from flask import Flask, render_template, request, flash, make_response, session

# Flaskクラスをインスタンス化する
app = Flask(__name__)

# 実習1-7
# SECRET_KEYを追加する
app.config["SECRET_KEY"] = "2AZSMss3p5QPbcY2hBsJ"

# 実習1-1
@app.route("/greeting1")
def greeting1():
    return "こんにちは"

# 実習1-2
@app.route("/greeting2/<name>")
def greeting2(name):
    return f"こんにちは、{name}さん"


# 実習1-3
@app.route("/double/<int:num>")
def double(num):
    return str(num * 2)

# 実習1-4
@app.route("/greeting3/<name>")
def greeting3(name):
    # テンプレートを利用する。テンプレート内のnameとして使用する値を設定する
    return render_template("basic_practice/greeting3.html", name=name)

# 実習1-5
@app.route("/static1")
def static1():
    # テンプレートを利用する。
    return render_template("basic_practice/static1.html")

# 実習1-6
@app.route("/form_in1")
def form_in1():
    return render_template("basic_practice/form_in1.html")

@app.route("/form_out1", methods=['POST'])
def form_out1():
    # フォームから送信されたcommentの値を取得する
    comment_val = request.form["comment"]

    # テンプレートを利用する。テンプレート内のcommentとして使用する値を設定する
    return render_template("basic_practice/form_out1.html", comment=comment_val)

# 実習1-7
@app.route("/form_in2")
def form_in2():
    return render_template("basic_practice/form_in2.html")

@app.route("/form_out2", methods=['POST'])
def form_out2():
    # フォームから送信されたcomment1～comment3の値をflashに設定する
    flash("コメント1は" + request.form["comment1"] + " です")
    flash("コメント2は" + request.form["comment2"] + " です")
    flash("コメント3は" + request.form["comment3"] + " です")

    return render_template("form_out2.html")

# 実習1-8
@app.route("/cookie_session_set/<val1>")
def cookie_session_set(val1):
    # レスポンスオブジェクトを取得
    response = make_response(
        render_template("basic_practice/cookie_session_set.html", cookie_val=val1, session_val=val1)
    )

    response.set_cookie("q1-8", val1)
    session["q1-8"] = val1

    return response

@app.route("/cookie_session_show")
def cookie_session_show():
    # cookieから値を取得
    cookie_val = request.cookies.get("q1-8")
    # sessionから値を取得
    session_val = session["q1-8"]

    # テンプレートを表示
    return render_template("basic_practice/cookie_session_show.html", cookie_val=cookie_val, session_val=session_val)
