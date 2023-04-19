import flask
import requests
from bs4 import BeautifulSoup
from lxml import etree as et


URL = 'https://karaganda.emenu.delivery/restoran/today_cafe_krg/menu/29951'

class Product:
    @staticmethod
    def get_products():
        response = requests.get(URL)
        soup = BeautifulSoup(response.text, "lxml")
        names = soup.find_all('div', class_='item-title')
        names_breakfast: list[str] = []

        for name in names:
            names_breakfast.append(name.text.strip())
        
        return flask.render_template(
            template_name_or_list='product.html',
            products = names_breakfast
        )


















        # print(structure)
        # print(prices)
        # names: list[str] = []
        # structure: list[str] = []
        # prices: list[str] = []
        # product_list = list[names,structure, prices]

        # for i in range(len(structure)):
        #     current_name = names[i].text.strip()
        #     current_structure = structure[i].text.strip()
        #     current_prices = prices[i].text.strip()
        #     products = current_name, current_structure, current_prices

        # prod = Product(
        #     name=current_name,
        #     structure=current_structure,
        #     price=current_prices
        # )
        # product_list.append(prod)

        # return product_list