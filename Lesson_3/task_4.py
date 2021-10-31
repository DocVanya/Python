num_1 = float(input('Введите положительное число: '))
num_2 = int(input('Введите отрицательное число: '))


def func(a, b):
    if a <= 0 or b >= 0:
        return 'Число "а" должно быть > 0 и число "b" > 0'
    else:
        result = a ** b
        print(f'Возведение числа {a} в степень {b} = {result}')


func(num_1, num_2)


def my_func(a, b):
    if a <= 0 or b >= 0:
        return 'Число "а" должно быть > 0 и число "b" > 0'
    else:
        result = 1
        for _ in range(abs(b)):
            result *= 1 / a
        print(f'Возведение числа {a} в степень {b} = {result}')


my_func(num_1, num_2)
