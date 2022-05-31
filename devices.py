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
        return f'{self.__class__.__name__, self.model, self.problem, self.year, self.os}'


class Phone(Device):
    def __init__(self, model: str, os: str, problem: str):
        super().__init__(model, problem)
        self.os = os

    def __str__(self):
        return f'{self.__class__.__name__, self.model, self.problem, self.os}'


class TV(Device):
    def __init__(self, model: str, diagonal: str, problem: str):
        super().__init__(model, problem)
        self.diagonal = diagonal

    def __str__(self):
        return f'{self.__class__.__name__, self.model, self.problem, self.diagonal}'
