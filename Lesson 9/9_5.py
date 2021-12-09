class Stationary:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationary):
    def draw(self):
        print('Запуск отрисовки ручкой')


class Pencil(Stationary):
    def draw(self):
        print('Запуск отрисовки карандашом')


class Handle(Stationary):
    def draw(self):
        print('Запуск отрисовки маркером')


object_list = [Stationary('Something'), Pen('Pen'), Pencil('Pen'), Handle('Handle')]

for item in object_list:
    item.draw()


