#Программа должна открывать файл с русским текстом в utf-8 и сообщать про него следующую информацию (по вариантам):
#2. во сколько раз самая короткая строка короче самой длинной
f = open('one.txt', 'r', encoding = 'utf-8')
maks = 1;
mini = 999999;
for line in f:
    words = line.split()
    if len(words) != 0:
        s = len(words) - 1 #прибавляем пробелы
        for each in words:
            s += len(each)
        if s > maks:
            maks = s
        if s < mini:
            mini = s

print(maks/mini)       
f.close()
