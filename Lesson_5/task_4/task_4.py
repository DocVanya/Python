rus_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('task_4_new.txt', 'w', encoding='utf-8') as new_f:
    with open('task_4.txt', encoding='utf-8') as f:
        new_f.write(str([line.replace(line.split()[0], rus_dict.get(line.split()[0])) for line in f]))

