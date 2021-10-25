proceeds = int(input('Введите значение выручки фирмы: '))
costs = int(input('Введите значение издержек фирмы: '))
profit = proceeds - costs
profitability = profit / proceeds

if proceeds > costs:
    print(f'Вы отработали с прибылью: {profit}')
    print(f'Ваша рентабильность составляет: {profitability}')
    staff = int(input('Введите количество сотрудников фирмы: '))
    print(f'Прибыль фирмы на каждого сотрудника составляет {profit / staff}')
else:
    print(f'Вы отработали с убытком: {profit}')
