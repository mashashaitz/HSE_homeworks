#2 вариант. Многоточие должно содержать столько точек, сколько букв в слове


import random


def open_file():
    f = open("words_with_explanations.csv", 'r', encoding = "utf-8")
    arr = f.readlines()
    f.close()
    return arr


def mapish(arr):
    mp = {}
    for line in arr:
        words = line.split(";")
        mp[words[0]] = words[1].replace('\n', '')
    return mp


def game(mp):
    answ = input('Хотите сыграть - введите "да" ')
    while answ == 'да':
        word = random.choice(list(mp.keys()))
        st = ""
        for letter in mp[word]:
            st += "*"
        print(word, " ", st)
        
        t = False
        while t == False:
            guess = input("Ваша версия ")
            if guess == mp[word]:
                t = True
                print("Да!!! Ура!!!")
            else:
                print("Нет(")
        answ = input('Хотите сыграть - введите "да" ')


def main():
    arr = open_file()
    mp = mapish(arr)
    game(mp)
    
    
main()
