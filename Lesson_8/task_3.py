class OwnError(Exception):
    def __init__(self, text):
        self.text = text


data = []
while True:
    int_data = input('Введите число или stop для выхода: ')

    if int_data == 'stop':
        break

    try:
        if not int_data.isdigit():
            raise OwnError(f'Вы ввели не число - {int_data}')
        else:
            data.append(int(int_data))
    except OwnError as err:
        print(err)

print(f'Ваш список - {data}')
