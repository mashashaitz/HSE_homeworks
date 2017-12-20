import re
import time
from flask import Flask
from flask import url_for, render_template, request, redirect
import csv
import os
import urllib.request

app = Flask(__name__)

def find_weather():

    pages = []
    
    time.sleep(2)

    weather_st = ''
    
    page = urllib.request.urlopen('https://yandex.ru/pogoda/skopje')
    page_read = page.read().decode('utf-8')

    reg_weather = re.compile('temp__value">([0-9 +−]+).*?}}\'>([А-Яа-я ]+).*?Давление.*?value">([0-9]+).*?Влажность.*?value">([0-9%]+)')
    weather_params = reg_weather.findall(page_read)

    degree_now = weather_params[0][0]
    weather_now = weather_params[0][1]
    pressure_now = weather_params[0][2]
    humidity_now = weather_params[0][3]
    weather_st += 'В Скопье сейчас ' + str(degree_now) + '°, ' + str(weather_now).lower() + ', давление ' + str(pressure_now) + ', влажность ' + str(humidity_now)
        
    return weather_st


def create_csv_file(htmls):
    words = []
    for html in htmls:
        time.sleep(2)
        page = urllib.request.urlopen(html)
        try:
            page_read = page.read().decode('cp1251')
        except:
            page_read = page.read().decode('utf-8')
        reg_bits_of_dict= re.compile('<td class="uu">([^>^<]*?)</td><td></td><td class="uu">(.*?)</td>')
        words.append(reg_bits_of_dict.findall(page_read))

    with open('dictionary.csv', 'w', encoding='cp1251') as csvfile:
        htmlwriter = csv.writer(csvfile, delimiter='|')
        for word in words:
            for line in word:
                htmlwriter.writerow(line)
    return 

def find_all_htmls():
    
    page = urllib.request.urlopen('http://www.dorev.ru/ru-index.html')
    page_read = page.read().decode('cp1251')

    reg_pages_htmls = re.compile('&nbsp;<a class="uu" href="(.*?)">')
    pages_htmls = reg_pages_htmls.findall(page_read)

    htmls = []

    for html in pages_htmls:
        htmls.append('http://www.dorev.ru/' + html)

    return htmls


def clean_the_spans():
    lines = []
    with open('dictionary.csv', 'r', encoding='cp1251') as csvfile:
        htmlreader = csv.reader(csvfile, delimiter='|')
        for line in htmlreader:
            charasteristics = re.sub('<.*?>', '', line[1])
            charasteristics = charasteristics.replace('\'', '')
            charasteristics = charasteristics.split()[0].strip(',.!?:;\'\"')
            lines.append([line[0].lower(), charasteristics.lower()])    
    with open('dictionary.csv', 'w', encoding='cp1251') as csvfile:
        htmlwriter = csv.writer(csvfile, delimiter='|')
        for line in lines:
            htmlwriter.writerow(line)


def create_dict():
    create_csv_file(find_all_htmls())
    clean_the_spans()
    return


def find_in_dict(stemm):
    try:
        with open('dictionary.csv', 'r', encoding='cp1251') as csvfile:
            htmlreader = csv.reader(csvfile, delimiter='|')
            for line in htmlreader:
                if stemm.lower() == line[0].lower():
                    return line[1].lower()
        return 'not_found'
    except:
        with open('dictionary.csv', 'r', encoding='cp1251') as csvfile:
            htmlreader = csv.reader(csvfile, delimiter='|')
            for line in htmlreader:
                if stemm.lower() == line[0].lower():
                    return line[1].lower()
        return 'not_found'
    

def stem_the_word(word):
    with open('word.txt', 'w', encoding = "utf-8") as f:
        f.write(word)
    os.system(r"./mystem -c -i -d word.txt my_stemmed_word.txt")
    
    with open('my_stemmed_word.txt', 'r', encoding = "utf-8") as f:
        text = f.read()
        stemm = text.split('{')[1].split('=')[0]
        gramm_inf = text.split('{')[1].split('|')[0]
    return stemm, gramm_inf


