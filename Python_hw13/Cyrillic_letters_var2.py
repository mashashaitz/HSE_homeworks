#сколько в дереве папок с полностью кириллическими названиями
#Программа должна обходить всё дерево папок,
#начинающееся с той папки, где она находится

import os

cyrillic_symbols = '\'"/.,<>:;[]{}\\|1234567890` ~!@#$%^&*()_+-=?!«»…—йцукенгшщзхъёфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРРОЛДЖЭЯЧСМИТЬБЮ'


def go_around():
    q = 0
    for root, dirs, files in os.walk('.'):
        for d in dirs:
            T = 0
            for letter in d:
                if letter not in cyrillic_symbols:
                    T += 1
            if T == 0:
                q += 1
    print(q)


def main():
    go_around()


main()
