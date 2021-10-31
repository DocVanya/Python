a = int(input('Введите число: '))
b = int(input('Введите число: '))
c = int(input('Введите число: '))


# def my_func(num_1, num_2, num_3):
#     my_list = [num_1, num_2, num_3]
#     my_list.remove(min(my_list))
#     return sum(my_list)

def my_func(num_1, num_2, num_3):
    my_list = [num_1, num_2, num_3]
    return sum(sorted(my_list)[1:])


print(my_func(a, b, c))
