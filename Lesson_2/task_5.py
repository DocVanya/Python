my_list = [7, 5, 3, 3, 2]
new_number = int(input('Введите новый элемент рейтинга в виде числа: '))
i = 0

for num in my_list:
    if new_number <= num:
        i += 1
    elif new_number > num:
        break

my_list.insert(i, float(new_number))
print(my_list)
