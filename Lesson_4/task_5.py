from functools import reduce

data = list(range(100, 1001, 2))
print(data)

pro = reduce(lambda x, y: x * y, data)
print(pro)
