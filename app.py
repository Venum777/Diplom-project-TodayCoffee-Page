import flask
# from models.product import Product
import requests
from bs4 import BeautifulSoup
import lxml

app = flask.Flask(__name__)

URL = 'https://karaganda.emenu.delivery/restoran/today_cafe_krg/menu/29951'


@app.route("/product", methods=['GET','POST'])
def productes_page():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "lxml-xml")
    names = soup.find_all('div', class_='item-title')
    names_breakfast: list[str] = []

    for name in names:
        names_breakfast.append(name.text.strip())
    
    return flask.render_template(
        template_name_or_list='product.html',
        products = names_breakfast
    )

if __name__ == '__main__':
    app.run(
        host='localhost',
        port=8000,
        debug=True
    )