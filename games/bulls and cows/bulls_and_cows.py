import tkinter as tk
import re
import random


def different_letters(word_1):
    letters = []
    difference = True
    for letter in word_1:
        if letter in letters:
            difference = False
        else:
            letters.append(letter)
    return difference
        
    

def find_right_words():
    f = open('dict.txt', 'r', encoding = 'utf-8')
    words_1 = []
    for line in f:
        word = line.split()[0]
        category = line.split()[2]
        if len(word) == 4 and category == 'сущ':
            if different_letters(word):
                words_1.append(word)
    f.close()
    return words_1


def delete_letter():
    global label_2
    text_of_2 = label_2.config('text')[-1]
    new_text_of_2 = ''
    if '____' in text_of_2:
        new_text_of_2 = '____'
    elif '___' in text_of_2:
        new_text_of_2 = '____'
    elif '__' in text_of_2:
        new_text_of_2 = text_of_2[0] + '___'
    elif '_' in text_of_2:
        new_text_of_2 = text_of_2[0] + text_of_2[1] + '__'
    else:
        new_text_of_2 = text_of_2[0] + text_of_2[1] + text_of_2[2] + '_'

    label_2 = tk.Label(root, text = new_text_of_2, width = 16)
    label_2.config(bg = "White", bd = 4, fg = "Black", font = ('times', 13, 'italic'))
    label_2.grid(row = 3, column = 1)


def add_letter(letter):
    global label_2
    text_of_2 = label_2.config('text')[-1]
    new_text_of_2 = ''
    if '____' in text_of_2:
        new_text_of_2 = letter + '___'
    elif '___' in text_of_2:
        new_text_of_2 = text_of_2[0] + letter + '__'
    elif '__' in text_of_2:
        new_text_of_2 = text_of_2[0] + text_of_2[1] + letter + '_'
    else:
        new_text_of_2 = text_of_2[0] + text_of_2[1] + text_of_2[2] + letter

    label_2 = tk.Label(root, text = new_text_of_2, width = 16)
    label_2.config(bg = "White", bd = 4, fg = "Black", font = ('times', 13))
    label_2.grid(row = 3, column = 1)


def how_many_bulls():
    k = 0
    b = 0

    global label_1
    global label_2

    guess = label_2.config('text')[-1]
    
    if guess not in words:
        
        label_2 = tk.Label(root, text = '____', width = 16)
        label_2.config(bg = "White", bd = 4, fg = "Black", font = ('times', 13))
        label_2.grid(row = 3, column = 1)

        
    else:
        for n in range(4):
            if guess[n] == word[n]:
                b += 1
            elif guess[n] in word:
                k += 1
        if b == 4:
            label_2 = tk.Label(root, text = 'Победа!!!', width = 16)
            label_2.config(bg = "White", bd = 4, fg = "Black", font = ('times', 13, 'italic'))
            label_2.grid(row = 3, column = 1)

            global list_of_words
            if guess + ' 4 0' not in list_of_words:
                list_of_words.append(guess + ' 4 0')

            label_1 = tk.Label(root, text = guess, width = 16)
            label_1.config(bg = "White", bd = 4, fg = "Black", font = ('times', 13, 'italic'))
            label_1.grid(row = 2, column = 1)

            listbox = tk.Listbox(root, width = 16, height = 16)
            listbox.config(bg = "White", bd = 1, fg = "Black", font = ('times', 13, 'italic'))
            for result in list_of_words:
                listbox.insert(tk.END, result)
            listbox.grid(row = 4, column = 1)

        else:
            label_2 = tk.Label(root, text = '____', width = 16)
            label_2.config(bg = "White", bd = 4, fg = "Black", font = ('times', 13))
            label_2.grid(row = 3, column = 1)

            global list_of_words
            if guess + '  ' + str(b) + ' ' + str(k) + '\n' not in list_of_words:
                list_of_words.append(guess + '  ' + str(b) + ' ' + str(k) + '\n')

            listbox = tk.Listbox(root, width = 16, height = 16)
            listbox.config(bg = "White", bd = 1, fg = "Black", font = ('times', 13))
            for result in list_of_words:
                listbox.insert(tk.END, result)
            listbox.grid(row = 4, column = 1)

        if len(list_of_words) == 16:
            label_2 = tk.Label(root, text = 'Проигрыш(', width = 16)
            label_2.config(bg = "White", bd = 4, fg = "Black", font = ('times', 13, 'italic'))
            label_2.grid(row = 3, column = 1)
            
            label_1 = tk.Label(root, text = word, width = 16)
            label_1.config(bg = "White", bd = 4, fg = "Black", font = ('times', 13, 'italic'))
            label_1.grid(row = 2, column = 1)
    
    
def find_bulls(button):
    global label_2
    if button.config('text')[-1].lower() == '-' and len(label_2.config('text')[-1]) == 4:
        delete_letter()
    elif button.config('text')[-1].lower() in label_2.config('text')[-1]:
        return
    elif '__' in label_2.config('text')[-1]:
        add_letter(button.config('text')[-1].lower())
    elif len(label_2.config('text')[-1]) == 4:
        add_letter(button.config('text')[-1].lower())
        how_many_bulls()

    
def click_on_letter(event):
    find_bulls(event.widget) 

    
def create_letters():
    row_of_letter = 1
    column_of_letter = 1
    for letter in alphabet:
        button = tk.Button(root, text = letter, width = 4)
        button.config(bg = "White", bd = 4, fg = "Black", font = ('times', 11))
        button.bind('<Button-1>', click_on_letter)
        column_of_letter += 1
        if column_of_letter >  18:
            column_of_letter = 2
            row_of_letter += 1
        button.grid(row = row_of_letter, column = column_of_letter)


def createall(event):
    global word
    word = random.choice(words)

    global list_of_words
    list_of_words = []
    list_of_words.append('слово б к \n')
    listbox = tk.Listbox(root, width = 16, height = 16)
    listbox.config(bg = "White", bd = 1, fg = "Black", font = ('times', 13))
    listbox.insert(tk.END, 'слово Б К \n')
    listbox.grid(row = 4, column = 1)

    global label_1
    global label_2
    
    label_1 = tk.Label(root, text = '****', width = 16)
    label_1.config(bg = "White", bd = 4, fg = "Black", font = ('times', 13))
    label_1.grid(row = 2, column = 1)

    label_2 = tk.Label(root, text = '____', width = 16)
    label_2.config(bg = "White", bd = 4, fg = "Black", font = ('times', 13))
    label_2.grid(row = 3, column = 1)

    create_letters()
    

def main():
    global root
    root = tk.Tk()
    root.configure(bg = "White")

    global alphabet
    alphabet = ('АБВГДЁЕЖЗИЙКЛМНОПРСТУФХЦШЩЧЬЫЪЭЮЯ-')

    global words
    words = find_right_words()


    button = tk.Button(root, text = "Новая игра", width = 16)
    button.config(bg = "White", bd = 4, fg = "Black", font = ('times', 12, 'italic'))
    button.bind('<Button-1>', createall)
    button.grid(row = 1, column = 1)

    root.mainloop()
    
    
main()
