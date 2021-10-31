data = ['name', 'surname', 'year_birthday', 'city', 'email', 'phone_num']


def func(params):
    for i in range(0, len(params)):
        data[i] = input(f'Введите ваш {data[i]}: ')
    print(' '.join(data))


func(data)
