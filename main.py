import receipt
import devices
import utils
from datetime import datetime
import bcrypt
import csv

with open('receipts.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter='*')
    for row in reader:
        if row[5] == 'Телефон':
            utils.order_list.append(
                receipt.Order(int(row[0]), row[2], devices.Phone(row[6], row[7], row[8], type=row[5]),
                              order_date=row[1], status=row[3], repair_date=row[4]))
        elif row[5] == 'Телевизор':
            utils.order_list.append(
                receipt.Order(int(row[0]), row[2], devices.TV(row[6], row[7], row[8], type=row[5]), order_date=row[1],
                              status=row[3], repair_date=row[4]))
        elif row[5] == 'Ноутбук':
            utils.order_list.append(
                receipt.Order(int(row[0]), row[2], devices.Notebook(row[6], row[7], row[8], row[9], type=row[5]),
                              order_date=row[1], status=row[3], repair_date=row[4]))

repeat_again = 'y'
while repeat_again == 'y':
    print('1 - Новая квитанцию', '2 - Информация о квитанциях', '3 - Вход администратора', sep='\n')
    do = input('Что делаем?: ')
    if do == '1':
        next_order_number = utils.order_list[-1].numb_receipt + 1  # контроль нумерации квитанций
        fio = input('ФИО: ')
        print('1 - Телефон', '2 - Ноутбук', '3 - Телевизор', sep='\n')
        type = input('Введите номер типа изделия: ')
        model = input('Модель: ')
        problem = input('Неисправность: ')
        if type == '1':
            os = input('Операционная система: ')
            device = devices.Phone(model, os, problem)
            order = receipt.Order(next_order_number, fio, device)
            utils.order_list.append(order)
            order.order_info()
        elif type == '2':
            year = input('Год выпуска: ')
            os = input('Операционная система: ')
            device = devices.Notebook(model, year, os, problem)
            order = receipt.Order(next_order_number, fio, device)
            utils.order_list.append(order)
            order.order_info()
        elif type == '3':
            diagonal = input('Диагональ: ')
            device = devices.TV(model, diagonal, problem)
            order = receipt.Order(next_order_number, fio, device)
            utils.order_list.append(order)
            order.order_info()
        else:
            print('!!! Был выбран неверный тип устройства !!!')
        print('_' * 33)

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
    elif do == '3':
        utils.help_pw_info()  # функция-подсказка логинов и паролей
        # читаю инфу об админах, только при входе в Админ. режим
        with open('admins.csv', 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter='*')
            for a, b, c in reader:
                utils.login_pw.append([a, bytes(b, encoding='utf-8'), c])
        #print(utils.login_pw)
        authorization = ''
        login = input('Логин: ')
        pw = input('Пароль: ')
        for i in utils.login_pw:
            if login == i[0] and bcrypt.checkpw(pw.encode(), i[1]):
                authorization = i[2]
        if authorization:
            print(f'{authorization}, Вы находитесь в администраторской панели.')
            admin_mode = 'y'
            while admin_mode == 'y':
                print('-' * 30)
                print(
                    '1 - Посмотреть список админов',
                    '2 - Удалить админа',
                    '3 - Добавить нового админа',
                    '4 - Квитанции',
                    '5 - Выход из админ. панели',
                    sep='\n'
                )
                print('-' * 30)
                mode = input('Что делаем?: ')
                if mode == '1':
                    for num, name in enumerate(utils.login_pw):
                        print(f'({num + 1}) {name[2]}', end=' | ')
                    print()
                elif mode == '2':
                    delete = input('Введите ФИО удаляемого админа или его номер из списка админов: ')
                    delete_number = None
                    if delete.isdigit():
                        delete_name = ''
                        for num, name in enumerate(utils.login_pw):
                            if num == int(delete) - 1:
                                delete_number = num
                                delete_name = name[2]
                        if delete_number is not None:
                            # тут я попался при попытке удалить Админа с 0 индексом используя "if delete_number:"
                            # но это может пригодиться, чтобы нельзя было удалить первого (нулевого) админа
                            utils.login_pw.pop(delete_number)
                            print(f'Админ {delete_name} успешно удален!')
                    else:
                        for num, name in enumerate(utils.login_pw):
                            if name[2] == delete:
                                delete_number = num
                        if delete_number is not None:
                            utils.login_pw.pop(delete_number)
                            print(f'Админ {delete} успешно удален!')
                        else:
                            print('Вы ввели неверное ФИО админа')
                elif mode == '3':
                    new_admin = input('Введите имя нового админа: ')
                    new_login = input('Введите логин: ')
                    new_pw = input('Введите пароль: ')
                    new_admin_check = ''
                    new_login_check = ''
                    for i in utils.login_pw:
                        if i[2] == new_admin:
                            new_admin_check = new_admin
                        if i[0] == new_login:
                            new_login_check = new_login
                    if new_admin_check:
                        print('Админ с таким же ФИО уже зарегистрирован!')
                    if new_login_check:
                        print('Данный логин занят!')
                    if not new_admin_check and not new_login_check:
                        hash_pw = bcrypt.hashpw(new_pw.encode(), bcrypt.gensalt())
                        utils.login_pw.append([new_login, hash_pw, new_admin])
                        print(f'Новый администратор {new_admin} успешно зарегистрирован!')
                        # print(utils.login_pw)
                elif mode == '4':
                    print('__________ Меню работы с квитанциями __________')
                    order_change_mode = 'y'
                    while order_change_mode == 'y':
                        order_inpt = input('Введите номер квитанции (1 - вернуться назад): ')
                        if order_inpt == '1':
                            order_change_mode = ''
                        elif order_inpt.isdigit():
                            order_num = None
                            for num, order in enumerate(utils.order_list):
                                if order.numb_receipt == int(order_inpt):
                                    order_num = num
                            if order_num is not None:
                                print('-' * 30)
                                print(
                                    '1 - Изменить статус ремонта',
                                    '2 - Изменить дату выполнения ремонта',
                                    '3 - Информация о квитанции',
                                    '4 - вернуться назад',
                                    sep='\n'
                                )
                                print('-' * 30)
                                mode4 = input('Что делаем?: ')
                                if mode4 == '1':
                                    print('1 - Ремонтируется', '2 - Готово', '3 - Выдано клиенту', sep='\n')
                                    status_number = input('Введите номер статуса заказа или введите новый статус: ')
                                    if status_number == '1':
                                        utils.order_list[order_num].status = 'Ремонтируется'
                                    elif status_number == '2':
                                        utils.order_list[order_num].status = 'Готово'
                                    elif status_number == '3':
                                        utils.order_list[order_num].status = 'Выдано клиенту'
                                    else:
                                        utils.order_list[order_num].status = status_number
                                if mode4 == '2':
                                    print('-' * 30)
                                    print('1 - Установить текущую дату', '2 - Установить другую дату', sep='\n')
                                    print('-' * 30)
                                    mode42 = input('Что делаем?: ')
                                    if mode42 == '1':
                                        utils.order_list[order_num].repair_date = datetime.now().strftime("%d.%m.%Y г.")
                                        print(
                                            f'Дата выполнения заказа №{utils.order_list[order_num].numb_receipt} изменена на {utils.order_list[order_num].repair_date}')

                                    elif mode42 == '2':
                                        # из-за наличия метода strftime при выводе квитанций приходиться писать код ниже
                                        day = input('Введите день: ')
                                        month = input('Введите месяц: ')
                                        year = input('Введите год: ')
                                        if day.isdigit() and month.isdigit() and year.isdigit():
                                            try:
                                                utils.order_list[order_num].repair_date = datetime(int(year),
                                                                                                   int(month),
                                                                                                   int(day)).strftime(
                                                    "%d.%m.%Y г.")
                                                print(
                                                    f'Дата выполнения заказа №{utils.order_list[order_num].numb_receipt} изменена на {utils.order_list[order_num].repair_date}')
                                            except ValueError:
                                                print('Вы ввели несуществующую дату! Попробуйте снова.')
                                        else:
                                            print('Дата может состоять только из цифр!')

                                if mode4 == '3':
                                    utils.order_list[order_num].order_info()
                                if mode4 == '4':
                                    print('Вы вышли из меню работы с квитанциями.')
                                    order_change_mode = ''
                            else:
                                print('Данная кватанция не найдена!')
                        else:
                            print('Номер квитанции содержит только цифры!')
                elif mode == '5':
                    print('Вы вышли из администраторской панели.')
                    admin_mode = ''

                    with open('admins.csv', 'w', newline='', encoding='utf-8') as f:
                        writer = csv.writer(f, delimiter='*')
                        for a, b, c in utils.login_pw:
                            # decode использую, так как не могу хранить в csv байтовую строку без кавычек
                            writer.writerow([a, b.decode('utf-8'), c])
                    utils.login_pw = []  # очищаю список, так как при повторном входе в админку он заполнится дубликатами
                else:
                    print('Неверный ввод. Выберите пункт от 1 до 7.')
        else:
            print('Неверный логин или пароль')
    else:
        print('Пока можно выбрать только 1, 2 или 3.')
    repeat_again = input('Вернуться в главное меню - "y", выход - "n": ')

with open('receipts.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter='*')
    for i in utils.order_list:
        writer.writerow(i.save())
