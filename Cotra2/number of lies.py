#считаем строчки в файле


import re


def open_file():
    f = open("isl.xml", 'r', encoding = "utf-8")
    st = f.read()
    f.close()
    return st


def count_lines(st):
    n = 0
    for each in st:
        if (each == "\n"):
            n += 1
    return n + 1 #все концы строчек + первая (сплитлайнзом считает только непустые)


def wrt(n):
    f = open('new.txt', 'w')
    f.write(str(n) + '\n')
    f.close()


def main():
    st = open_file()
    n = count_lines(st)
    wrt(n)

	
main()
