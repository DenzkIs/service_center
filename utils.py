order_list = []

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
