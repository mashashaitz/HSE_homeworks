#2. статьи о городах (напр., Санкт-Петербург) -- часовой пояс;


import re


def open_file():
    f = open("SPB.html", 'r', encoding = "utf-8")
    st = f.read()
    f.close()
    return st


def find_names(st):
    exp = '(">)(UTC)([0-9+-]*?)(</a>)'
    arr = re.findall(exp, st)
    return arr


def clean_res(arr):
    new_arr = []
    for each in arr:
        res = each[1] + each[2]
        if res not in new_arr:
            new_arr.append(res)
    return new_arr


def main():
    st = open_file()
    arr = find_names(st)
    new_arr = clean_res(arr)
    for each in new_arr:
        print(each)

	
main()
