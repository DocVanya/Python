my_dict = {}
with open('task_6.txt', encoding='utf-8') as f:
    for line in f:
        name, stats = line.split(':')
        elems = [i for i in stats if i == ' ' or ('0' <= i <= '9')]
        print(elems)
        name_sum = sum(map(int, ''.join(elems).split()))
        my_dict[name] = name_sum
print(f'{my_dict}')

# import re
# pattern = re.compile('[0-9]+')
# with open('task_6.txt', encoding='utf-8') as f:
#     for line in f:
#         print(re.findall(pattern, line))



