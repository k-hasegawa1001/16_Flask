from apps.app import db

# db.Modelを継承した独自クラスProductを作成する
class Product(db.Model):
    # テーブル名を指定する
    __tablename__ = "products"
    # カラムを定義する
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, index=True)
    price = db.Column(db.Integer)

# __init__.pyも作成した後、以下を実行
# flask db init
# flask db migrate
# このとき、Detected added table 'products'が表示されていなければおかしい
# flask db upgrade