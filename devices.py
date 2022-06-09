class Device:
    def __init__(self, model: str, problem: str):
        self.model = model
        self.problem = problem


class Notebook(Device):
    def __init__(self, model: str, year: str, os: str, problem: str, type='Ноутбук'):
        super().__init__(model, problem)
        self.type = type
        self.year = year
        self.os = os

    def __str__(self):
        return f'Тип устройства: {self.type}\nМодель: {self.model}\
        \nГод выпуска: {self.year}\nОперационная система: {self.os}\nНеисправность: {self.problem}'

    def __repr__(self):
        return f'Тип устройства: {self.type}\nМодель: {self.model}\
        \nГод выпуска: {self.year}\nОперационная система: {self.os}\nНеисправность: {self.problem}'

    def save(self):
        return self.type, self.model, self.year, self.os, self.problem


class Phone(Device):
    def __init__(self, model: str, os: str, problem: str, type='Телефон'):
        super().__init__(model, problem)
        self.os = os
        self.type = type

    def __str__(self):
        return f'Тип устройства: {self.type}\nМодель: {self.model}\
        \nОперационная система: {self.os}\nНеисправность: {self.problem}'

    def __repr__(self):
        return f'Тип устройства: {self.type}\nМодель: {self.model}\
        \nОперационная система: {self.os}\nНеисправность: {self.problem}'

    def save(self):
        return self.type, self.model, self.os, self.problem, ''


class TV(Device):
    def __init__(self, model: str, diagonal: str, problem: str, type='Телевизор'):
        super().__init__(model, problem)
        self.diagonal = diagonal
        self.type = type

    def __str__(self):
        return f'Тип устройства: {self.type}\nМодель: {self.model}\
        \nДиагональ: {self.diagonal}"\nНеисправность: {self.problem}'

    def __repr__(self):
        return f'Тип устройства: {self.type}\nМодель: {self.model}\
        \nДиагональ: {self.diagonal}"\nНеисправность: {self.problem}'

    def save(self):
        return self.type, self.model, self.diagonal, self.problem, ''
