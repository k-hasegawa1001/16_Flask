from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return "Hello, Flaskbook!"

@app.route(
           "/hello/<name>",
           methods=["GET","POST"],
           endpoint="hello-endpoint"
           )
def hello(name):
    # Python 3.6から導入されたf-stringで文字列を定義
    return f"Hello, {name}!"
