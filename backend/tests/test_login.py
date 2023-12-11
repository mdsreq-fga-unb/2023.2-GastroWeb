import pytest

class user_admin:
    user_name = 'autorizado'
    password = '1234'

def verf_user(user_name, password):
    if len(password)<=8:
        if len(password)>=4:
            if user_name == user_admin.user_name and password == user_admin.password:
                return True
            else:
                return False
        else:
            print('Senha muito pequena')
            return False
    else:
        print('Senha maior do que o limite')
        return False


def test_verf_user():
    name = 'naoautorizado'
    password = '12345'
    assert verf_user(name, password) == False

def test_tam_maior_8():
    name = 'autorizado'
    password = '123456789'
    assert verf_user(name, password) == False

def test_tam_menor_4():
    name = 'autorizado'
    password = '123'
    assert verf_user(name, password) == False

def test_final():
    name = 'autorizado'
    password = '1234'
    assert verf_user(name, password) == True