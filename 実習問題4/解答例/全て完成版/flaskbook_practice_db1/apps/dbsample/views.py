from flask import Blueprint

from apps.dbsample.models import Product
from apps.app import db

# 実習4-9
from sqlalchemy import desc

# Blueprintでdbsampleアプリを生成する
dbsample = Blueprint(
    "dbsample",
    __name__,
    template_folder="templates",
    static_folder="static",
)

# 実習4-3
@dbsample.route("/select1") # /dbsample/select1
def select1():
    db.session.query(Product).all()
    return "コンソールログを確認してください"

# 実習4-4
@dbsample.route("/select2") # /dbsample/select2
def select2():
    db.session.query(Product).first()
    return "コンソールログを確認してください"

# 実習4-5
@dbsample.route("/select3/<int:num>") # /dbsample/select3/2
def select3(num):
    db.session.query(Product).get(num)
    return "コンソールログを確認してください"

# 実習4-6 WHERE句(filter_by)
@dbsample.route("/where1/<int:num>") # /dbsample/where1/2
def where1(num):
    db.session.query(Product).filter_by(id=num).all()
    return "コンソールログを確認してください"

# 実習4-7 WHERE句(filter)
@dbsample.route("/where2/<string:str>") # /dbsample/where2/商品
def where2(str):
    db.session.query(Product).filter(Product.name==str).all()
    return "コンソールログを確認してください"

# 実習4-8 ORDER BY句(昇順)
@dbsample.route("/sort1") # /dbsample/sort1
def sort1():
    db.session.query(Product).order_by("price").all()
    return "コンソールログを確認してください"

# 実習4-9 ORDER BY句(降順)
@dbsample.route("/sort2") # /dbsample/sort2
def sort2():
    db.session.query(Product).order_by(desc("price")).all()
    return "コンソールログを確認してください"

# 実習4-10 insert
@dbsample.route("/insert/<string:str>/<int:num>") # /dbsample/insert/商品4/900
def insert(str, num):
    product = Product(
        name=str,
        price=num
    )
    db.session.add(product)
    db.session.commit()
    return "コンソールログを確認してください"

# 実習4-11 update
@dbsample.route("/update/<int:num1>/<string:str>/<int:num2>")
# /dbsample/update/4/商品x/999
def update(num1, str, num2):
    product = db.session.query(Product).filter_by(id=num1).first()
    product.name = str
    product.price = num2

    db.session.add(product)
    db.session.commit()
    return "コンソールログを確認してください"

# 実習4-12 delete
@dbsample.route("/delete/<int:num>") # /dbsample/delete/4
def delete(num):
    product = db.session.query(Product).filter_by(id=num).delete()
    db.session.commit()
    return "コンソールログを確認してください"
