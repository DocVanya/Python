data = []
while len(data) != 5:
    data.append(input('Введите данные для списка: '))
print(data)

for i in range(1, len(data), 2):
    data[i], data[i - 1] = data[i - 1], data[i]
print(data)

