class Worker:

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income['wage']


class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)
        self._bonus = income['bonus']

    def get_full_name(self):
        return f'Полное имя сотрудника: {self.name} {self.surname}\n'

    def get_total_income(self):
        return f'Сумма оклада: {self._income + self._bonus}\n'


info_dict = {'wage': 5000, 'bonus': 1000}
worker = Position('Владимир', 'Иванов', 'Менеджер табуретки', info_dict)

print(worker.get_full_name(), worker.get_total_income())