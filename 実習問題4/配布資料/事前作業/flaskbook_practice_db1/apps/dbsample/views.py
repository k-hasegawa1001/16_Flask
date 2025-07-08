from flask import Blueprint

# Blueprintでdbsampleアプリを生成する
dbsample = Blueprint(
    "dbsample",
    __name__,
    template_folder="templates",
    static_folder="static",
)
