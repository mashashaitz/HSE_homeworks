#Посчитайте, сколько в каждом файле слов,
#запишите эту информацию в новый текстовый файл в формате
#"название файла<табуляция>количество слов",
#для каждого файла информация на новой строчке.


punct = '\'"/.,<>:;[]{}\\|1234567890`~!@#$%^&*()_+-=?!«»…—'
import os
import re


def open_file(path):
    fi = open(path, 'r', encoding = "cp1251")
    st = fi.read()
    fi.close()
    return st


def norm_txt(st):
    st_clean = st.replace('<title>', '')
    st_clean = st_clean.replace('</title>', '\n')
    st_clean = st_clean.replace('<se>', '')
    st_clean = st_clean.replace('\n<w>', '')
    st_clean = st_clean.replace('</se>', '')
    st_clean = st_clean.replace('</w>', ' ')
    st_clean = re.sub('<ana lex=".*?"></ana>', '', st_clean)
    st_clean = re.sub('<.*>\n', '', st_clean)
    st_clean = st_clean.replace('  ', ' ')
    return st_clean


def count_words(f):
    num = 0
    st = open_file(f)
    st_clean = norm_txt(st)
    arr_word = []
    for word in st_clean.split():
        if word.strip(punct) != '':
            arr_word.append(word.strip(punct))
    num = len(arr_word)
    return num


def all_in_all():
    arr = []
    file_all = []
    path = 'news'
    for root, dirs, files in os.walk(path):
        for f in files:
            arr.append(count_words(os.path.join(root, f)))
            file_all.append(f)
    return arr, file_all


def wrt(stri):
    f = open("result.txt", 'w', encoding = "utf-8")
    f.write(stri)
    f.close()

def main():
    arr, file_all = all_in_all()
    stri = ''
    for idx, file in enumerate(file_all):
        stri += file
        stri += '\t'
        stri += str(arr[idx])
        stri += '\n'
    wrt(stri)


main()
