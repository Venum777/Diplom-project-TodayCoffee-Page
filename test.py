import requests
from bs4 import BeautifulSoup


URL = 'https://karaganda.emenu.delivery/restoran/today_cafe_krg/menu/29951'


response = requests.get(URL)
soup = BeautifulSoup(response.text, "lxml")

img: list = soup.find_all('div', class_='square lazy')

image: list = []

for tag4 in img:
    img_breakfast = (tag4.find('img'))
    image.append(img_breakfast)

print(image)

