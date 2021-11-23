class DivisionError(Exception):

    def __init__(self, text):
        self.text = text


num_1 = int(input('Введите число: '))
num_2 = int(input('Введите число: '))


def div(a, b):
    try:
        if b == 0:
            raise DivisionError('Деление на ноль!')
        print(a / b)
    except DivisionError as err:
        print(err)


div(num_1, num_2)


# class DivisionByZeroException(Exception):
#     def __init__(self, *args: object) -> None:
#          super().__init__('На 0 делить нельзя!')
#
# def div(value1: int, value2: int) -> float:
#     if value2 == 0:
#         raise DivisionByZeroException()
#     return value1 / value2
#
# while (i := input('Введите делитель для 100: ')) != '':
#     try:
#         print(f'Результат: {div(100, int(i))}')
#     except DivisionByZeroException as e:
#         print(e)
#     except ValueError:
#         pass
