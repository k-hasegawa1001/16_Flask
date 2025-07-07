from flask import Flask,redirect, render_template,url_for,request,flash,make_response,session
from dotenv import load_dotenv # type: ignore
import os

load_dotenv()

app=Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')


@app.route("/")
def index():
    redirect(url_for("greeting1"))

@app.route("/greeting1")
def greeting1():
    return "こんにちは"

@app.route("/greeting2/<name>")
def greeting2(name):
    return f"こんにちは、{name}さん"

@app.route("/double/<int:num>")
def double(num):
    return "%d" % (num*2)

@app.route("/greeting3/<str>")
def greeting3(str):
    return render_template("greeting3.html", name=str)

@app.route("/static1")
def static1():
    return render_template('static1.html')

@app.route("/form_in1")
def form_in1():
    return render_template("form_in1.html")

@app.route("/form_out1", methods=["post"])
def form_out1():
    comment = request.form["comment"]
    return render_template("form_out1.html", comment=comment)

@app.route("/form_in2")
def form_in2():
    return render_template("form_in2.html")

@app.route("/form_out2", methods=["post"])
def form_out2():
    comment1 = request.form["comment1"]
    # print(comment1)
    comment2 = request.form["comment2"]
    comment3 = request.form["comment3"]
    flash(f"コメント1は{comment1} です")
    flash(f"コメント2は{comment2} です")
    flash(f"コメント3は{comment3} です")
    return render_template("form_out2.html")

@app.route("/cookie_session_set/<str>")
def cookie_session_set(str):
    response = make_response(render_template("cookie_session_set.html", cookie_val=str, session_val=str))
    response.set_cookie("q1-8",str)
    session["q1-8"] = str
    # print(str)
    return response

@app.route("/cookie_session_show")
def cookie_session_show():
    cookie_val=request.cookies.get("q1-8")
    session_val=session["q1-8"]
    print(cookie_val)
    print(session_val)
    return render_template("cookie_session_show.html", cookie_val=cookie_val, session_val=session_val)