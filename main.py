import receipt
import devices
import utils

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
        print(' - - - Введен неверный тип устройства - - - ')
    print('_' * 33)
    print('Создать новый заказ - введите "y"')
    print('Для выхода нажмите "Enter"')
    new_order = input('Продолжаем?: ')
