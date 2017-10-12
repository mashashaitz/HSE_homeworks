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


def draw_victory():
    global canvas
    canvas = tk.Canvas(root, width = 775, height = 256, background="SteelBlue1", bd = 0, relief = "flat")
    canvas.grid(row = 4, column = 3, columnspan=15)

    canvas.create_rectangle(0, 250, 776, 257, fill = "SpringGreen4", outline = "SpringGreen4")
    canvas.create_oval(740, -35, 810, 35, fill = "Gold", outline = "Gold")

    for each in [[0, "yellow1", "lightblue", "DeepPink2"], [1, "red2", "DarkOliveGreen2", "hotpink"], [2, "cyan", "green3", "purple"], [3, "tan1", "dim gray", "paleTurquoise1"], [4, "sienna1", "RoyalBlue2", "coral2"], [5, "yellow2", "medium sea green", "maroon1"], [6, "orangered2", "gray56", "aquamarine"]]:
        canvas.create_oval(60 + each[0]*100, 40, 100 + each[0]*100, 80, fill = "BlanchedAlmond", outline = "BlanchedAlmond")
        canvas.create_line(80 + each[0]*100, 60, 80 + each[0]*100, 180, fill = "BlanchedAlmond", width = 4)
        canvas.create_line(80 + each[0]*100, 178, 95 + each[0]*100, 250, fill = "BlanchedAlmond", width = 3)
        canvas.create_line(79 + each[0]*100, 178, 64 + each[0]*100, 250, fill = "BlanchedAlmond", width = 3)
        canvas.create_line(81 + each[0]*100, 105, 91 + each[0]*100, 155, fill = "BlanchedAlmond", width = 2)
        canvas.create_line(79 + each[0]*100, 105, 60 + each[0]*100, 151, fill = "BlanchedAlmond", width = 2)
        
        canvas.create_oval(60 + 15 + each[0]*100, 40 + 24, 100 - 15 + each[0]*100, 80 - 7, fill = "Tomato1", outline = "Tomato1")
        canvas.create_oval(60 + 15 + each[0]*100, 40 + 22, 100 - 15 + each[0]*100, 80 - 9, fill = "BlanchedAlmond", outline = "BlanchedAlmond")

        canvas.create_oval(67 + each[0]*100, 50, 72 + each[0]*100, 57, fill = each[2], outline = each[2])
        canvas.create_oval(88 + each[0]*100, 50, 93 + each[0]*100, 57, fill = each[2], outline = each[2])
        canvas.create_oval(68 + each[0]*100, 52, 69 + each[0]*100, 53, fill = "black", outline = "black")
        canvas.create_oval(89 + each[0]*100, 52, 90 + each[0]*100, 53, fill = "black", outline = "black")

        canvas.create_oval(10 + each[0]*100, 2, 50 + each[0]*100, 75, fill = each[1], outline = each[1])
        canvas.create_polygon(27 + each[0]*100, 78, 30 + each[0]*100, 75, 33 + each[0]*100, 78, fill = each[1], outline = each[1])
        canvas.create_line(30 + each[0]*100, 78, 60 + each[0]*100, 151, fill = "orange1", width = 1)

        canvas.create_polygon(87 + each[0]*100, 38, 90 + each[0]*100, 43, 84 + each[0]*100, 41, fill = each[3], outline = each[3])
        canvas.create_polygon(93 + each[0]*100, 47, 90 + each[0]*100, 43, 96 + each[0]*100, 44, fill = each[3], outline = each[3])


def draw_loss():
    global canvas
    canvas = tk.Canvas(root, width = 775, height = 256, background="gray54", bd = 0, relief = "flat")
    canvas.grid(row = 4, column = 3, columnspan=15)

    canvas.create_rectangle(0, 250, 776, 257, fill = "dark olive green", outline = "dark olive green")
    canvas.create_oval(740, -35, 810, 35, fill = "ghost white", outline = "ghost white")

    for each in [[0, "yellow1", "lightblue", "DeepPink2"], [1, "red2", "DarkOliveGreen2", "hotpink"], [2, "cyan", "green3", "purple"], [3, "tan1", "dim gray", "paleTurquoise1"], [4, "sienna1", "RoyalBlue2", "coral2"], [5, "yellow2", "medium sea green", "maroon1"], [6, "orangered2", "gray56", "aquamarine"]]:
        canvas.create_oval(60 + each[0]*100, 40, 100 + each[0]*100, 80, fill = "BlanchedAlmond", outline = "BlanchedAlmond")
        canvas.create_line(80 + each[0]*100, 60, 80 + each[0]*100, 180, fill = "BlanchedAlmond", width = 4)
        canvas.create_line(80 + each[0]*100, 178, 95 + each[0]*100, 250, fill = "BlanchedAlmond", width = 3)
        canvas.create_line(79 + each[0]*100, 178, 64 + each[0]*100, 250, fill = "BlanchedAlmond", width = 3)
        canvas.create_line(81 + each[0]*100, 105, 91 + each[0]*100, 155, fill = "BlanchedAlmond", width = 2)
        canvas.create_line(79 + each[0]*100, 105, 69 + each[0]*100, 155, fill = "BlanchedAlmond", width = 2)
        
        canvas.create_oval(60 + 15 + each[0]*100, 71-2, 100 - 15 + each[0]*100, 80 - 2, fill = "Tomato1", outline = "Tomato1")
        canvas.create_oval(60 + 15 + each[0]*100, 71, 100 - 15 + each[0]*100, 80, fill = "BlanchedAlmond", outline = "BlanchedAlmond")

        canvas.create_oval(67 + each[0]*100, 50, 72 + each[0]*100, 57, fill = each[2], outline = each[2])
        canvas.create_oval(88 + each[0]*100, 50, 93 + each[0]*100, 57, fill = each[2], outline = each[2])
        canvas.create_oval(69 + each[0]*100, 53, 70 + each[0]*100, 54, fill = "black", outline = "black")
        canvas.create_oval(90 + each[0]*100, 53, 91 + each[0]*100, 54, fill = "black", outline = "black")


