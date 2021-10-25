while True:
    days = 1
    start_km = float(input('Начальный результат: '))
    last_km = float(input('Финальный результат: '))
    if start_km <= 0 or last_km <= 0:
        print('Данные должны быть > 0')
    else:
        while start_km < last_km:
            start_km *= 1.1
            days += 1
        print(f'Спортсмен добьется результата за {days} дней')


#  я пытался по разному как придумал, ниже часть этого
# a = int(input('a: '))
# b = int(input('b: '))
# day = 1
# c = a
# while True:
#     print(f'{day}-й день: {c} км')
#     c = a + (a * 0.1)
#     c = c + (c * 0.1)
#     day += 1
#     if c > b:
#         break
# print(f'на {day}-й день спортсмен достиг результата - не менее {b} км')