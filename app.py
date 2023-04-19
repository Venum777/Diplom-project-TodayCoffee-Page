import flask
from models.product import Product
import requests
from bs4 import BeautifulSoup
import lxml

app = flask.Flask(__name__)

URL = 'https://karaganda.emenu.delivery/restoran/today_cafe_krg/menu/29951'


@app.route("/products", methods=['GET','POST'])
def productes_page():
    products: list[Product] = Product.get_products()
    return products

if __name__ == '__main__':
    app.run(
        host='localhost',
        port=8080,
        debug=True
    )