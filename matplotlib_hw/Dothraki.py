import matplotlib
import matplotlib.pyplot as plt
import re


def open_dict():
    
    with open('dothraki_vocabulary.txt', 'r', encoding='utf-8') as f:
        text = f.read()
        reg_words = re.compile('<ul><li><b>([A-Za-z]+)</b>')
        reg_speech_parts = re.compile('<dl><dd><i>([a-z./&#8594;→]+)</i>')
        words = reg_words.findall(text)
        speech_parts = reg_speech_parts.findall(text)

        for speech_part in speech_parts:
            if '&' in speech_part:
                speech_part = speech_part.replace('&#8594;', '→')
        return speech_parts, words


def prepare_speech_parts(speech_parts):
    speech = {}
    for speech_part in speech_parts:
        if speech_part in speech:
            speech[speech_part] += 1
        else:
            speech[speech_part] = 1
    speech_part_array = []
    speech_part_quantity_array = []
    for speech_part in sorted(speech):
        speech_part_array.append(speech_part.replace('&#8594;', '→'))
        speech_part_quantity_array.append(speech[speech_part])
    return speech_part_array, speech_part_quantity_array


def prepare_words(words):
    letters = {}
    for word in words:
        if word[0].lower() in letters:
            letters[word[0].lower()] += 1
        else:
            letters[word[0].lower()] = 1
    letters_array = []
    letters_quantity_array = []
    for letter in sorted(letters):
        letters_array.append(letter)
        letters_quantity_array.append(letters[letter])
    return letters_array, letters_quantity_array


def draw_plot(speech, speechq, letters, lettersq):
    f, (graph_Speech, graph_Letters) = plt.subplots(2, 1)

    X = []
    for i, q in enumerate(speechq):
        graph_Speech.bar(i*2, q, color='g')
        X.append(i*2)
    graph_Speech.set_xticks(X)
    graph_Speech.set_xticklabels(speech)
    graph_Speech.set_xlabel("Часть речи")
    graph_Speech.set_ylabel("Количество")
    graph_Speech.set_title("Части речи в Детракийскомм")
    
    #graph_Speech.set_xlim(0,3000)
    #graph_Speech.set_ylim(0,700)
    #graph_Speech.invert_yaxis()
    
    X = []
    for i, q in enumerate(lettersq):
        graph_Letters.bar(i*2, q, color='g')
        X.append(i*2)
    graph_Letters.set_xticks(X)
    graph_Letters.set_xticklabels(letters)
    graph_Letters.set_xlabel("Буква")
    graph_Letters.set_ylabel("Количество")
    #graph_Letters.yaxis.tick_right()
    graph_Letters.set_title("\nБуквы в Детракийском")
    #graph_Letters.set_xlim(0,3000)
    #graph_Letters.set_ylim(0,700)
    #graph_Letters.invert_yaxis()
    #graph_Letters.yaxis.set_label_position('right')

    plt.tight_layout()
    plt.show()

    return 


def main():
    speech_parts, words = open_dict()
    speech, speechq = prepare_speech_parts(speech_parts)
    letters, lettersq = prepare_words(words)
    
    draw_plot(speech, speechq, letters, lettersq)


main()
