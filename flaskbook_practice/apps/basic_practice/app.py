from flask import Flask,redirect, render_template,url_for,request,flash
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
    flash(comment1)
    flash(comment2)
    flash(comment3)
    return render_template("form_out2.html")