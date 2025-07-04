from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return "Hello, Flaskbook!"

@app.route(
           "/hello",
           methods=["GET","POST"],
           endpoint="hello-endpoint"
           )
def hello():
    return "Hello, World!"

# Flask2からは@app.get("/hello")、@app.post("/hello")と記述することが可能
# @app.get("/hello")
# @app.post("/hello")
# def hello():
#     return "Hello, World!"