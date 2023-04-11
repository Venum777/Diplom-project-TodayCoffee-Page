import requests
from bs4 import BeautifulSoup


URL = 'https://glovoapp.com/kz/ru/karaganda/today-kgf-kgf/'

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")


class Product:
    def product_page():
        names = soup.find_all('div', class_='product-row__name')
        structure = soup.find_all('span', class_='product-row__info__description')
        prices = soup.find_all(
            'div', 
            class_='product-price product-row__price layout-vertical-tablet'
            )
        
        list_product: list[str] = []

        for i in range(len(names)):
            current_name = names[i].text.strip()
            current_structure = structure[i].text.strip()
            current_prices = prices[i].text.strip()
            products = current_name, current_structure, current_prices
            list_product.append(products)

        return list_product