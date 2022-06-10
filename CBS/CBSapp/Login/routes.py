from flask import render_template, url_for, flash, redirect, request, Blueprint
from CBSapp import app, conn, bcrypt
from CBSapp.forms import CustomerLoginForm, EmployeeLoginForm
from flask_login import login_user, current_user, logout_user, login_required
from CBSapp.models import Customers, select_Customers, select_Employees

Login = Blueprint('Login', __name__)

posts = [{}]




@Login.route("/")
@Login.route("/home")
def home():
    return render_template('home.html', posts=posts)

# @Login.route("/beersearch")
# def beersearch():
#     return render_template('beersearch.html', title = 'Beers Search')

@Login.route("/TopBar")
def TopBar():
    return render_template('TopBar.html', title = 'Top Bar')
 
@Login.route("/about")
def about():
    return render_template('about.html', title='About')



@Login.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('Login.home'))
    is_employee = True if request.args.get('is_employee') == 'true' else False
    form = EmployeeLoginForm() if is_employee else CustomerLoginForm()
    if form.validate_on_submit():
        user = select_Employees(form.id.data) if is_employee else select_Customers(form.id.data)
        if user != None and bcrypt.check_password_hash(user[2], form.password.data):
            login_user(user, remember=form.remember.data)
            flash('Login successful.','success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('Login.home'))
        else:
            flash('Login Unsuccessful. Please check identifier and password', 'danger')
    return render_template('login.html', title='Login', is_employee=is_employee, form=form)


@Login.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('Login.home'))


@Login.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')
