from .models import * 
from django.http import HttpResponse



def password_genrator():
    import string
    import random
    uppercase = string.ascii_uppercase
    lower_case = string.ascii_lowercase
    digits = string.digits
    password = []
    password.extend(list(uppercase))
    password.extend(list(lower_case))
    password.extend(list(digits))
    new_password = ''.join(random.sample(password,8))
    return new_password
