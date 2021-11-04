from itertools import cycle, count


def lst(start, finish=11):
    return list(range(start, finish))


data = lst(3)
print(data)


new_data = ['a', 'b', 'c', 'd', 'e', 'f']
i = 0
for el in cycle(new_data):
    i += 1
    if i > 10:
        break
    print(el)


for el in count(3):
    if el > 10:
        break
    print(el)
