from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    labels = ["商品A", "商品B", "商品C", "商品D"]
    sales = [120000, 90000, 150000, 80000]

    return render_template("index.html", labels=labels, sales=sales)
