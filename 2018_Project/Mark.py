from flask import Flask
from flask import request
from flask import render_template
from random import choice
import re
from random import uniform
from collections import defaultdict

r_alphabet = re.compile(u'[а-яА-ЯЁё0-9-]+|[.,:;?!]+')


def gen_lines(corpus):
    data = open(corpus, 'r', encoding = 'utf-8')
    for line in data:
        yield line.lower()


def gen_tokens(lines):
    for line in lines:
        for token in r_alphabet.findall(line):
            yield token


def is_capital(corpus, word):
    data = open(corpus, 'r', encoding = 'utf-8')
    for line in data:
        for token in r_alphabet.findall(line):
            if token == word:
                return False
    return True


def find_a_pair(word):
    data = open('old_testament.txt', 'r', encoding = 'utf-8')
    for line in data:
        for n, token in enumerate(r_alphabet.findall(line.lower())):
                if token == word:
                    return r_alphabet.findall(line.lower())[n+1]


def gen_trigrams(tokens):
    t0, t1 = '$', '$'
    for t2 in tokens:
        yield t0, t1, t2
        if t2 in '.!?':
            yield t1, t2, '$'
            yield t2, '$','$'
            t0, t1 = '$', '$'
        else:
            t0, t1 = t1, t2


def train(corpus):
    lines = gen_lines(corpus)
    tokens = gen_tokens(lines)
    trigrams = gen_trigrams(tokens)

    bi, tri = defaultdict(lambda: 0.0), defaultdict(lambda: 0.0)

    for t0, t1, t2 in trigrams:
        bi[t0, t1] += 1
        tri[t0, t1, t2] += 1

    model = {}
    for (t0, t1, t2), freq in tri.items():
        if (t0, t1) in model:
            model[t0, t1].append((t2, freq/bi[t0, t1]))
        else:
            model[t0, t1] = [(t2, freq/bi[t0, t1])]
            print(t0, t1)
    return model


def unirand(seq):
    sum_, freq_ = 0, 0
    for item, freq in seq:
        sum_ += freq
    rnd = uniform(0, sum_)
    for token, freq in seq:
        freq_ += freq
        if rnd < freq_:
            return token

        
def generate_sentence(model, word):
    phrase = ''
    t0, t1 = '$', word
    while 1:
        if t1 == '$': break
        elif t0 == '$':
            phrase += t1.capitalize()
        elif t1 in ('.!?,;:'):
            phrase += t1
        else:
            if is_capital('old_testament.txt', t1):
                phrase += ' ' + t1.capitalize()
            else:
                phrase += ' ' + t1
        try:
            t0, t1 = t1, unirand(model[t0, t1])
        except KeyError:
            t0, t1 = t1, find_a_pair(t1)
    return phrase


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main_page.html')


@app.route('/get_a_word')
def create_new_phrase():
    if request.args['the_word'] != '' and request.args['the_word'] != ' ':
        word = request.args['the_word'].split()[-1].lower().strip()
    else:
        return render_template('error.html')
    model = train('old_testament.txt')
    try:
        return render_template('result_page.html', sentence=generate_sentence(model, word))
    except KeyError:
        return render_template('error.html')


if __name__ == '__main__':
    import os
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
