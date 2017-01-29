#формы глагола "найти"


import re


def open_file():
    f = open("oister.txt", 'r', encoding = "utf-8")
    st = f.read()
    f.close()
    return st


def clean(st):
    arr_dirty = st.split()
    for idx, word in enumerate(arr_dirty):
        arr_dirty[idx] = word.strip('\'"/.,<>:;[]{}\\|1234567890`~!@#$%^&*()_+-=?!«»…—').lower()
        arr = []
        for each in arr_dirty:
            if (each != ""):
                st2 = " " + each + " "
                arr.append(st2)
    return arr


def make_st(arr):
    st = ''
    for word in arr:
        if word != "":
            st += word
            st += " "
    return st


def find_find(arr):
    exp = ' на(й|ш)(т|д|е|ё|л)(и|у|е|ё|л|д|я|а|о)(т|ш|м|н)?(е|ь|н|а|о|ы|ий|ие|ая|ее)?(ый|ая|ое|ые)?(ся|сь)? '
    for word in arr:
        if re.search(exp, word):
            print(word)

def main():
    st = open_file()
    arr = clean(st)

    find_find(arr)

	
main()
