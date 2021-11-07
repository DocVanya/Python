with open('task_1.txt', 'w', encoding='utf-8') as f:
    while True:
        line = input('Введите данные или нажмите Enter для выхода: ')
        if not line:
            break
        f.write(f'{line}\n')

# with open('task_1.txt', encoding='utf-8') as f:
#     print(f.read())