from flask import Flask, render_template
import json
import requests

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/autarization")
def autarization():
    return render_template('log_in.html')

@app.route("/product/")
def product():
    with open("static/product.json") as file:
        product_objects_json : dict = json.load(file)
    product_objects = product_objects_json["data"]
    return render_template('product.html',product_objects = product_objects)

@app.route("/product_info/<int:product_id>")
def product_info(product_id):
    with open("static/product.json") as file:
        product_objects_json : dict = json.load(file)
        product_objects = product_objects_json["data"]
        product_objects_need = product_objects[product_id]
    return render_template('product_info.html',product_objects_need = product_objects_need)

@app.route("/news")
def news():

    data = requests.get("https://fakenews.squirro.com/news/technology").json()

    return render_template('news.html',data=data)