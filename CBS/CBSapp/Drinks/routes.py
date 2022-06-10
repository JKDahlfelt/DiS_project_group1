from flask import render_template, url_for, flash, redirect, request, Blueprint
from CBSapp import app, conn, bcrypt
from CBSapp.forms import CustomerLoginForm, EmployeeLoginForm
from flask_login import login_user, current_user, logout_user, login_required
from CBSapp.models import select_Bars, select_Drinks, select_Bars_Beers, select_Bars_Cider, select_Bars_Shot, select_Bars_KU, select_top_5_sold


Drinks = Blueprint('Drinks', __name__)

posts = [{}]

# @Drinks.route("/")
@Drinks.route("/")
@Drinks.route("/home")
def home():
    return render_template('home.html', posts=posts)

@Drinks.route("/beers", methods=['GET', 'POST'])
def beersearch():
    drinks_data = select_Drinks()
    # print(drinks_data)
    return render_template('beersearch.html', title='Beer table', drinks_data = drinks_data)


@Drinks.route("/barlist", methods=['GET', 'POST'])
def bars():
    bars_data = select_Bars()
    # print(bars_data)
    return render_template('bars.html', title='Bar table', bars_data=bars_data)

@Drinks.route("/barlistbeer", methods=['GET', 'POST'])
def bars_beers():
    bars_beer_data = select_Bars_Beers()
    # print(bars_data)
    return render_template('cheapest_by_beer.html', title='Bar table', bars_beer_data=bars_beer_data)

@Drinks.route("/barlistcider", methods=['GET', 'POST'])
def bars_cider():
    bars_cider_data = select_Bars_Cider()
    # print(bars_data)
    return render_template('cheapest_by_cider.html', title='Bar table', bars_cider_data=bars_cider_data)

@Drinks.route("/barlistku", methods=['GET', 'POST'])
def bars_ku():
    bars_ku_data = select_Bars_KU()
    # print(bars_data)
    return render_template('cheapest_by_ku.html', title='Bar table', bars_ku_data=bars_ku_data)

@Drinks.route("/barlistshot", methods=['GET', 'POST'])
def bars_shot():
    bars_shot_data = select_Bars_Shot()
    # print(bars_data)
    return render_template('cheapest_by_shot.html', title='Bar table', bars_shot_data=bars_shot_data)

@Drinks.route("/top5beers", methods=['GET', 'POST'])
def top_fem():
    most_sold_beers = select_top_5_sold()
    return render_template('top_bar.html', title='Most sold beers', most_sold_beers=most_sold_beers)

# @Drinks.route("/barlistshot", methods=['GET', 'POST'])
# def bars_shot():
#     bars_shot_data = select_Bars_Shot
#     # print(bars_data)
#     return render_template('cheapest_by_shot.html', title='Bar table', bars_shot_data=bars_shot_data)

# @Drinks.route("/beersearch")
# def beersearch():
#     return render_template('beersearch.html', title = 'Beers Search')
    
# @Drinks.route("/beersearch")
# def beersearch():
#     return render_template('beersearch.html', title = 'Beers Search')



