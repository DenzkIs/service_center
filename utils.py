order_list = []

# https://pythonist.ru/heshirovanie-parolej-v-python-tutorial-po-bcrypt-s-primerami/
# использовалось при хранении
# login_pw = [
#     ['login', b'$2b$12$W7WInw6ax8b.z2HiO9oeAOi7djONiUZp3/SEjV6WmBpP7vRmYdB0K', 'Vasya'],  # тут пароль password
#     ['login2', b'$2b$12$EZBILSmHXjOiA1MWNSapVOIc7QFkngsxe0PogAVX5SBXZ0.KyumQ2', 'Olya'],  # тут пароль 12345
#     ['login3', b'$2b$12$JEdI.LKN0K91Mvi1Lw1IqueS/ewo9bXSfpc0Z3hfqod9hoTafAxfe', 'Denis']  # тут пароль qwerty
# ]
login_pw = []
# def check(s):  # проверяет, существует ли номер заказа
#     for num, order in enumerate(order_list):
#         if order.numb_receipt == s:
#             return num

def help_pw_info():
    print('  Для справки (первого входа):')
    print('\t Логин\t|\tПароль')
    print('\t', '-' * 20)
    for key, value in {'login': 'password', 'login2': 12345, 'login3': 'qwerty'}.items():
        print(f'\t {key}\t|\t{value}')
    print('\t', '-' * 20)