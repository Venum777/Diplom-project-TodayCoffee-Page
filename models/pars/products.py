import requests
from bs4 import BeautifulSoup


class Product:
    def __init__(
        self,
        name: str,
        structure: str,
        price: int    
    ) -> None:
        self.name = name
        self.structure = structure
        self.price = price

#-------------------------------------------------------------------------------------------
# ALL URLS FOR PARSING PRODUCTS
URL_BREAKFAST = 'https://karaganda.emenu.delivery/restoran/today_cafe_krg/menu/29951'
URL_BREAD = 'https://karaganda.emenu.delivery/restoran/today_cafe_krg/menu/41786'
URL_BURGER = 'https://karaganda.emenu.delivery/restoran/today_cafe_krg/menu/39383'
URL_COFFEE = 'https://karaganda.emenu.delivery/restoran/today_cafe_krg/menu/38938'
URL_COLD_DRINKS = 'https://karaganda.emenu.delivery/restoran/today_cafe_krg/menu/29941'
URL_DESERTS = 'https://karaganda.emenu.delivery/restoran/today_cafe_krg/menu/29944'
URL_FIRST_DISH = 'https://karaganda.emenu.delivery/restoran/today_cafe_krg/menu/29948'
URL_PASTS = 'https://karaganda.emenu.delivery/restoran/today_cafe_krg/menu/29949'
URL_PIZZA = 'https://karaganda.emenu.delivery/restoran/today_cafe_krg/menu/39382'
URL_SALAD = 'https://karaganda.emenu.delivery/restoran/today_cafe_krg/menu/29943'
URL_SNACKS = 'https://karaganda.emenu.delivery/restoran/today_cafe_krg/menu/29945'
URL_W_AND_C = 'https://karaganda.emenu.delivery/restoran/today_cafe_krg/menu/34409'
#-------------------------------------------------------------------------------------------


#--------------------------------------------
# EMPTY LISTS PRODUCT
list_product_breakfast: list[Product] = []
list_product_bread: list[Product] = []
list_product_burger: list[Product] = []
list_product_coffee: list[Product] = []
list_product_cold_drinks: list[Product] = []
list_product_deserts: list[Product] = []
list_product_first_dish: list[Product] = []
list_product_pasts: list[Product] = []
list_product_pizza: list[Product] = []
list_product_salad: list[Product] = []
list_product_snacks: list[Product] = []
list_product_w_and_c: list[Product] = []
#--------------------------------------------


#----------------------------------------------------
# GET URL PRODUCTS
pars_breakfast = requests.get(URL_BREAKFAST)
pars_bread = requests.get(URL_BREAD)
pars_burger = requests.get(URL_BURGER)
pars_coffee = requests.get(URL_COFFEE)
pars_cold_drinks = requests.get(URL_COLD_DRINKS)
pars_deserts = requests.get(URL_DESERTS)
pars_first_dish = requests.get(URL_FIRST_DISH)
pars_pasts = requests.get(URL_PASTS)
pars_pizza = requests.get(URL_PIZZA)
pars_salad = requests.get(URL_SALAD)
pars_snacks = requests.get(URL_SNACKS)
#----------------------------------------
# W_AND_C == Waffles and cheesecakes
pars_w_and_c = requests.get(URL_W_AND_C)
#----------------------------------------
#----------------------------------------------------


#------------------------------------------------------------
# PARS ALL PRODUCTS
breakfast = BeautifulSoup(pars_breakfast.text, "lxml")
bread = BeautifulSoup(pars_bread.text, "lxml")
burger = BeautifulSoup(pars_burger.text, "lxml")
coffee = BeautifulSoup(pars_coffee.text, "lxml")
cold_drinks = BeautifulSoup(pars_cold_drinks.text, "lxml")
deserts = BeautifulSoup(pars_deserts.text, "lxml")
first_dish = BeautifulSoup(pars_first_dish.text, "lxml")
pasts = BeautifulSoup(pars_pasts.text, "lxml")
pizza = BeautifulSoup(pars_pizza.text, "lxml")
salad = BeautifulSoup(pars_salad.text, "lxml")
snacks = BeautifulSoup(pars_snacks.text, "lxml")
w_and_c = BeautifulSoup(pars_w_and_c.text, "lxml")
#------------------------------------------------------------


