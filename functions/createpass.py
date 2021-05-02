import secrets
import string
from crypto.config.config import login


def createpassword():
    symbols = '!@#$%^&*'
    alphabet = string.ascii_letters + string.digits + login + symbols
    password = ''.join(secrets.choice(alphabet) for _ in range(32))
    return password
