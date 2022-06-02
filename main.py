import receipt
import devices
import utils

utils.for_check_level_2()
print('1 - Заполнить новую квитанцию.', '2 - Просмотреть информацию о квитанциях', sep='\n')
do = input('Что делаем?: ')
if do == '1':
    new_order = 'y'
    while new_order == 'y':
        fio = input('ФИО: ')
        print('1 - Телефон', '2 - Ноутбук', '3 - Телевизор', sep='\n')
        type = input('Введите номер типа изделия: ')
        model = input('Модель: ')
        problem = input('Неисправность: ')
        # Проверяю на тип изделия
        if type == '1':
            os = input('Операционная система: ')
            device = devices.Phone(model, os, problem)
            order = receipt.Order(fio, device)
            utils.order_list.append(order)
            order.order_info()
        elif type == '2':
            year = input('Год выпуска: ')
            os = input('Операционная система: ')
            device = devices.Notebook(model, year, os, problem)
            order = receipt.Order(fio, device)
            utils.order_list.append(order)
            order.order_info()
        elif type == '3':
            diagonal = input('Диагональ: ')
            device = devices.TV(model, diagonal, problem)
            order = receipt.Order(fio, device)
            utils.order_list.append(order)
            order.order_info()
        else:
            print('!!! Был выбран неверный тип устройства !!!')
        print('_' * 33)
        print('Создать новый заказ - введите "y"')
        print('Для выхода нажмите "Enter"')
        new_order = input('Заполнить еще квитанцию?: ')
elif do == '2':
    inf = input('Введите номер квитанции или ФИО заказчика: ')
    if inf.isdigit():
        for order in utils.order_list:
            if order.numb_receipt == int(inf):
                order.order_info()
    else:
        for order in utils.order_list:
            if order.fio == inf:
                order.order_info()
    print('----- Поиск окончен -----')
else:
    print('Пока можно выбрать только 1 или 2.')
