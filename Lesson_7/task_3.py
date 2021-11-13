class Cell:

    def __init__(self, cnt):
        self.cnt = int(cnt)

    def __add__(self, other):
        return self.cnt + other.cnt

    def __sub__(self, other):
        return self.cnt - other.cnt

    def __mul__(self, other):
        return self.cnt * other.cnt

    def __truediv__(self, other):
        return self.cnt / other.cnt

    def make_order(rows, cnt):
        return '\n'.join(['*' * rows for _ in range(cnt // rows)]) + '\n' + '*' * (cnt % rows)


cell_1 = Cell(15)
cell_2 = Cell(10)

print(cell_1 + cell_2)
print(cell_1 - cell_2)
