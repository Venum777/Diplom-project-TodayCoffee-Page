import flask
from models.product import Product


app = flask.Flask(__name__)

@app.route("/product")
def product_page():
    products: list[Product]
    return flask.render_template('product.html', products=products)


if __name__ == '__main__':
    app.run(
        host='localhost',
        port=8000,
        debug=True
    )