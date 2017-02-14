#все вхождения прилагательных во множественном числе
#(то есть таких разборов, в которых type=" начинается с "l" и содержит "f" на третьей позиции, например: type="lhfosf").
#Результат подсчётов напечатать в другой открытый для записи файл таким образом, чтобы каждая пара "разбор - число вхождений" располагалась на одной строке.
#Преобразуйте содержимое корпуса в формат csv. Возьмите строки внутри тэга <body> и очистите их от тэгов при помощи re.sub. Запишите результат в новый файл следующим образом:
#на одной строке должны находиться лемма, разбор, словоформа, разделенные запятыми


import re


def open_file():
    f = open("isl.xml", 'r', encoding = "utf-8")
    st = f.read()
    f.close()
    return st


#<w lemma="frekur" type="lvfovm">frekari</w>
def create_dic(st):
    dic = {}
    reg = '(<w lemma=")(.*?)(" type=")(.*?)(">)(.*?)(</w>)'
    m = re.findall(reg, st)
    for exp in m:
        if exp[3] in dic:
            dic[exp[3]] += 1
        else:
            dic[exp[3]] = 1
    return dic


def wrt(dic):
    f = open('new.txt', 'w')
    for each in dic:
        f.write(each)
    f.close()


def main():
    st = open_file()
    dic = create_dic(st)
    wrt(dic)

	
main()
