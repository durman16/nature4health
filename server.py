from flask import Flask, session
from flask_login import LoginManager,current_user

from users import Users
import views
import Database
from cures import Cures
from users import get_user
import dbinit
import forms
import os


lm = LoginManager()

@lm.user_loader
def load_user(user_id):
    return get_user(user_id)

def create_app():
    app = Flask(__name__)
    app.config.from_object("settings")

    db = Database.Curedb()
    db.add_cure(Cures("SALATALIK", disease="detox"))
    db.add_cure(Cures("soğan suyu"))
    app.config["db"] = db

    app.add_url_rule("/", view_func=views.home)
    app.add_url_rule("/dashboard", view_func=views.dashboard, methods=["GET", "POST"])
    app.add_url_rule("/about", view_func=views.about)
    app.add_url_rule("/cure", view_func=views.cure)
    app.add_url_rule("/cure/<int:cure_key>", view_func=views.curedetails)
    app.add_url_rule("/signup", view_func=views.signup, methods=["GET", "POST"])
    app.add_url_rule("/login", view_func=views.login, methods=["GET", "POST"])
    app.add_url_rule("/mycure", view_func=views.mycure, methods=["GET", "POST"])
    app.add_url_rule("/likecure", view_func=views.likecure, methods=["GET", "POST"])
    app.add_url_rule("/logout", view_func=views.logout)
    app.add_url_rule("/cure-details", view_func=views.curedetails)



    SECRET_KEY = os.urandom(32)
    app.config['SECRET_KEY'] = SECRET_KEY
 
    lm.init_app(app)
    lm.login_view = "login"


    return app




if __name__ == "__main__":
    app = create_app()
    port = app.config.get("PORT", 5000)
    app.run(host="127.0.0.1", port=port)
