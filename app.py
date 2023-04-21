import flask
from models.product import Product
import requests
from bs4 import BeautifulSoup


URL = 'https://karaganda.emenu.delivery/restoran/today_cafe_krg/menu/29951'

app = flask.Flask(__name__)
products: list[Product] = []


@app.route("/products", methods=['GET','POST'])
def get_products():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "lxml")
    list_breakfast: list = soup.find_all('div', class_='list-product-item')

    list_names_breakfast: list[str] = []
    list_structure_breakfast: list[str] = []
    list_prices_breakfast: list[str] = []

    for tag1 in list_breakfast:
        names_breakfast = (tag1.find('div', class_='item-title').text)
        list_names_breakfast.append(names_breakfast)

    for tag2 in list_breakfast:
        structure_breakfast = (tag2.find('p', class_='hidden-lg').text.replace("\n",""))
        list_structure_breakfast.append(structure_breakfast)

    for tag3 in list_breakfast:
        prices_breakfast = (tag3.find('span', class_='price').text)
        list_prices_breakfast.append(prices_breakfast)

    product = Product(
        name=list_names_breakfast,
        structure=list_structure_breakfast,
        price=list_prices_breakfast
    )
    products.append(product)
        
    return flask.render_template(
        template_name_or_list="product.html",
        products=products
    )


if __name__ == '__main__':
    app.run(
        host='localhost',
        port=8080,
        debug=True
    )