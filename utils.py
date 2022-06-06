from receipt import Order
from devices import Phone, Notebook, TV
order_list = [
    Order('Cat', Phone('Xiaomi', 'Android', 'разбито стекло экрана')),
    Order('Dog', Notebook('HP', '2010', 'Windows 7', 'не загружается')),
    Order('Cat', Notebook('Acer', '2015', 'Windows 10', 'перегрев')),
    Order('Dog', TV('LG', '40', 'не включается')),
    Order('Cat', TV('Samsung', '55', 'не работает Wi-Fi')),
]

def for_check_level_2():
    print('Для проверки "вшиты" ФИО: Cat и Dog, и номера квитанций:', end=' ')
    for el in order_list:
        print(el.numb_receipt, end=' ')
    print()

# https://pythonist.ru/heshirovanie-parolej-v-python-tutorial-po-bcrypt-s-primerami/
login_pw = [
    ['login', b'$2b$12$W7WInw6ax8b.z2HiO9oeAOi7djONiUZp3/SEjV6WmBpP7vRmYdB0K', 'Vasya'],  # тут пароль password
    ['login2', b'$2b$12$EZBILSmHXjOiA1MWNSapVOIc7QFkngsxe0PogAVX5SBXZ0.KyumQ2', 'Olya'],  # тут пароль 12345
    ['login3', b'$2b$12$JEdI.LKN0K91Mvi1Lw1IqueS/ewo9bXSfpc0Z3hfqod9hoTafAxfe', 'Denis']  # тут пароль qwerty
]

# def check(s):  # проверяет, существует ли номер заказа
#     for num, order in enumerate(order_list):
#         if order.numb_receipt == s:
#             return num