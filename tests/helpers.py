import random
import string


def helper_name():
    random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    return random_name


def helper_password():
    random_password = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    return random_password


def helper_email():
    random_email = ''.join(random.choices(string.ascii_letters + string.digits, k=6)) + '@gmail.com'
    return random_email


def helper_wrong_password():
    random_wrong_password = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    return random_wrong_password
