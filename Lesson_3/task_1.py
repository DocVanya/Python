num_1 = int(input('Введите число: '))
num_2 = int(input('Введите число: '))


def func(a, b):
    if b == 0:
        print('Делить на ноль нельзя!')
    else:
        result = a / b
        return print(result)


func(num_1, num_2)
