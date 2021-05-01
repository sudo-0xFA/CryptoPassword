# -*- coding: utf-8 -*-
import os
import secrets
import string

print('Hello! This program is for creating cryptographic passwords.')

try:
    login = str(input('Write your login: \n>'))
    symbols = '!@#$%^&*'
    alphabet = string.ascii_letters + string.digits + login + symbols
    password = ''.join(secrets.choice(alphabet) for i in range(32))
except Exception as e:
    raise e

file = open('YourLogPass.txt', 'a+')
file.write('\nYour login: ' + login + '\nYour password: ' + password)
file.close()

directory = os.getcwd()
print(f'Thank you for using our program!'
      f'\nYour data is stored at {directory} in file YourLogPass.txt',
      '\nSave it in a safe place!')
