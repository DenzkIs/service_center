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