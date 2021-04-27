# -*- coding: utf-8 -*-
import base64
import secrets

try:
	login = input('Введите Ваш логин:')
	password = ''.join(str(secrets.randbelow(8)) for i in range(8))
	print('Ваш пароль был создан, происходит криптошифрование Ваших данных')

	login_obj = bytes(str(login), 'UTF-8')
	login_enc = base64.standard_b64encode(login_obj)
	print ('Ваш логин: ' + str(login_enc))

	password_obj = bytes(str(password), 'UTF-8')
	password_enc = base64.standard_b64encode(password_obj)
	print ('Ваш пароль: ' + str(password_enc))


except Exception as e:
	raise e

input() 