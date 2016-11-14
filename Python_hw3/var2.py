#Программа должна спрашивать у пользователя слова до тех пор, пока он не введёт пустое слово. После этого программа должна вывести на экран те из введённых слов, длина которых больше 5 символов (каждое слово на отдельной строчке).
words = []
while 4 < 5:
    smth = input('put a word here, to stop putting words press enter ')
    
    if smth == "":
        break
    elif len(smth) > 5:
        words.append(smth)

for digit in range(len(words)):
    print(words[digit])
        