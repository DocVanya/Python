string = input('Введите несколько слов через пробел: ')
string = string.split()
for ind, word in enumerate(string, 1):
    print(ind, word[:10])