#----------------------------------------------------------------------------------
# FIND ALL BLOCK PRODUCTS
list_breakfast: list = breakfast.find_all('div', class_='list-product-item')
list_img_breakfast: list = breakfast.find_all('div', class_='square lazy')

list_bread: list = bread.find_all('div', class_='list-product-item')
list_img_bread: list = bread.find_all('div', class_='square lazy')

list_burger: list = burger.find_all('div', class_='list-product-item')
list_img_burger: list = burger.find_all('div', class_='square lazy')

list_coffee: list = coffee.find_all('div', class_='list-product-item')
list_img_coffee: list = coffee.find_all('div', class_='square lazy')

list_cold_drinks: list = cold_drinks.find_all('div', class_='list-product-item')
list_img_cold_drinks: list = cold_drinks.find_all('div', class_='square lazy')

list_deserts: list = deserts.find_all('div', class_='list-product-item')
list_img_deserts: list = deserts.find_all('div', class_='square lazy')

list_first_dish: list = first_dish.find_all('div', class_='list-product-item')
list_img_first_dish: list = first_dish.find_all('div', class_='square lazy')

list_pasts: list = pasts.find_all('div', class_='list-product-item')
list_img_pasts: list = pasts.find_all('div', class_='square lazy')

list_pizza: list = pizza.find_all('div', class_='list-product-item')
list_img_pizza: list = pizza.find_all('div', class_='square lazy')

list_salad: list = salad.find_all('div', class_='list-product-item')
list_img_salad: list = salad.find_all('div', class_='square lazy')

list_snacks: list = snacks.find_all('div', class_='list-product-item')
list_img_snacks: list = snacks.find_all('div', class_='square lazy')

list_w_and_c: list = w_and_c.find_all('div', class_='list-product-item')
list_img_w_and_c: list = w_and_c.find_all('div', class_='square lazy')
#----------------------------------------------------------------------------------


#---------------------------------------------
# EMPTY LISTS (NAMES,STRUCTURE,PRICES,IMAGE) PRODUCT
list_names_breakfast: list[str] = []
list_structure_breakfast: list[str] = []
list_prices_breakfast: list[str] = []
list_image_breakfast: list[str] = []

list_names_bread: list[str] = []
list_structure_bread: list[str] = []
list_prices_bread: list[str] = []
list_image_bread: list[str] = []

list_names_burger: list[str] = []
list_structure_burger: list[str] = []
list_prices_burger: list[str] = []
list_image_burger: list[str] = []

list_names_coffee: list[str] = []
list_structure_coffee: list[str] = []
list_prices_coffee: list[str] = []
list_image_coffee: list[str] = []

list_names_cold_drinks: list[str] = []
list_structure_cold_drinks: list[str] = []
list_prices_cold_drinks: list[str] = []
list_image_cold_drinks: list[str] = []

list_names_deserts: list[str] = []
list_structure_deserts: list[str] = []
list_prices_deserts: list[str] = []
list_image_deserts: list[str] = []

list_names_first_dish: list[str] = []
list_structure_first_dish: list[str] = []
list_prices_first_dish: list[str] = []
list_image_first_dish: list[str] = []

list_names_pasts: list[str] = []
list_structure_pasts: list[str] = []
list_prices_pasts: list[str] = []
list_image_pasts: list[str] = []

list_names_pizza: list[str] = []
list_structure_pizza: list[str] = []
list_prices_pizza: list[str] = []
list_image_pizza: list[str] = []

list_names_salad: list[str] = []
list_structure_salad: list[str] = []
list_prices_salad: list[str] = []
list_image_salad: list[str] = []

list_names_snacks: list[str] = []
list_structure_snacks: list[str] = []
list_prices_snacks: list[str] = []
list_image_snacks: list[str] = []

list_names_w_and_c: list[str] = []
list_structure_w_and_c: list[str] = []
list_prices_w_and_c: list[str] = []
list_image_w_and_c: list[str] = []
#---------------------------------------------


#-------------------------------------------------------------------------------------------
# SEARCH NAMES, STRUCTURE, PRICES AND IMAGE PRODUCTS
for tag1 in list_breakfast:
    names_breakfast = (tag1.find('div', class_='item-title').text)
    list_names_breakfast.append(names_breakfast)

    structure_breakfast = (tag1.find('p', class_='hidden-lg').text.replace("\n",""))
    list_structure_breakfast.append(structure_breakfast)

    prices_breakfast = (tag1.find('span', class_='price').text)
    list_prices_breakfast.append(prices_breakfast)

