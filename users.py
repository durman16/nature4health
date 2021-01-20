from flask import current_app
from flask_login import UserMixin

class Users(UserMixin):
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.active = True
        self.is_admin = False

    def get_id(self):
        return self.email

    @property
    def is_active(self):
        return self.active
    
    @property   
    def is_authenticated(self):    
        return True


def get_user(user_id):
    name = ""
    password = 0
    user = Users(name, user_id, password)
    return user

def get_user_2(name, email, Password):
    password = Password
    user = Users(name, email, password)
    return user