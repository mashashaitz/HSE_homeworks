# Создайте csv-таблицу с полями
#"Название файла", "Автор", "Дата создания текста", 

import os
import re


def open_file(path):
    fi = open(path, 'r', encoding = "cp1251")
    st = fi.read()
    fi.close()
    return st


def find_auth(f):
    try:
        auth_arr = re.search('<title>(\w+)\..*//.*</title>', r).group(1)
    except Exception:
        auth_arr = []
    auth = ''
    for l in auth_arr:
        auth += l
    return auth


def find_date(f):
    try:
        date_arr = re.search('<title>.*//.*, ([0-9.]*)</title>', r).group(1)
    except Exception:
        date_arr = []
    date = ''
    for l in date_arr:
        date += l
    return date


def all_in_all():
    auth = []
    date = []
    file_all = []
    path = 'news'
    for root, dirs, files in os.walk(path):
        for f in files:
            file_all.append(f)
            auth.append(find_auth(f))
            date.append(find_date(f))           
    return auth, date, file_all


def wrt(stri):
    f = open("result.csv", 'w', encoding = "utf-8")
    f.write(stri)
    f.close()

def main():
    auth, date, file_all = all_in_all()
    stri = ''
    for idx, file in enumerate(file_all):
        stri += file
        stri += ','
        stri += auth[idx]
        stri += ','
        stri += date[idx]
        stri += '\n'
    wrt(stri)

main()
