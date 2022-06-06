from datetime import datetime, timedelta
import locale
import random

locale.setlocale(locale.LC_ALL, 'ru_RU')


class Order:
    numb_receipt = 100

    def __init__(self, fio, device):
        Order.numb_receipt += 1
        self.numb_receipt = Order.numb_receipt
        self.device = device
        self.order_date = datetime.now()
        self.repair_date = self.order_date + timedelta(days=random.randint(1, 6))
        self.fio = fio
        self.status = 'Ремонтируется'

    def __str__(self):
        return f'{self.numb_receipt, self.order_date, self.fio, self.device, self.status, self.repair_date}'

    def __repr__(self):
        return f'{self.numb_receipt, self.order_date.strftime("%H:%M:%S, %d.%m.%Y г."), self.fio, self.device, self.status, self.repair_date}'

    def order_info(self):
        print(
            f'{"-" * 33}',
            f'Номер заказа: {self.numb_receipt}',
            f'Дата заказа: {self.order_date.strftime("%H:%M:%S, %d.%m.%Y г.")}',
            f'ФИО заказчика: {self.fio}',
            f'{self.device}',
            f'Статус заказа: {self.status}',
            f'Дата готовности: {self.repair_date.strftime("%d.%m.%Y г.")}',
            sep='\n'
        )
