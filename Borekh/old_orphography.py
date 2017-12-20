import urllib.request
import re
import time
from flask import Flask
from flask import url_for, render_template, request, redirect
import csv
import os

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
    span = prepos
    span = span.replace(';', ';</span>')
    span = span.replace('&', '<span>&')
    return span               


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


def find_news():
    
    time.sleep(2)

    page = urllib.request.urlopen('https://lenta.ru/')
    page_read = page.read().decode('utf-8')

    reg_news = re.compile('[А-ЯЁа-яё]+')
    news = reg_news.findall(page_read)

    how_often_news = {}
    for new in news:
        if new.lower() not in how_often_news:
            how_often_news[new.lower()] = 1
        else:
            how_often_news[new.lower()] += 1

    max_quantity = [0]*10
    first_ten = ['']*10

    for new in how_often_news:
        i = 0
        while i < 10:
            if max_quantity[i] < how_often_news[new]:
                max_quantity[i] = how_often_news[new]
                first_ten[i] = new
                i += 10
            i += 1
    first_ten

    return first_ten, max_quantity, how_often_news.keys()


@app.route('/')
def index():
    return render_template('main_page.html', weather_st=find_weather())

@app.route('/get_a_word')
def word_into_old():
    phrase = request.args['the_word']
    new_phrase = create_new_phrase(phrase)
    return render_template('word_page.html', weather_st=find_weather(), old_word=new_phrase)


@app.route('/get_the_text')
def make_news_old():
    first_ten, max_quantity, how_often_news = find_news()
    old_news = []
    for new in how_often_news:
        old_news.append(create_new_phrase(new))
    most_common_words = 'Самые частотные слова - '
    for i in range(10):
        most_common_words += first_ten[i] + ' ' + str(max_quantity[i]) + ', '
    most_common_words = most_common_words[:-2]
    most_common_words += '.'
    return render_template('text_page.html', most_common_words=most_common_words, news = old_news)


@app.route('/get_the_test')
def create_a_test():
    questions = []
    with open('test_questions.csv', 'r', encoding='utf-8') as csvfile:
        htmlreader = csv.reader(csvfile, delimiter='|')
        for line in htmlreader:
            questions.append(line)
    return render_template('test_page.html', weather_st=find_weather(), questions=questions)


@app.route('/test_result')
def get_test_results():
    questions = []
    with open('test_questions.csv', 'r', encoding='utf-8') as csvfile:
        htmlreader = csv.reader(csvfile, delimiter='|')
        for line in htmlreader:
            questions.append(line)
    result = 0
    for question in questions:
        if request.args[question[1]] == question[2]:
            result += 1
    results = str(result) + ' из 10'
    return render_template('test_results_page.html', weather_st=find_weather(), results=results)


if __name__ == '__main__':
    app.run(debug=True) #можно ли перезапускать файл
