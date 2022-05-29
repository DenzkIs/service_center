import receipt
import devices

new_order = 'y'
while new_order == 'y':
    fio = input('ФИО: ')
    print('1 - Телефон', '2 - Ноутбук', '3 - Телевизор', sep='\n')
    type = input('Введите номер типа изделия: ')

    # Проверяю на тип изделия
    if type == '1':
        model = input('Модель: ')
        os = input('Операционная система: ')
        problem = input('Неисправность: ')
        d = devices.Phone(model, os, problem)  # создаю объект класса Phone, передаю полученные данные
        o = receipt.Order(fio, d.info())  # передаю в Order инфу об устройстве в виде словаря d.info()
        o.print_info()  # вывожу в консоль информацию с квитанции
    elif type == '2':
        model = input('Модель: ')
        year = input('Год выпуска: ')
        os = input('Операционная система: ')
        problem = input('Неисправность: ')
        d = devices.Notebook(model, year, os, problem)  # создаю объект класса Notebook, передаю полученные данные
        o = receipt.Order(fio, d.info())  # передаю в Order инфу об устройстве в виде словаря d.info()
        o.print_info()
    elif type == '3':
        model = input('Модель: ')
        diagonal = input('Диагональ: ')
        problem = input('Неисправность: ')
        d = devices.TV(model, diagonal, problem)  # создаю объект класса TV, передаю полученные данные
        o = receipt.Order(fio, d.info())  # передаю в Order инфу об устройстве в виде словаря d.info()
        o.print_info()
    else:
        print(' - - - Введен неверный тип устройства - - - ')
    print('_' * 33)
    print('Чтобы создать новый заказ введите "y"')
    print('Для выхода нажмите "Enter"')
    new_order = input('Продолжаем?: ').lower()
