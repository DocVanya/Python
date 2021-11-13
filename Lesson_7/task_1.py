a = [[1, 1, 1, 4], [7, 0, 2, 0], [5, 9, 6, 8], [7, 7, 5, 5]]
b = [[0, 9, 0, 2], [7, 7, 5, 1], [3, 1, 4, 3], [5, 8, 2, 5]]


class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return '\n'.join(map(str, self.lists))

    def __add__(self, other):
        c = []
        for i in range(len(self.lists)):
            c.append([])
            for j in range(len(self.lists)):
                c[i].append(self.lists[i][j] + other.lists[i][j])
        return '\n'.join(map(str, c))


matrix_1 = Matrix(a)
matrix_2 = Matrix(b)

print(matrix_1, '\n')
print(matrix_2, '\n')
print(matrix_1 + matrix_2)
