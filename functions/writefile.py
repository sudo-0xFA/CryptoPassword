import os
from crypto.config.config import login
from crypto.functions.createpass import createpassword


def writeinfile():
    file = open('YourLogPass.txt', 'a+')
    file.write('\nYour login: ' + login + '\nYour password: ' + str(createpassword()))
    file.close()
    directory = os.getcwd()
    print(f'Thank you for using our program!'
          f'\nYour data is stored at {directory} in file YourLogPass.txt',
          '\nSave it in a safe place!')
