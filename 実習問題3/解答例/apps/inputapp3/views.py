from flask import Blueprint, flash, current_app, render_template, request, url_for, redirect
from pathlib import Path
import pickle

# Blueprintでinputapp3アプリを生成する
inputapp3 = Blueprint(
    "inputapp3",
    __name__,
    template_folder="templates",
    static_folder="static",
)

# page1
@inputapp3.route("/page1") # /inputapp3/page1 の /inputapp3 は app.pyのurl_prefixで指定する
def page1():
    return render_template("inputapp3/page1.html")


# page2
@inputapp3.route("/page2", methods=["POST"]) # /inputapp3/page2 の /inputapp3 は app.pyのurl_prefixで指定する
def page2():
    # フォームから送信された値を取得する
    height_val = request.form["height"] # 身長
    weight_val = request.form["weight"] # 体重
    age_val = request.form["age"] # 年代


    try:
        # 入力値を文字列から数値へ変換
        height_val = int(height_val)
        weight_val = int(weight_val)
        age_val = int(age_val)
    except:
        # 入力エラーの場合はpage1に戻す
        flash("入力値を見直してください")
        return redirect(url_for("inputapp3.page1"))


    # ファイルのパスの指定方法 Flaskテキスト P228
    model_path = Path(current_app.root_path, "inputapp3", "KvsT.pkl")


    # スッキリわかるPythonによる機械学習入門 P123～124
    # モデルの読み込み
    with open( model_path, 'rb') as f:
        print(model_path)
        model = pickle.load(f)

    # 予測データの作成
    predict_data = [[height_val, weight_val, age_val]]

    # 予測の実行(結果はリストで返ってくるため、最初の1件だけを取得)
    result_val = model.predict(predict_data)[0]

    # 予測結果を表示する
    return render_template("inputapp3/page2.html", result=result_val)
