import requests
from bs4 import BeautifulSoup
from lxml import etree as et


# URL = 'https://glovoapp.com/kz/ru/karaganda/today-kgf-kgf/'

# class Product:

URL = 'https://karaganda.emenu.delivery/restoran/today_cafe_krg/menu/29951'

class Product:
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "lxml-xml")
    names = soup.find_all('div', class_='item-title')
    names_breakfast: list[str] = []

    for name in names:
        names_breakfast.append(name.text.strip())


# class Product:
#     names = soup.find_all('div', class_='product-row__name')
#     structure = soup.find_all('span', class_='product-row__info__description')
#     prices = soup.find_all(
#         'div', 
#         class_='product-price product-row__price layout-vertical-tablet'
#     )


#     print(names.text.strip())
    # names: list[str] = []
    # structure: list[str] = []
    # prices: list[str] = []

    # for name in names:
    #     names.append(name.text.strip())
    
    # for struct in structure:
    #     names.append(struct.text.strip())

    # for price in prices:
    #     names.append(price.text.strip())


    # for i in range(len(structure)):
    #     price(f'''
    #     name: {names[i]}
    #     structure: {structure[i]}
    #     price: {prices[i]}
    #     ''')

















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