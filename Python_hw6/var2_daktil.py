# coding=utf-8
import random
# Текст должен представлять собой стихотворение на русском языке из четырёх строк без рифмы, но написанное с соблюдением одной метрической схемы, кроме трёхстопного анапеста.
# Вы́рыта да́ктилем я́ма глубо́кая

vowels = "АЕЁИОУЫЭЮЯаеёиоуыэюя"
stressed_vowels = "АЕЁИОУЫЭЮЯ"
non_stressed_vowels ="аеёиоуыэюя"

strng = ''

def word_read():
    f = open("stressed_out.txt", 'r', encoding = "utf-8")
    f2 = f.read()
    f.close()
    words = f2.split('\n')
    return words
def word_info_vowels(words):
    vowel_info = []
    for indx, word in enumerate(words):
        vowel_info.append(0)
        for letter in word:
            if letter in vowels:
                vowel_info[indx] += 1
    return vowel_info
def word_info_stresses(words):
    stress_info = []
    for indx, word in enumerate(words):
        stress_info.append(0)
        vow = 0
        for letter in word:
            if letter in vowels:
                vow += 1
                if letter in stressed_vowels:
                    stress_info[indx] = vow
    return stress_info
def strng_tv():
    t_v = 0
    for letter in strng:
        if letter in stressed_vowels:
            t_v = 0
        if letter in non_stressed_vowels:
            t_v += 1
    return t_v
def strng_tsv():
    t_s_v = 0
    for letter in strng:
        if letter in stressed_vowels:
            t_s_v += 1
    return t_s_v
def new_word_in_line(words, vowel_info, stress_info):
    global strng
    t_v = strng_tv()
    t_s_v = strng_tsv()
    if (t_v == 0) and (t_s_v == 0):
        d = 0
        while d == 0:
            n = random.randint(0, len(words) - 1)
            if (stress_info[n] == 1) and (vowel_info[n] < 4):
                strng += words[n]
                strng += " "
                d += 1
            if (stress_info[n] == 0) and (vowel_info[n] == 0):
                strng += words[n]
                strng += " "
    if (t_v == 0) and ((t_s_v == 1) or (t_s_v == 2)):
        d = 0
        while d == 0:
            n = random.randint(0, len(words) - 1)
            if (stress_info[n] == 3) and (vowel_info[n] < 6):
                strng += words[n]
                strng += " "
                d += 1
            if (stress_info[n] == 0) and (vowel_info[n] == 0):
                strng += words[n]
                strng += " "
    if (t_v == 0) and (t_s_v == 3):
        d = 0
        while d == 0:
            n = random.randint(0, len(words) - 1)
            if (stress_info[n] == 3) and (vowel_info[n] == 5):
                strng += words[n]
                strng += " "
                d += 1
            if (stress_info[n] == 0) and (vowel_info[n] == 0):
                strng += words[n]
                strng += " "
    if (t_v == 1) and ((t_s_v == 1) or (t_s_v == 2)):
        d = 0
        while d == 0:
            n = random.randint(0, len(words) - 1)
            if (stress_info[n] == 2) and (vowel_info[n] < 5):
                strng += words[n]
                strng += " "
                d += 1
            if (stress_info[n] == 0) and (vowel_info[n] == 0):
                strng += words[n]
                strng += " "
    if (t_v == 1) and (t_s_v == 3):
        d = 0
        while d == 0:
            n = random.randint(0, len(words) - 1)
            if (stress_info[n] == 2) and (vowel_info[n] == 4):
                strng += words[n]
                strng += " "
                d += 1
            if (stress_info[n] == 0) and (vowel_info[n] == 0):
                strng += words[n]
                strng += " "
    if (t_v == 2) and ((t_s_v == 1) or (t_s_v == 2)):
        d = 0
        while d == 0:
            n = random.randint(0, len(words) - 1)
            if (stress_info[n] == 1) and (vowel_info[n] < 4):
                strng += words[n]
                strng += " "
                d += 1
            if (stress_info[n] == 0) and (vowel_info[n] == 0):
                strng += words[n]
                strng += " "
    if (t_v == 2) and (t_s_v == 3):
        d = 0
        while d == 0:
            n = random.randint(0, len(words) - 1)
            if (stress_info[n] == 1) and (vowel_info[n] == 3):
                strng += words[n]
                strng += " "
                d += 1
            if (stress_info[n] == 0) and (vowel_info[n] == 0):
                strng += words[n]
                strng += " "
def create_line(words, vowel_info, stress_info):
    global strng 
    strng = ""
    for n in range(4):
        new_word_in_line(words, vowel_info, stress_info)
    new_word_in_line(words, vowel_info, stress_info)
def create_txt(words, vowel_info, stress_info):
    global strng
    for n in range(4):
        create_line(words, vowel_info, stress_info)
        print(strng.lower().capitalize())
def main():
    words = word_read()
    vowel_info = word_info_vowels(words)
    stress_info = word_info_stresses(words)
    create_txt(words, vowel_info, stress_info)
main()
