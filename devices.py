class Device:
    def __init__(self, model: str, problem: str):
        self.model = model
        self.problem = problem


class Notebook(Device):
    def __init__(self, model: str, year: str, os: str, problem: str):
        super().__init__(model, problem)
        self.year = year
        self.os = os

    def __str__(self):
        return f'Тип устройства: {self.__class__.__name__}\nМодель: {self.model}\
        \nГод выпуска: {self.year}\nОперационная система: {self.os}\nНеисправность: {self.problem}'

    def __repr__(self):
        return f'Тип устройства: {self.__class__.__name__}\nМодель: {self.model}\
        \nГод выпуска: {self.year}\nОперационная система: {self.os}\nНеисправность: {self.problem}'


class Phone(Device):
    def __init__(self, model: str, os: str, problem: str):
        super().__init__(model, problem)
        self.os = os

    def __str__(self):
        return f'Тип устройства: {self.__class__.__name__}\nМодель: {self.model}\
        \nОперационная система: {self.os}\nНеисправность: {self.problem}'

    def __repr__(self):
        return f'Тип устройства: {self.__class__.__name__}\nМодель: {self.model}\
        \nОперационная система: {self.os}\nНеисправность: {self.problem}'


class TV(Device):
    def __init__(self, model: str, diagonal: str, problem: str):
        super().__init__(model, problem)
        self.diagonal = diagonal

    def __str__(self):
        return f'Тип устройства: {self.__class__.__name__}\nМодель: {self.model}\
        \nДиагональ: {self.diagonal}\nНеисправность: {self.problem}'

    def __repr__(self):
        return f'Тип устройства: {self.__class__.__name__}\nМодель: {self.model}\
        \nДиагональ: {self.diagonal}\nНеисправность: {self.problem}'
