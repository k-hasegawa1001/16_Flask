from apps.crud.forms import UserForm
from apps.app import db
from apps.crud.models import User

from flask import Blueprint,render_template,redirect,url_for

# Blueprintでcrudアプリを生成する
crud=Blueprint(
    "crud",
    __name__,
    template_folder="templates",
    static_folder="static"
)

# indexエンドポイントを作成しindex.htmlを返す
@crud.route("/")
def index():
    return render_template("crud/index.html")

@crud.route("/users/new", methods=["get","post"])
def create_user():
    # UserFromをインスタンス化する
    form = UserForm()
    # フォームの値をバリデートする
    if form.validate_on_submit():
        # ユーザーを作成する
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
        )
        # ユーザーを追加してコミットする
        db.session.add(user)
        db.session.commit()
        # ユーザーの一覧画面へリダイレクトする
        return redirect(url_for("crud.users"))
    return render_template("crud/create.html", form=form)

@crud.route("/users")
def users():
    """ユーザーの一覧を取得する"""
    users=User.query.all()
    return render_template("crud/index.html", users=users)

# methodsにGETとPOSTを指定する
@crud.route("/users/<user_id>", methods=["get","post"])
def edit_user(user_id):
    form = UserForm()

    # Userモデルを利用してユーザーを取得する
    user = User.query.filter_by(id=user_id).first()

    # formからサブミットされた場合はユーザーを更新しユーザーの一覧画面へリダイレクトする
    if form.validate_on_submit():
        user.username = form.username.data
        user.email = form.email.data
        user.password = form.password.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("crud.users"))
    
    # GETの場合はHTMLを返す
    return render_template("crud/edit.html", user=user, form=form)