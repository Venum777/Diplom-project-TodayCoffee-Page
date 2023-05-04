import flask
from flask import url_for
#-----------------------------------------------------
# IMPORT ALL PRODUCTS
from models.pars.breakfast import *
#-----------------------------------------------------


app = flask.Flask(__name__)


@app.route("/products", methods=['GET','POST'])
def get_products():

    return flask.render_template(
        template_name_or_list="products/product.html",
        list_product_breakfast=list_product_breakfast,
        image=list_image_breakfast
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
        list_product_coffee=list_product_cold_drinks,
        image=list_image_cold_drinks
    )

@app.route("/deserts", methods=['GET','POST'])
def get_products_deserts():

    return flask.render_template(
        template_name_or_list="products/desserts.html",
        list_product_coffee=list_product_deserts,
        image=list_image_deserts
    )

@app.route("/firstDish", methods=['GET','POST'])
def get_products_first_dish():

    return flask.render_template(
        template_name_or_list="products/first_dish.html",
        list_product_coffee=list_product_first_dish,
        image=list_image_first_dish
    )

@app.route("/pasts", methods=['GET','POST'])
def get_products_pasts():

    return flask.render_template(
        template_name_or_list="products/pasts.html",
        list_product_coffee=list_product_pasts,
        image=list_image_pasts
    )

@app.route("/pizza", methods=['GET','POST'])
def get_products_pizza():

    return flask.render_template(
        template_name_or_list="products/pizza.html",
        list_product_coffee=list_product_pizza,
        image=list_image_pizza
    )

@app.route("/salad", methods=['GET','POST'])
def get_products_salad():

    return flask.render_template(
        template_name_or_list="products/salad.html",
        list_product_coffee=list_product_salad,
        image=list_image_salad
    )

@app.route("/snacks", methods=['GET','POST'])
def get_products_snacks():

    return flask.render_template(
        template_name_or_list="products/snacks.html",
        list_product_coffee=list_product_snacks,
        image=list_image_snacks
    )

@app.route("/wafflesChesecakes", methods=['GET','POST'])
def get_products_w_and_c():

    return flask.render_template(
        template_name_or_list="products/waffles_and_cheesecakes.html",
        list_product_coffee=list_product_w_and_c,
        image=list_image_w_and_c
    )



if __name__ == '__main__':
    app.run(
        host='localhost',
        port=8080,
        debug=True
    )