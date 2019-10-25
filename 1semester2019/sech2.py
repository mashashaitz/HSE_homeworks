import csv
import math
import numpy as np
import copy
from scipy.sparse import csr_matrix
from gensim.models import Word2Vec, KeyedVectors
import pandas as pd
import spacy
from tqdm import tqdm
import os
import re
import time
import pickle
import tensorflow_hub as hub
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
from pymystem3 import Mystem
m = Mystem()
from flask import Flask
from flask import request
from flask import render_template
from random import choice
import logging
logging._warn_preinit_stderr = 0
logging.warning('Worrying Stuff')


logging.basicConfig(filename="mySnake.log", level=logging.INFO)

logging.debug("This is a debug message")
logging.info("Informational message")
logging.error("An error has happened!")

log = logging.getLogger("ex")
logging.info("Program started")


#elmo = hub.Module(\https://tfhub.dev/google/elmo/2\, trainable=True)
fasttext_file = '181/model.model'
fasttext = KeyedVectors.load(fasttext_file)


def nopunct(phrase):
    nphrase = phrase
    nphrase = nphrase.replace(',', '')
    nphrase = nphrase.replace('.', '')
    nphrase = nphrase.replace('!', '')
    nphrase = nphrase.replace('?', '')
    nphrase = nphrase.replace('\n', ' ')
    nphrase = nphrase.replace('-', '')
    nphrase = nphrase.replace('  ', ' ')
    return nphrase


def get_data():
    import csv
    question2 = []
    with open('quora_question_pairs_rus.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            line = []
            for qword in m.lemmatize(nopunct(row[2])):
                if qword != ' ' and qword != '\n':
                    line.append(qword)
            question2.append(line)
    N = len(question2)
    return question2, N


def get_data1():
    import csv
    question1 = []
    with open('quora_question_pairs_rus.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            question1.append(row[1])
    return question1


def get_data2():
    import csv
    question2 = []
    with open('quest.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            question2.append(row)
    N = len(question2)
    return question2, N
    

def get_phrase(quiery):
    quiery = m.lemmatize(nopunct(quiery))
    phrase = []
    for word in quiery:
        if word != ' ' and word != '\n':
            phrase.append(word)
    lp = len(phrase)
    return phrase, lp


def get_lengths(question2):
    ls = []
    for question in question2:
        ls.append(len(question))
    avgdl = 0
    for l in ls:
        avgdl += l
    avgdl = avgdl/len(ls)
    return ls, avgdl


def get_words(question2):
    words = []
    for question in question2:
        for word in question:
            if word not in words:
                words.append(word)
    lw = len(words)
    return words, lw


def get_words2():
    words = []
    with open('word.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            words.append(''.join(row))
    lw = len(words)
    return words, lw


def get_dict(words, lw):
    dw = {}
    for g in range(lw):
        dw[words[g]] = g
    return dw


def TF(lw, N, question2, dw):
    TF = csr_matrix((N, lw)).toarray()
    for D in range(N):
        for Dword in question2[D]:
            q = dw[Dword]
            TF[D][q] = ((TF[D][q] * ls[D]) + 1) / ls[D] 
    return TF


def get_qdoc(lw, N):
    nq = []
    for q in range(lw):
        nq.append(0)
    for D in range(N):
        qmock = []
        for qword in question2[D]:
            q = dw[qword]
            if qword not in qmock:
                nq[q] += 1
            qmock.append(qword)
    return nq


def IDF(lw, N, nq):
    IDF = []
    for q in range(lw):
        IDF.append(0)
    for q in range(lw):
        IDF[q] = math.log(N/nq[q])
    return IDF


def IDFq(lw, N, nq):
    IDFq = []
    for q in range(lw):
        IDFq.append(0)
    for q in range(lw):
        IDFq[q] = math.log((N - nq[q] + 0.5)/(nq[q] + 0.5))
    return IDFq


def TFIDF(N, phrase, dw, TF, IDF):
    scores = []
    for D in range(N):
        score = 0
        for word in phrase:
            q = dw[word]
            score += IDF[q] * TF[D][q]
        scores.append(score)
    return scores


def bm25(N, phrase, dw, IDFq, TF, ls, avgdl, k, b):
    scores = []
    for D in range(N):
        score = 0
        for word in phrase:
            q = dw[word]
            score += IDFq[q] * ((TF[D][q] * (k + 1))/(TF[D][q] + k*(1 - b + b*ls[D]/avgdl)))
        scores.append(score)
    return scores


def results(scores, question2):
    results = []
    i = 10
    r = 0
    while r < i:
        r += 1
        best = sorted(scores, reverse=True)[r]
        for D in range(N):
            if scores[D] == best:
                if question1[D] not in results:
                    results.append(question1[D])
                else:
                    i += 1
                break
    return results


def get_fast_vect(phrase):
    lemmas_vectors = np.zeros((len(phrase), fasttext.vector_size))
    vec = np.zeros((fasttext.vector_size,))
    for idx, word in enumerate(phrase):
        try:
            if word in fasttext:
                lemmas_vectors[idx] = fasttext[word]
        except AttributeError as e:
            #log.exception(e)
            continue
    if lemmas_vectors.shape[0] is not 0:
        vec = np.mean(lemmas_vectors, axis=0)
    return vec


def get_fast_corp(question2):
    fast = []
    for phrase in question2:
        fast.append(get_fast_vect(phrase))
    return np.array(fast)


app = Flask(__name__)
    

if __name__ == '__main__':
    question1 = get_data1()
    question2, N = get_data2()            
    ls, avgdl = get_lengths(question2)
    words, lw = get_words2()                            
    dw = get_dict(words, lw)
    TF = TF(lw, N, question2, dw)
    nq = get_qdoc(lw, N)
    IDF = IDF(lw, N, nq)
    IDFq = IDFq(lw, N, nq)
    fast = get_fast_corp(question2)
    app.config.update(FLASK_ENV='development', TESTING=True, DEBUG=True)
    app.run(host='localhost', port=5000)
    

@app.route('/')
def index():
    return render_template('main_page.html')


@app.route('/2')
def sech():
    if 'TFIDF' in request.args:
        phrase, lp = get_phrase(request.args['TFIDF'])
        TFIDF = TFIDF(N, phrase, dw, TF, IDF)
        rtf = results(TFIDF, question2)
        logging.info("Done!")
        return render_template('test_page.html', innits = rtf)
    
    elif 'bm25' in request.args:
        phrase, lp = get_phrase(request.args['bm25'])
        bm25 = bm25(N, phrase, dw, IDFq, TF, ls, avgdl, 2.0, 0.75)
        rbm = results(bm25, question2)
        logging.info("Done!")
        return render_template('test_page.html', innits = rbm)
        
    elif 'fast' in request.args:
        phrase, lp = get_phrase(request.args['fast'])
        fast_score = fast.dot(get_fast_vect(phrase)).tolist()
        rfs = results(fast_score, question2)
        logging.info("Done!")
        return render_template('test_page.html', innits = rfs)
















