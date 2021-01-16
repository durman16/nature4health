from flask import current_app
from flask_login import UserMixin

class Users:
    def __init__(self, name, surname, password):
        self.name = name
        self.email = email
        self.password = password
        self.active = True
        self.is_admin = False

    def get_id(self):
        return self.name

    @property
    def is_active(self):
        return self.active


def get_user(user_id):
    password = current_app.config["PASSWORDS"].get(user_id)
    user = User(user_id, password) if password else None
    if user is not None:
        user.is_admin = user.username in current_app.config["ADMIN_USERS"]
    return user