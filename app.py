from flask import Flask, redirect, url_for, render_template, request, session
import flask
from random import choices
import string

#-----------------------------------------------------
# IMPORT ALL PRODUCTS
from models.pars.products import *
from services.interface import *
#-----------------------------------------------------

from models.pars.review import *
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from services.interface import *

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///review.db"
db.init_app(app)
app.secret_key = (''.join(choices(string.ascii_lowercase, k=20)))


# ---------------------------------------------
# Главная страница
# ---------------------------------------------
@app.route("/", methods=["GET"])
def main_page():
    if not session.get("login") is None:
        return render_template("index.html")
    return redirect(url_for("registration"))

# ---------------------------------------------
# Страница регистрации
# ---------------------------------------------
@app.route("/registration", methods=["GET"])
def registration():
    if not session.get("login") is None:
        return redirect(url_for("main_page"))
    return render_template("views/registration.html")


# ---------------------------------------------
# Страница авторизации
# ---------------------------------------------
@app.route("/authorization", methods=["GET"])
def authorization():
    if not session.get("login") is None:
        return redirect(url_for("main_page"))
    return render_template("views/authorization.html")


# ---------------------------------------------
# Страница деавторизации
# ---------------------------------------------
@app.route("/deauth", methods=["GET"])
def deauth():
    session.clear()
    return redirect(url_for("main_page"))

# ---------------------------------------------
# API's
# ---------------------------------------------
# ---------------------------------------------
# API регистрации
# ---------------------------------------------
@app.route("/api/v1/registration", methods=["GET", "POST"])
def registration_api():
    data = request.get_json()
    result_of_registration = registrate(data=data)
    return json.dumps(result_of_registration)

# ---------------------------------------------
# API авторизации 
# ---------------------------------------------
@app.route("/api/v1/authorization", methods=["GET", "POST"])
def authorization_api():
    data = request.get_json()
    result_of_authorization = authorize(data=data)
    return json.dumps(result_of_authorization)


@app.route('/contacts')
def contacts_page():
    return flask.render_template(
        template_name_or_list="menu-bar/contacts.html"
    )


@app.route('/info')
def info_page():
    return flask.render_template(
        template_name_or_list="menu-bar/info.html"
    )

@app.route('/stocks')
def stocks_page():
    return flask.render_template(
        template_name_or_list="menu-bar/stocks.html"
    )


@app.route("/breakfast", methods=['GET','POST'])
def get_products_breakfast():

    return flask.render_template(
        template_name_or_list="products/breakfast.html",
        list_product_breakfast=list_product_breakfast,
        image=list_image_breakfast
    )

@app.route("/bread", methods=['GET','POST'])
def get_products_bread():

    return flask.render_template(
        template_name_or_list="products/bread.html",
        list_product_bread=list_product_bread,
        image=list_image_bread
    )

@app.route("/burger", methods=['GET','POST'])
def get_products_burger():

    return flask.render_template(
        template_name_or_list="products/burger.html",
        list_product_burger=list_product_burger,
        image=list_image_burger
    )

@app.route("/coffee", methods=['GET','POST'])
def get_products_coffee():

    return flask.render_template(
        template_name_or_list="products/coffee.html",
        list_product_coffee=list_product_coffee,
        image=list_image_coffee
    )

@app.route("/coldDrinks", methods=['GET','POST'])
def get_products_cold_drinks():

    return flask.render_template(
        template_name_or_list="products/cold_drinks.html",
        list_product_cold_drinks=list_product_cold_drinks,
        image=list_image_cold_drinks
    )

@app.route("/deserts", methods=['GET','POST'])
def get_products_deserts():

    return flask.render_template(
        template_name_or_list="products/desserts.html",
        list_product_deserts=list_product_deserts,
        image=list_image_deserts
    )

@app.route("/firstDish", methods=['GET','POST'])
def get_products_first_dish():

    return flask.render_template(
        template_name_or_list="products/first_dish.html",
        list_product_first_dish=list_product_first_dish,
        image=list_image_first_dish
    )

@app.route("/pasts", methods=['GET','POST'])
def get_products_pasts():

    return flask.render_template(
        template_name_or_list="products/pasts.html",
        list_product_pasts=list_product_pasts,
        image=list_image_pasts
    )

@app.route("/pizza", methods=['GET','POST'])
def get_products_pizza():

    return flask.render_template(
        template_name_or_list="products/pizza.html",
        list_product_pizza=list_product_pizza,
        image=list_image_pizza
    )

@app.route("/salad", methods=['GET','POST'])
def get_products_salad():

    return flask.render_template(
        template_name_or_list="products/salad.html",
        list_product_salad=list_product_salad,
        image=list_image_salad
    )

@app.route("/snacks", methods=['GET','POST'])
def get_products_snacks():

    return flask.render_template(
        template_name_or_list="products/snacks.html",
        list_product_snacks=list_product_snacks,
        image=list_image_snacks
    )

@app.route("/wafflesChesecakes", methods=['GET','POST'])
def get_products_w_and_c():

    return flask.render_template(
        template_name_or_list="products/waffles_and_cheesecakes.html",
        list_product_w_and_c=list_product_w_and_c,
        image=list_image_w_and_c
    )


#-----------------------------------------------
# Создаем экземпляр класса БД(Rev) для написания отзыва
#-----------------------------------------------
class Rev(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=False, nullable=False)
    # description = db.Column(db.String, unique=True, nullable=False)
    rate = db.Column(db.Integer)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

with app.app_context():
    db.create_all()
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


#-----------------------------------------------
# Создаем отзыв
#-----------------------------------------------
@app.route("/write", methods=["GET", "POST"])
def write_review():
    if request.method == "POST":
        review = Rev(
            name = request.form['name'],
            # description = request.form['description'],
            rate = request.form['rate'],
        )
        try:
            db.session.add(review)
            db.session.commit()
            return redirect(url_for('review_page'))
        except:
            return 'При добавлении отзыва произошла ошибка'
    return render_template("review/write_review.html")
#-----------------------------------------------

# ---------------------------------------------
# Страница отзывы
# ---------------------------------------------
@app.route("/reviews", methods=["GET", "POST"])
def review_page():
    reviews = db.session.execute(db.select(Rev)).scalars()
    return flask.render_template(
        template_name_or_list="review/review.html",
        reviews = reviews,
        list_review = list_review,
        image = list_img_review
    )
#-----------------------------------------------


if __name__ == "__main__":
    app.run(
        host=HOST,
        port=PORT
    )