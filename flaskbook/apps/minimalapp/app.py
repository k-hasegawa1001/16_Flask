# url_forを追加でimportする
from flask import Flask, render_template,url_for

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

# show_nameエンドポイントを作成する
@app.route("/name/<name>")
def show_name(name):
    # 変数をテンプレートエンジンに渡す
    return render_template("index.html", name=name)

with app.test_request_context():
    # /
    print(url_for("index"))
    # /hello/world
    print(url_for("hello-endpoint", name="world"))
    # /name/ichiro?page=1
    print(url_for("show_name", name="ichiro",page="1"))