for img1 in list_img_breakfast:
    img_breakfast = (img1.find('img'))
    list_image_breakfast.append(img_breakfast["src"])

for tag2 in list_bread:
    names_bread = (tag2.find('div', class_='item-title').text)
    list_names_bread.append(names_bread)

    structure_bread = (tag2.find('p', class_='hidden-lg').text.replace("\n",""))
    list_structure_bread.append(structure_bread)

    prices_bread = (tag2.find('span', class_='price').text)
    list_prices_bread.append(prices_bread)

for img2 in list_img_bread:
    img_bread = (img2.find('img'))
    list_image_bread.append(img_bread["src"])


for tag3 in list_burger:
    names_burger = (tag3.find('div', class_='item-title').text)
    list_names_burger.append(names_burger)

    structure_burger = (tag3.find('p', class_='hidden-lg').text.replace("\n",""))
    list_structure_burger.append(structure_burger)

    prices_burger = (tag3.find('span', class_='price').text)
    list_prices_burger.append(prices_burger)

for img3 in list_img_burger:
    img_burger = (img3.find('img'))
    list_image_burger.append(img_burger["src"])


for tag4 in list_coffee:
    names_coffee = (tag4.find('div', class_='item-title').text)
    list_names_coffee.append(names_coffee)

    structure_coffee = (tag4.find('p', class_='hidden-lg').text.replace("\n",""))
    list_structure_coffee.append(structure_coffee)

    prices_coffee = (tag4.find('span', class_='price').text)
    list_prices_coffee.append(prices_coffee)

for img4 in list_img_coffee:
    img_coffee = (img4.find('img'))
    list_image_coffee.append(img_coffee["src"])


for tag5 in list_cold_drinks:
    names_cold_drinks = (tag5.find('div', class_='item-title').text)
    list_names_cold_drinks.append(names_cold_drinks)

    structure_cold_drinks = (tag5.find('p', class_='hidden-lg').text.replace("\n",""))
    list_structure_cold_drinks.append(structure_cold_drinks)

    prices_cold_drinks = (tag5.find('span', class_='price').text)
    list_prices_cold_drinks.append(prices_cold_drinks)

for img5 in list_img_cold_drinks:
    img_cold_drinks = (img5.find('img'))
    list_image_cold_drinks.append(img_cold_drinks["src"])


for tag6 in list_deserts:
    names_deserts = (tag6.find('div', class_='item-title').text)
    list_names_deserts.append(names_deserts)

    structure_deserts = (tag6.find('p', class_='hidden-lg').text.replace("\n",""))
    list_structure_deserts.append(structure_deserts)

    prices_deserts = (tag6.find('span', class_='price').text)
    list_prices_deserts.append(prices_deserts)

for img6 in list_img_deserts:
    img_deserts = (img6.find('img'))
    list_image_deserts.append(img_deserts["src"])


for tag7 in list_first_dish:
    names_first_dish = (tag7.find('div', class_='item-title').text)
    list_names_first_dish.append(names_first_dish)

    structure_first_dish = (tag7.find('p', class_='hidden-lg').text.replace("\n",""))
    list_structure_first_dish.append(structure_first_dish)

    prices_first_dish = (tag7.find('span', class_='price').text)
    list_prices_first_dish.append(prices_first_dish)

for img7 in list_img_first_dish:
    img_first_dish = (img7.find('img'))
    list_image_first_dish.append(img_first_dish["src"])


for tag8 in list_pasts:
    names_pasts = (tag8.find('div', class_='item-title').text)
    list_names_pasts.append(names_pasts)

    structure_pasts = (tag8.find('p', class_='hidden-lg').text.replace("\n",""))
    list_structure_pasts.append(structure_pasts)

    prices_pasts = (tag8.find('span', class_='price').text)
    list_prices_pasts.append(prices_pasts)

for img8 in list_img_pasts:
    img_pasts = (img8.find('img'))
    list_image_pasts.append(img_pasts["src"])