def draw_regular():
    global canvas
    canvas = tk.Canvas(root, width = 775, height = 256, background="SteelBlue1", bd = 0, relief = "flat")
    canvas.grid(row = 4, column = 3, columnspan=15)

    canvas.create_rectangle(0, 250, 776, 257, fill = "SpringGreen4", outline = "SpringGreen4")
    canvas.create_oval(740, -35, 810, 35, fill = "Gold", outline = "Gold")

    for each in [[0, "yellow1", "lightblue", "DeepPink2"], [1, "red2", "DarkOliveGreen2", "hotpink"], [2, "cyan", "green3", "purple"], [3, "tan1", "dim gray", "paleTurquoise1"], [4, "sienna1", "RoyalBlue2", "coral2"], [5, "yellow2", "medium sea green", "maroon1"], [6, "orangered2", "gray56", "aquamarine"]]:
        canvas.create_oval(60 + each[0]*100, 40, 100 + each[0]*100, 80, fill = "BlanchedAlmond", outline = "BlanchedAlmond")
        canvas.create_line(80 + each[0]*100, 60, 80 + each[0]*100, 180, fill = "BlanchedAlmond", width = 4)
        canvas.create_line(80 + each[0]*100, 178, 95 + each[0]*100, 250, fill = "BlanchedAlmond", width = 3)
        canvas.create_line(79 + each[0]*100, 178, 64 + each[0]*100, 250, fill = "BlanchedAlmond", width = 3)
        canvas.create_line(81 + each[0]*100, 105, 91 + each[0]*100, 155, fill = "BlanchedAlmond", width = 2)
        canvas.create_line(79 + each[0]*100, 105, 69 + each[0]*100, 155, fill = "BlanchedAlmond", width = 2)
        
        canvas.create_line(60 + 16 + each[0]*100, 70, 100 - 16 + each[0]*100, 70, fill = "Tomato1", width = 2)

        canvas.create_oval(67 + each[0]*100, 50, 72 + each[0]*100, 57, fill = each[2], outline = each[2])
        canvas.create_oval(88 + each[0]*100, 50, 93 + each[0]*100, 57, fill = each[2], outline = each[2])
        canvas.create_oval(69 + each[0]*100, 53, 70 + each[0]*100, 54, fill = "black", outline = "black")
        canvas.create_oval(90 + each[0]*100, 53, 91 + each[0]*100, 54, fill = "black", outline = "black")


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
    label_2.config(bg = "White", bd = 4, fg = "Black", font = ('times', 13))
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
    elif '_' in text_of_2:
        new_text_of_2 = text_of_2[0] + text_of_2[1] + text_of_2[2] + letter
    else:
        new_text_of_2 = text_of_2

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
            label_2.config(bg = "White", bd = 4, fg = "Black", font = ('times', 13))
            label_2.grid(row = 3, column = 1)

            label_1 = tk.Label(root, text = word, width = 16)
            label_1.config(bg = "White", bd = 4, fg = "Black", font = ('times', 13))
            label_1.grid(row = 2, column = 1)

            draw_victory()

            global list_of_words
            if guess + ' 4 0' not in list_of_words:
                list_of_words.append(guess + ' 4 0')

            label_1 = tk.Label(root, text = guess, width = 16)
            label_1.config(bg = "White", bd = 4, fg = "Black", font = ('times', 13))
            label_1.grid(row = 2, column = 1)

            listbox = tk.Listbox(root, width = 16, height = 16)
            listbox.config(bg = "White", bd = 1, fg = "Black", font = ('times', 13))
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
            label_2.config(bg = "White", bd = 4, fg = "Black", font = ('times', 13))
            label_2.grid(row = 3, column = 1)
            
            label_1 = tk.Label(root, text = word, width = 16)
            label_1.config(bg = "White", bd = 4, fg = "Black", font = ('times', 13))
            label_1.grid(row = 2, column = 1)

            draw_loss()


