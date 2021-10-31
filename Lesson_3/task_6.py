# string = input('Введите несколько слов с прописной первой буквой: ')
#
#
# def int_func(a):
#     print(a.title())
#
#
# int_func(string)

def int_func(word):
    latin_char = 'qwertyuiopasdfghjklzxcvbnm'
    return word.title() if not set(word).difference(latin_char) else False


words = input('Введите несколько слов латинскими буквами начиная с прописной буквы: ').split()
for w in words:
    result = int_func(w)
    if result:
        print(int_func(w), ' ')