for tag9 in list_pizza:
    names_pizza = (tag9.find('div', class_='item-title').text)
    list_names_pizza.append(names_pizza)

    structure_pizza = (tag9.find('p', class_='hidden-lg').text.replace("\n",""))
    list_structure_pizza.append(structure_pizza)

    prices_pizza = (tag9.find('span', class_='price').text)
    list_prices_pizza.append(prices_pizza)

for img9 in list_img_pizza:
    img_pizza = (img9.find('img'))
    list_image_pizza.append(img_pizza["src"])


for tag10 in list_salad:
    names_salad = (tag10.find('div', class_='item-title').text)
    list_names_salad.append(names_salad)

    structure_salad = (tag10.find('p', class_='hidden-lg').text.replace("\n",""))
    list_structure_salad.append(structure_salad)

    prices_salad = (tag10.find('span', class_='price').text)
    list_prices_salad.append(prices_salad)

for img10 in list_img_salad:
    img_salad = (img10.find('img'))
    list_image_salad.append(img_salad["src"])


for tag11 in list_snacks:
    names_snacks = (tag11.find('div', class_='item-title').text)
    list_names_snacks.append(names_snacks)

    structure_snacks = (tag11.find('p', class_='hidden-lg').text.replace("\n",""))
    list_structure_snacks.append(structure_snacks)

    prices_snacks = (tag11.find('span', class_='price').text)
    list_prices_snacks.append(prices_snacks)

for img11 in list_img_snacks:
    img_snacks = (img11.find('img'))
    list_image_snacks.append(img_snacks["src"])


for tag12 in list_snacks:
    names_w_and_c = (tag12.find('div', class_='item-title').text)
    list_names_w_and_c.append(names_w_and_c)

    structure_w_and_c = (tag12.find('p', class_='hidden-lg').text.replace("\n",""))
    list_structure_w_and_c.append(structure_w_and_c)

    prices_w_and_c = (tag12.find('span', class_='price').text)
    list_prices_w_and_c.append(prices_w_and_c)

for img12 in list_img_w_and_c:
    img_w_and_c = (img12.find('img'))
    list_image_w_and_c.append(img_w_and_c["src"])
#-------------------------------------------------------------------------------------------
    

#--------------------------------------------
# ASSIGN A PRODUCT LIST TO A CLASS
product_breakfast = Product(
    name=list_names_breakfast,
    structure=list_structure_breakfast,
    price=list_prices_breakfast
)

product_bread = Product(
    name=list_names_bread,
    structure=list_structure_bread,
    price=list_prices_bread
)

product_burger = Product(
    name=list_names_burger,
    structure=list_structure_burger,
    price=list_prices_burger
)

product_coffee = Product(
    name=list_names_coffee,
    structure=list_structure_coffee,
    price=list_prices_coffee
)

product_cold_drinks = Product(
    name=list_names_cold_drinks,
    structure=list_structure_cold_drinks,
    price=list_prices_cold_drinks
)

product_deserts = Product(
    name=list_names_deserts,
    structure=list_structure_deserts,
    price=list_prices_deserts
)

product_first_dish = Product(
    name=list_names_first_dish,
    structure=list_structure_first_dish,
    price=list_prices_first_dish
)

product_pasts = Product(
    name=list_names_pasts,
    structure=list_structure_pasts,
    price=list_prices_pasts
)

product_pizza = Product(
    name=list_names_pizza,
    structure=list_structure_pizza,
    price=list_prices_pizza
)

product_salad = Product(
    name=list_names_salad,
    structure=list_structure_salad,
    price=list_prices_salad
)

product_snacks = Product(
    name=list_names_snacks,
    structure=list_structure_snacks,
    price=list_prices_snacks
)

product_w_and_c = Product(
    name=list_names_w_and_c,
    structure=list_structure_w_and_c,
    price=list_prices_w_and_c
)
#--------------------------------------------


list_product_breakfast.append(product_breakfast)
list_product_bread.append(product_bread)
list_product_burger.append(product_burger)
list_product_coffee.append(product_coffee)
list_product_cold_drinks.append(product_cold_drinks)
list_product_first_dish.append(product_first_dish)
list_product_deserts.append(product_deserts)
list_product_pasts.append(product_pasts)
list_product_pizza.append(product_pizza)
list_product_salad.append(product_salad)
list_product_snacks.append(product_snacks)
list_product_w_and_c.append(product_w_and_c)