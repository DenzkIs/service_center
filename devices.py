class Device:
    def __init__(self, model: str, problem: str):
        self.model = model
        self.problem = problem


class Notebook(Device):
    def __init__(self, model, year, os, problem):
        super().__init__(model, problem)
        self.year = year
        self.os = os

    def info(self):  # возвращает словарь с информацией об устройстве
        return {
            'Тип устройства': self.__class__.__name__,
            'Модель': self.model,
            'Год выпуска': self.year,
            'Операционная система': self.os,
            'Неисправность': self.problem
        }


class Phone(Device):
    def __init__(self, model, os, problem):
        super().__init__(model, problem)
        self.os = os

    def info(self):
        return {
            'Тип устройства': self.__class__.__name__,
            'Модель': self.model,
            'Операционная система': self.os,
            'Неисправность': self.problem
        }


class TV(Device):
    def __init__(self, model, diagonal, problem):
        super().__init__(model, problem)
        self.diagonal = diagonal

    def info(self):
        return {
            'Тип устройства': self.__class__.__name__,
            'Модель': self.model,
            'Диагональ экрана': self.diagonal,
            'Неисправность': self.problem
        }
