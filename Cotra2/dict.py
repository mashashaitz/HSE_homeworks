#создаем словарь


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
