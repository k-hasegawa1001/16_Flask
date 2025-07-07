from flask import Blueprint, render_template

# 実習2-5
# Blueprintでapp2アプリを生成する
app2 = Blueprint(
    "app2",
    __name__,
    template_folder="templates",
    static_folder="static",
)
# 実習2-5
# index
@app2.route("/")
def index():
    return "こんにちは"
