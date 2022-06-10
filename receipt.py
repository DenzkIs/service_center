from datetime import datetime, timedelta
import locale
import random

locale.setlocale(locale.LC_ALL, 'ru_RU')


class Order:

    def __init__(self, numb_receipt, fio, device, status='Ремонтируется',
                 order_date=datetime.now().strftime("%H:%M:%S, %d.%m.%Y г."),
                 repair_date=(datetime.now() + timedelta(days=random.randint(1, 6))).strftime("%d.%m.%Y г.")):
        self.numb_receipt = numb_receipt
        self.device = device
        self.order_date = order_date
        self.repair_date = repair_date
        self.fio = fio
        self.status = status

    def __str__(self):
        return f'{self.numb_receipt, self.order_date, self.fio, self.device, self.status, self.repair_date}'

    def __repr__(self):
        return f'{self.numb_receipt, self.order_date, self.fio, self.device, self.status, self.repair_date}'

    def order_info(self):
        print(
            f'{"-" * 33}',
            f'Номер заказа: {self.numb_receipt}',
            f'Дата заказа: {self.order_date}',
            f'ФИО заказчика: {self.fio}',
            f'{self.device}',
            f'Статус заказа: {self.status}',
            f'Дата готовности: {self.repair_date}',
            sep='\n'
        )

    def save(self):
        return (
            self.numb_receipt,
            self.order_date,
            self.fio,
            self.status,
            self.repair_date,
            self.device.save()[0],
            self.device.save()[1],
            self.device.save()[2],
            self.device.save()[3],
            self.device.save()[4],
        )