def give_up(event):
    global label_1
    global label_2

    if '*' in label_2.config('text')[-1]:
    
        label_2 = tk.Label(root, text = 'Вы сдались(', width = 16)
        label_2.config(bg = "White", bd = 4, fg = "Black", font = ('times', 13))
        label_2.grid(row = 3, column = 1)
                
        label_1 = tk.Label(root, text = word, width = 16)
        label_1.config(bg = "White", bd = 4, fg = "Black", font = ('times', 13))
        label_1.grid(row = 2, column = 1)

        draw_loss()


def give_up_with_style(event):
    global label_1
    global label_2

    if '*' in label_2.config('text')[-1]:
    
        label_2 = tk.Label(root, text = 'Вы сдались)', width = 16)
        label_2.config(bg = "White", bd = 4, fg = "Black", font = ('times', 13))
        label_2.grid(row = 3, column = 1)

        label_1 = tk.Label(root, text = word, width = 16)
        label_1.config(bg = "White", bd = 4, fg = "Black", font = ('times', 13))
        label_1.grid(row = 2, column = 1)

        draw_victory()

        
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


def change_colour(button):
    row_of_letter = 5
    column_of_letter = 1
    for letter in alphabet[0:-1]:
        column_of_letter += 1
        if column_of_letter >  18:
            column_of_letter = 2
            row_of_letter += 1
        if button.config('text')[-1].lower() == letter.lower():
            label = tk.Label(root, text = '', width = 7, height = 1)
            label.config(bg = "White", bd = 4, fg = "Black", font = ('times', 11))
            label.bind('<Button-1>', click_on_letter_2)
            label.grid(row = row_of_letter, column = column_of_letter)



def click_on_letter_2(event):
    change_colour(event.widget)

    
def create_letters_2():
    row_of_letter = 5
    column_of_letter = 1
    for letter in alphabet[0:-1]:
        button_1 = tk.Button(root, text = letter, width = 4)
        button_1.config(bg = "Green", bd = 4, fg = "Black", font = ('times', 11))
        button_1.bind('<Button-1>', click_on_letter_2)
        column_of_letter += 1
        if column_of_letter >  18:
            column_of_letter = 2
            row_of_letter += 1
        button_1.grid(row = row_of_letter, column = column_of_letter)

        
def create_letters_3(event):
    row_of_letter = 5
    column_of_letter = 1
    for letter in alphabet[0:-1]:
        button_1 = tk.Button(root, text = letter, width = 4)
        button_1.config(bg = "Green", bd = 4, fg = "Black", font = ('times', 11))
        button_1.bind('<Button-1>', click_on_letter_2)
        column_of_letter += 1
        if column_of_letter >  18:
            column_of_letter = 2
            row_of_letter += 1
        button_1.grid(row = row_of_letter, column = column_of_letter)


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

    global canvas
    canvas = tk.Canvas(root, width = 775, height = 256, background="White", bd = 0, relief = "flat")
    canvas.grid(row = 4, column = 3, columnspan=15)

    draw_regular()

    create_letters()
    create_letters_2()
    

def main():
    global root
    root = tk.Tk()
    root.configure(bg = "White")

    global alphabet
    alphabet = ('АБВГДЁЕЖЗИЙКЛМНОПРСТУФХЦШЩЧЬЫЪЭЮЯ-')

    global words
    words = find_right_words()

    button = tk.Button(root, text = "Новая игра", width = 16)
    button.config(bg = "White", bd = 4, fg = "Black", font = ('times', 12))
    button.bind('<Button-1>', createall)
    button.grid(row = 1, column = 1)

    button_1 = tk.Button(root, text = "+", width = 4)
    button_1.config(bg = "White", bd = 4, fg = "Black", font = ('times', 12))
    button_1.bind('<Button-1>', create_letters_3)
    button_1.grid(row = 6, column = 18)

    button_2 = tk.Button(root, text = "Сдаться", width = 16)
    button_2.config(bg = "White", bd = 4, fg = "Black", font = ('times', 13))
    button_2.bind('<Button-1>', give_up)
    button_2.grid(row = 5, column = 1)

    button_3 = tk.Button(root, text = "Сдаться красиво", width = 16)
    button_3.config(bg = "White", bd = 4, fg = "Black", font = ('times', 13))
    button_3.bind('<Button-1>', give_up_with_style)
    button_3.grid(row = 6, column = 1)

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
    create_letters_2()

    draw_regular()

    root.mainloop()
    
    
main()
