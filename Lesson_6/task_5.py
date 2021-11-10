class Stationary:

    def __init__(self, title='Что нибудь рисуем!'):
        self.title = title

    def draw(self):
        print(f'Начинаем рисовать! {self.title}')


class Pen(Stationary):

    def draw(self):
        print(f'Начинаем рисовать Ручкой! {self.title}')


class Pencil(Stationary):

    def draw(self):
        print(f'Начинаем рисовать Карандашом! {self.title}')


class Marker(Stationary):

    def draw(self):
        print(f'Начинаем рисовать Маркером! {self.title}')


stat = Stationary()
stat.draw()

penc = Pencil()
mark = Marker()
pn = Pen()

pn.draw()
penc.draw()
mark.draw()
