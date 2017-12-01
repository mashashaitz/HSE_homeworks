from flask import Flask
from flask import url_for, render_template, request, redirect
import csv
import json
import random
import sqlite3


app = Flask(__name__)


def open_file(file_name):
    list_of_lines = []
    with open(file_name, 'r',  encoding = 'utf-8') as f:
        list_of_lines = f.read().split('\n')
    return list_of_lines


def make_json(general_answers, correct_sentences):
    dictionary = general_answers
    dictionary['sentences'] = correct_sentences
    with open('data.json', 'r', encoding='utf-8') as f:
        text = f.read()
    data = json.loads(text)
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii = False, indent = 4)
        json.dump(dictionary, f, ensure_ascii = False, indent = 4)
    return


def make_sql(general_answers, correct_sentences):
    conn = sqlite3.connect('sql_answers.db')
    cur = conn.cursor()


    answ_values = []
    for quest in open_file('general_questions.txt'):
        answ_values.append(general_answers[quest])
    
    sent_values = []
    for sent in open_file('sentences.txt'):
        sent_values.append(correct_sentences[sent])


    cur.execute('INSERT INTO answers (age, city, education, profession, language) VALUES (?, ?, ?, ?, ?)', answ_values)
    conn.commit()

    cur.execute('INSERT INTO sentences (first, second, third, fourth, fifth, sixth, seventh, eigth, nineth, tenth, eleventh, twelfth, thirteenth, fourteenth, fifteenth) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', sent_values)
    conn.commit()

    return


@app.route('/')
def index():
    sentences_list = []
    for n, phrase in enumerate(open_file('sentences.txt')):
        sentences_list.append([phrase, str(n)])
    general_questions_list = []
    for n, phrase in enumerate(open_file('general_questions.txt')):
        general_questions_list.append([phrase, str(n)])
    
    random.shuffle(sentences_list)
    return render_template('main_page.html', sentences=sentences_list, general_questions=general_questions_list)


@app.route('/json')
def json_results_presentation():
    f = open('data.json', 'r', encoding='utf-8')
    st = f.read()
    return st


@app.route('/save_results')
def save_results():
    sentences_list = open_file('sentences.txt')                                                  
    general_questions_list = open_file('general_questions.txt')

    general_answers = {}
    for n, question in enumerate(general_questions_list):
        general_answers[question] = request.args[str(n) + "_meta_information"]
        
    correct_sentences = {}
    for n, sentence in enumerate(sentences_list):
        correct_sentences[sentence] = request.args[str(n) + '_correct_sentence']

    make_json(general_answers, correct_sentences)
    make_sql(general_answers, correct_sentences)
        
    return redirect(url_for('json_results_presentation'))


@app.route('/stats')
def show_stats():
    conn = sqlite3.connect('sql_answers.db')
    cur = conn.cursor()

    tables = []

    params_1 = ['age', 'city', 'education', 'profession', 'language']
    params_2 = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eigth', 'nineth', 'tenth', 'eleventh', 'twelfth', 'thirteenth', 'fourteenth', 'fifteenth']

    for param in params_1:
        cur.execute('SELECT id, ' + str(param) + ' FROM answers')
        tables.append(['id', str(param), cur.fetchall()])
    for param in params_2:
        cur.execute('SELECT id, ' + str(param) + ' FROM sentences')
        tables.append(['id', str(param), cur.fetchall()])

    return render_template('statistics_page.html', data=tables)


@app.route('/search')
def search_info():
    return render_template('ask_form.html')
    
    
@app.route('/results')
def show_results():
    conn = sqlite3.connect('sql_answers.db')
    cur = conn.cursor()

    params = []
    if request.args['age'] != '':
        params.append('age')
    if request.args['city'] != '':
        params.append('city')
    if request.args['education'] != '':
        params.append('education')
    if request.args['profession'] != '':
        params.append('profession')
    if request.args['language'] != '':
        params.append('language')

    ids = []
    st = 'SELECT id FROM answers WHERE '
    for param in params:
        st += str(param) + ' = "' + str(request.args[str(param)]) + '" AND '
    st = st[:-5]

    cur.execute(st)
    ids = cur.fetchall()

    if ids == []:
        return redirect(url_for('search_info'))
    else:
        tables = []
        for an_id in ids:
            cur.execute('SELECT * FROM sentences WHERE id = "' + str(an_id).strip('(, )') + '"')
            tables.append(['id', "answ", str(an_id).strip('(, )'), cur.fetchall()])
        return render_template('statistics_page.html', data=tables)
    
           
if __name__ == '__main__':
    app.run(debug=True) #можно ли перезапускать файл

