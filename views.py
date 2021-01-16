from datetime import datetime
import Database
from flask import abort, current_app, render_template, request
from passlib.hash import pbkdf2_sha256 as hasher
from forms import LoginForm
from flask_login import LoginManager



def home():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['your_pass']
        obje = Database.Userdb()
        cursor = obje.Check_email(email)
        if cursor:
            return render_template('login.html', message='Please Sign Up before Login!')
        if email== '' or password == '':
            return render_template('login.html', message='Please fill up the form correctly!')
        return render_template('index.html', title='Home Page')
    else:
        return render_template(
            'index.html',
            title='Home Page',
            year=datetime.now().year,
        )



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
    cures= db.get_cures()
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
    form = LoginForm()
    if form.validate_on_submit():
        email = form.data["email"]
        user = get_user(username)
        if user is not None:
            password = form.data["password"]
            if hasher.verify(password, user.password):
                login_user(user)
                flash("You have logged in.")
                next_page = request.args.get("next", url_for("home_page"))
                return redirect(next_page)
        flash("Invalid credentials.")
    return render_template("login.html", form=form)


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
    else:
        return render_template(
            'login.html',
            title='Login',
            year=datetime.now().year,
        )


def signup():
    return render_template(
        'signup.html',
        title='Sign Up',
        year=datetime.now().year,
    )


