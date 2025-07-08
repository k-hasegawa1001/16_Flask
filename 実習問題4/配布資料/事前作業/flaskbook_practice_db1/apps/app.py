# 必要なモジュールをインポートする
__空欄__

# SQLAlchemyのインスタンスを作成する
db=__空欄__

# create_app関数を作成する
def create_app():
    app = Flask(__name__)

    # アプリのコンフィグ設定をする
    app.config.from_mapping(
        SECRET_KEY="2AZSMss3p5QPbcY2hBsJ",
        SQLALCHEMY_DATABASE_URI=f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        # 実行したSQLをコンソールに表示する設定にする
        __空欄__
    )

    #SQLAlchemyとアプリを連携する
    __空欄__

    # Migrateとアプリを連携する
    __空欄__

    # dbsampleパッケージからviewsをimportする。インポート名称はdbsample_viewsとする
    __空欄__ as dbsample_views

    # dbsample_viewsのdbsampleインスタンスをアプリへ登録する。url_prefixは/dbsampleとする
    __空欄__

    return app
