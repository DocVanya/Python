with open('task_2.txt', encoding='utf8') as f:
    usefulness = [f'{num}. {" ".join(line.split())} - {len(line.split())} слов' for num, line in enumerate(f, 1)]
    print(*usefulness, f'Всего строк - {len(usefulness)}', sep='\n')


# lines_n = 0
# words_n = 0
# f = open('task_2.txt', encoding='utf8')
# for line in f:
#     lines_n += 1
#     words = line.split()
#     words_n += len(words)
# f.close()
# print(f' Строк всего - {lines_n}')
# print(f' Слов всего - {words_n}')
