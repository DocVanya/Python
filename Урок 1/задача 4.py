user_num = int(input('Введите целое положительное число: '))
maximum = user_num % 10
num = user_num

while num > 0:
    digit = num % 10
    if digit > maximum:
        maximum = digit
    if digit == 9:
        break
    num = num // 10
    # print(num)
print(f'Cамая большая цифра в числе {user_num} будет {maximum}')