def construct_new_word(word, stemm, gramm_inf, old_form, gramm_inf_next=''):
    real_word_form = ''
    if old_form != 'not_found':
        i = 0
        for letter in word:
            if (letter.lower() in 'аиёуоыеяюэ') and (i < len(old_form)):
                if old_form[i] == '&':
                    for old_letter in old_form[i:i+7]:
                        real_word_form += old_letter
                    i += 7
                elif old_form[i].lower() in 'аиёуоыеяюэ' and (i + 1 != len(old_form)):
                    real_word_form += old_form[i]
                    i += 1
                else:
                    real_word_form += letter
                    i += 1
            else:
                real_word_form += letter
                i += 1
        if (old_form[-1] == 'ъ') and (old_form.lower().startswith(real_word_form.lower())):
            real_word_form += old_form[-1]           
    else:
        real_word_form = word
    if real_word_form[-1].lower() not in 'аиёуоыеяюэъьй':
        real_word_form += 'ъ'
    with_i_letter = ''
    for i, letter in enumerate(real_word_form[:-1]):
        if letter.lower() == 'и' and real_word_form[i + 1].lower() in 'аиёуоыеяюэ':
            with_i_letter +=  '&#1110;'
        else:
            with_i_letter += letter
    with_i_letter += real_word_form[-1]
    with_cases = with_i_letter
    if ('од=пр' in gramm_inf or 'од=дат' in gramm_inf) and (',ед' in gramm_inf) and ('=S' in gramm_inf): 
         if with_i_letter[-1].lower() == 'е':
             with_cases = ''
             for letter in with_i_letter[:-1]:
                 with_cases += letter
             with_cases += '&#1123;'
    for_adj = with_cases
    if ('=S' in gramm_inf_next) and ('=A' in gramm_inf):
        if 'муж' not in gramm_inf_next:
            if with_cases.lower().endswith('&#1110;е'):
                for_adj = ''
                for letter in with_cases[:-1]:
                    for_adj += letter
                for_adj += 'я'
            elif with_cases.lower().endswith('ые'):
                for_adj = ''
                for letter in with_cases[:-1]:
                    for_adj += letter
                for_adj += 'я'
            elif with_cases.lower().endswith('&#1110;&#1123;ся'):
                for_adj = ''
                for letter in with_cases[:-9]:
                    for_adj += letter
                for_adj += 'яся'
            elif with_cases.lower().endswith('&#1110;еся'):
                for_adj = ''
                for letter in with_cases[:-3]:
                    for_adj += letter
                for_adj += 'яся'
    prepos = for_adj
    if for_adj.startswith('бес'):
        prepos = 'без'
        for letter in for_adj[3:]:
            prepos += letter
    if for_adj.startswith('черес'):
        prepos = 'через'
        for letter in for_adj[3:]:
            prepos += letter
    if for_adj.startswith('чрес'):
        prepos = 'чрез'
        for letter in for_adj[3:]:
            prepos += letter                      
    return prepos               


def create_new_phrase(phrase):
    for root, dirs, files in os.walk(os.path.abspath('.')):
        if 'dictionary' not in files:
            create_dict()
    new_phrase = phrase
    reg_words= re.compile('[А-ЯЁа-яё]+')
    words = reg_words.findall(phrase)
    stemms = []
    gramm_infs = []
    old_forms = []
    for word in words:
        stemm, gramm_inf = stem_the_word(word)
        stemms.append(stemm)
        gramm_infs.append(gramm_inf)
        if find_in_dict(word) != 'not_found':
            old_forms.append(find_in_dict(word))
        else:
            old_forms.append(find_in_dict(stemm))
    for i in range(len(words)):
        if (i + 1 != len(words)):
            new_word = construct_new_word(words[i], stemms[i], gramm_infs[i], old_forms[i], gramm_infs[i+1])
        else:
            new_word = construct_new_word(words[i], stemms[i], gramm_infs[i], old_forms[i])
        new_phrase = new_phrase.replace(words[i], new_word)

    return new_phrase


phrase = 'мост'
new_phrase = create_new_phrase(phrase)
print(new_phrase)
