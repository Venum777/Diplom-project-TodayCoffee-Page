import requests
from bs4 import BeautifulSoup


class Review:
    def __init__(
            self,
            name: str,
            date: str,
            rate: str
        ) -> None:
        self.name = name
        self.date = date
        self.rate = rate

URL = 'https://karaganda.emenu.delivery/restoran/today_cafe_krg/review'

list_review: list[Review] = []
pars_review = requests.get(URL)
review = BeautifulSoup(pars_review.text, 'lxml')

review_block: list = review.find_all('div', class_='list-review-item')
review_img = review.find_all('div', class_='logo')


list_name_review: list[str] = []
list_date_review: list[str] = []
list_rate_review: list[str] = []
list_img_review: list[str] = []


for tag1 in review_block:
    name_review = (tag1.find('b', class_='review-username').text)
    list_name_review.append(name_review)

    date_review = (tag1.find('span', class_='review-date').text)
    list_date_review.append(date_review)

    rate_review = (tag1.find('strong').text.replace("\n","").lstrip().rstrip())
    list_rate_review.append(rate_review)


for img1 in review_img:
    img_review = img1.find('img')
    list_img_review.append(img_review["src"])


reviews = Review(
    name=list_name_review,
    date=list_date_review,
    rate=list_rate_review
)

list_review.append(reviews)
