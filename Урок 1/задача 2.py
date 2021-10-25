time = int(input('Введите время в секундах: '))

hh = time // 3600
mm = (time % 3600) // 60
ss = time % 60

print(f'Время в формате чч:мм:сс - {hh:02}:{mm:02}:{ss:02}')
