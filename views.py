from datetime import datetime
import Database
from flask import abort, current_app, render_template, request, url_for, redirect, session, flash
from passlib.hash import pbkdf2_sha256 as hasher
from forms import LoginForm
from flask_login import LoginManager, login_user, login_required, current_user, logout_user
from cures import Cures
from users import get_user_2
import forms

def home():
    logout_user()
    return redirect(url_for("dashboard"))

def dashboard():
    return render_template("index.html", title="Home")


def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )


def cure():
    db = current_app.config["db"]
    cures = db.get_cures()
    return render_template(
        'cure.html',
        title='Cures',
        cures = sorted(cures)
    )


def curedetails(cure_key):
    db = current_app.config["db"]
    cure = db.get_cure(cure_key)
    if cure is None:
        abort(404)
    return render_template(
        'cure-details.html',
        title='Cure Details',
        cure = cure
    )


def login():
    forms = LoginForm()
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['your_pass']
        obje = Database.Userdb()
        cursor = obje.Check_email(email)
        if cursor:
            return render_template('login.html', message='Please Sign Up before Login!')
        if email== '' or password == '':
            return render_template('login.html', message='Please fill up the form correctly!')
        cursor2 = obje.Check_existing_user(email)
        if len(cursor2) != 1:
            return render_template('login.html', message='Email or password is wrong!')
        else:
            if not hasher.verify(password, cursor2[0][1]):
                return render_template('login.html', message='Email or password is wrong!')
            else:
                user = get_user_2(cursor2[0][0], email, cursor2[0][1])
                login_user(user, remember=True)

                session['logged_in'] = True
                session['user_id'] = user.email
                
                next_page = request.args.get("next", url_for("dashboard"))
                return redirect(next_page)
    return render_template(
        'login.html',
        title='Login',
        year=datetime.now().year,
        forms = forms
    )


def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['pass']
        re_pass = request.form['re_pass']
        obje = Database.Userdb()
        cursor=obje.Check_email(email)
        if cursor == False:
            return render_template('signup.html', message='This email is already in use!')
        if email== '' or password == '' or name == '':
            return render_template('signup.html', message='Please fill up the form correctly!')
        if re_pass != password:
            return render_template('signup.html', message='Please enter the password correctly!')
        obje.User_Add(name, email, hasher.hash(password))
        return render_template('login.html', title='Login')
    return render_template(
        'signup.html',
        title='Sign Up',
        year=datetime.now().year,
    )


@login_required
def mycure():
    db = current_app.config["db"]
    cures = db.get_cures()
    return render_template(
        'my-cures.html',
        title='My Cures',
        cures = sorted(cures)
    )

@login_required
def likecure():
    db = current_app.config["db"]
    cures = db.get_cures()
    return render_template(
        'like-cures.html',
        title='Liked Cures',
        cures = sorted(cures)
    )


@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))

@login_required
def delete():
    obje=Database.Userdb()
    obje.Delete_account(current_user.email)
    return redirect(url_for("home"))

@login_required
def update():
    obje=Database.Userdb()
    obje.update(current_user.email,"yeni")
    return redirect(url_for("home"))


def curedetails():
    db = current_app.config["db"]
    cures = db.get_cures()
    return render_template(
        'cure-details.html',
        title='Cures',
        cure = sorted(cures)
    )
