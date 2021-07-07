from classes.profile import *

adam = NewProfile('john', 'aaa', '12345678')

# logins
x = input('Login: ')
y = input('Pass: ')
tryLogin = ExistentProfile(x, y)

if tryLogin.email == adam.email:
    print('Login Aprovado!')
else:
    print('Login não encontrado')
