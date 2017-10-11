import tkinter as tk
import re
import random

root = tk.Tk()
root.configure(bg = "White")
canvas = tk.Canvas(root, width = 500, height = 1000, background="Blue", bd = 0, relief = "flat")

def viselitsa(a):

    if a == 0:
        canvas.create_oval(500 - 200, 200 - 100, 600 - 200, 300 - 100, fill = "BlanchedAlmond", outline = "BlanchedAlmond")
        canvas.create_line(550 - 200, 300 - 100, 550 - 200, 480 - 100, fill = "BlanchedAlmond", width = 10)
        canvas.create_line(550 - 200, 330 - 100, 500 - 200, 480 - 100, fill = "BlanchedAlmond", width = 5)
        canvas.create_line(550 - 200, 330 - 100, 600 - 200, 480 - 100, fill = "BlanchedAlmond", width = 5)
        canvas.create_line(550 - 200, 470 - 100, 500 - 200, 720 - 100, fill = "BlanchedAlmond", width = 7)
        canvas.create_line(550 - 200, 470 - 100, 600 - 200, 720 - 100, fill = "BlanchedAlmond", width = 7)

    if a == 1:

        canvas.create_oval(500 - 200, 200 - 100, 600 - 200, 300 - 100, fill = "Blue", outline = "Blue")
        canvas.create_line(550 - 200, 300 - 100, 550 - 200, 480 - 100, fill = "Blue", width = 10)
        canvas.create_line(550 - 200, 330 - 100, 500 - 200, 480 - 100, fill = "Blue", width = 5)
        canvas.create_line(550 - 200, 330 - 100, 600 - 200, 480 - 100, fill = "Blue", width = 5)
        canvas.create_line(550 - 200, 470 - 100, 500 - 200, 720 - 100, fill = "Blue", width = 7)
        canvas.create_line(550 - 200, 470 - 100, 600 - 200, 720 - 100, fill = "Blue", width = 7)

        canvas.create_oval(500 - 200, 150 - 100, 600 - 200, 250 - 100, fill = "BlanchedAlmond", outline = "BlanchedAlmond")
        canvas.create_line(550 - 200, 250 - 100, 550 - 200, 430 - 100, fill = "BlanchedAlmond", width = 10)
        canvas.create_line(550 - 200, 280 - 100, 500 - 200, 430 - 100, fill = "BlanchedAlmond", width = 5)
        canvas.create_line(550 - 200, 280 - 100, 600 - 200, 430 - 100, fill = "BlanchedAlmond", width = 5)
        canvas.create_line(550 - 200, 420 - 100, 500 - 200, 670 - 100, fill = "BlanchedAlmond", width = 7)
        canvas.create_line(550 - 200, 420 - 100, 600 - 200, 670 - 100, fill = "BlanchedAlmond", width = 7)
#taburet
        canvas.create_rectangle(475 - 200, 675 - 100, 625 - 200, 695 - 100, fill = "DarkOrange4", outline = "DarkOrange4")
        canvas.create_rectangle(480 - 200, 670 - 100, 620 - 200, 700 - 100, fill = "DarkOrange4", outline = "DarkOrange4")
        
        canvas.create_oval(475 - 200, 675 - 100, 480 - 200, 670 - 100, fill = "DarkOrange4", outline = "DarkOrange4")
        canvas.create_oval(475 - 200, 695 - 100, 480 - 200, 700 - 100, fill = "DarkOrange4", outline = "DarkOrange4")
        canvas.create_oval(625 - 200, 675 - 100, 620 - 200, 670 - 100, fill = "DarkOrange4", outline = "DarkOrange4")
        canvas.create_oval(625 - 200, 695 - 100, 620 - 200, 700 - 100, fill = "DarkOrange4", outline = "DarkOrange4")
        
        canvas.create_rectangle(475 - 200, 700 - 100, 500 - 200, 720 - 100, fill = "DarkOrange4", outline = "Salmon4")
        canvas.create_rectangle(600 - 200, 700 - 100, 625 - 200, 720 - 100, fill = "DarkOrange4", outline = "Salmon4")
        
    if a == 2:
#плаха       
        canvas.create_rectangle(675 - 200, 720, 700 - 200, 0, fill = "DarkOrange4", outline = "DarkOrange4")
        canvas.create_rectangle(670 - 200, 715, 705 - 200, 5, fill = "DarkOrange4", outline = "DarkOrange4")

        canvas.create_oval(675 - 200, 720, 670 - 200, 715, fill = "DarkOrange4", outline = "DarkOrange4")
        canvas.create_oval(675 - 200, 0, 670 - 200, 5, fill = "DarkOrange4", outline = "DarkOrange4")
        canvas.create_oval(700 - 200, 720, 705 - 200, 715, fill = "DarkOrange4", outline = "DarkOrange4")
        canvas.create_oval(700 - 200, 0, 705 - 200, 5, fill = "DarkOrange4", outline = "DarkOrange4")
        
        
    if a == 3:
#плаха
        canvas.create_rectangle(425 - 200, 0, 700 - 200, 35, fill = "DarkOrange4", outline = "DarkOrange4")
        canvas.create_rectangle(420 - 200, 5, 705 - 200, 30, fill = "DarkOrange4", outline = "DarkOrange4")
        canvas.create_oval(425 - 200, 0, 420 - 200, 5, fill = "DarkOrange4", outline = "DarkOrange4")
        canvas.create_oval(425 - 200, 35, 420 - 200, 30, fill = "DarkOrange4", outline = "DarkOrange4")
        canvas.create_oval(700 - 200, 0, 705 - 200, 5, fill = "DarkOrange4", outline = "DarkOrange4")
        canvas.create_oval(700 - 200, 35, 705 - 200, 30, fill = "DarkOrange4", outline = "DarkOrange4")
        
    if a == 4:
#rope
        canvas.create_line(550 - 200, 35, 550 - 200, 150 - 100, fill = "Orange2", width = 6)
        canvas.create_line(544 - 200, 270 - 100, 556 - 200, 270 - 100, fill = "Orange2", width = 6)

    if a == 5:
#throw taburet        
        canvas.create_rectangle(475 - 200, 675 - 100, 625 - 200, 695 - 100, fill = "Blue", outline = "Blue")
        canvas.create_rectangle(480 - 200, 670 - 100, 620 - 200, 700 - 100, fill = "Blue", outline = "Blue")
        
        canvas.create_oval(475 - 200, 675 - 100, 480 - 200, 670 - 100, fill = "Blue", outline = "Blue")
        canvas.create_oval(475 - 200, 695 - 100, 480 - 200, 700 - 100, fill = "Blue", outline = "Blue")
        canvas.create_oval(625 - 200, 675 - 100, 620 - 200, 670 - 100, fill = "Blue", outline = "Blue")
        canvas.create_oval(625 - 200, 695 - 100, 620 - 200, 700 - 100, fill = "Blue", outline = "Blue")
        
        canvas.create_rectangle(475 - 200, 700 - 100, 500 - 200, 720 - 100, fill = "Blue", outline = "Blue")
        canvas.create_rectangle(600 - 200, 700 - 100, 625 - 200, 720 - 100, fill = "Blue", outline = "Blue")

        #
        canvas.create_rectangle(300 - 200, 620 - 100, 450 - 200, 720 - 100, fill = "DarkOrange4", outline = "Salmon4")

        canvas.create_rectangle(315 - 200, 635 - 100, 330 - 200, 650 - 100, fill = "DarkOrange4", outline = "Salmon4")
        canvas.create_rectangle(420 - 200, 635 - 100, 435 - 200, 650 - 100, fill = "DarkOrange4", outline = "Salmon4")
        canvas.create_rectangle(315 - 200, 705 - 100, 330 - 200, 690 - 100, fill = "DarkOrange4", outline = "Salmon4")
        canvas.create_rectangle(420 - 200, 705 - 100, 435 - 200, 690 - 100, fill = "DarkOrange4", outline = "Salmon4")

    if a == 6:
#body        
        canvas.create_oval(500 - 200, 150 - 100, 600 - 200, 250 - 100, fill = "Blue", outline = "Blue")
        canvas.create_line(550 - 200, 250 - 100, 550 - 200, 430 - 100, fill = "Blue", width = 10)
        canvas.create_line(550 - 200, 280 - 100, 500 - 200, 430 - 100, fill = "Blue", width = 5)
        canvas.create_line(550 - 200, 280 - 100, 600 - 200, 430 - 100, fill = 'Blue', width = 5)
        canvas.create_line(550 - 200, 420 - 100, 500 - 200, 670 - 100, fill = "Blue", width = 7)
        canvas.create_line(550 - 200, 420 - 100, 600 - 200, 670 - 100, fill = "Blue", width = 7)

        canvas.create_oval(500 - 200, 150 - 100, 600 - 200, 250 - 100, fill = "LightYellow1", outline = "LightYellow1")
#hands
        canvas.create_line(548 - 200, 285 - 100, 519.91 - 200, 353.15 - 100, fill = "LightYellow1", width = 5)
        canvas.create_line(518.32 - 200, 356.69 - 100, 516.73 - 200, 360.23 - 100, fill = "LightYellow1", width = 5)
        canvas.create_line(515.14 - 200, 363.77 - 100, 495 - 200, 430 - 100, fill = "LightYellow1", width = 5)

        canvas.create_line(552 - 200, 285 - 100, 575.32 - 200, 353.15 - 100, fill = "LightYellow1", width = 5)
        canvas.create_line(576.91 - 200, 356.69 - 100, 578.5 - 200, 360.23 - 100, fill = "LightYellow1", width = 5)
        canvas.create_line(580.09 - 200, 363.77 - 100, 605 - 200, 430 - 100, fill = "LightYellow1", width = 5)
#legs        
        canvas.create_line(548 - 200, 427 - 100, 525 - 200, 533.92 - 100, fill = "LightYellow1", width = 7)
        canvas.create_line(524 - 200, 541.21 - 100, 522.56 - 200, 548.5 - 100, fill = "LightYellow1", width = 7)
        canvas.create_line(521.12 - 200, 555.79 - 100, 500 - 200, 670 - 100, fill = "LightYellow1", width = 7)

        canvas.create_line(552 - 200, 427 - 100, 573.12 - 200, 533.92 - 100, fill = "LightYellow1", width = 7)
        canvas.create_line(574.56 - 200, 541.21 - 100, 576 - 200, 548.5 - 100, fill = "LightYellow1", width = 7)
        canvas.create_line(577.44 - 200, 555.79 - 100, 600 - 200, 670 - 100, fill = "LightYellow1", width = 7)
#spine
        canvas.create_line(550 - 200, 245 - 100, 550 - 200, 430 - 100, fill = "LightYellow1", dash = (4, 4), width = 10)

#rope again
        canvas.create_line(550 - 200, 35 - 100, 550 - 200, 150 - 100, fill = "Orange2", width = 6)
        canvas.create_line(550 - 200, 255 - 100, 550 - 200, 265 - 100, fill = "Orange2", width = 6)
        canvas.create_line(544 - 200, 270 - 100, 556 - 200, 270 - 100, fill = "Orange2", width = 6)
#mouth        
        canvas.create_oval(535 - 200, 225 - 100, 565 - 200, 235 - 100, fill = "black", outline = "black")
        canvas.create_oval(535 - 200, 230 - 100, 565 - 200, 240 - 100, fill = "LightYellow1", outline = "LightYellow1")
#глаза
        canvas.create_oval(515 - 200, 175 - 100, 540 - 200, 200 - 100, fill = "black", outline = "black")
        canvas.create_oval(585 - 200, 175 - 100, 560 - 200, 200 - 100, fill = "black", outline = "black")
#ноздри
        canvas.create_oval(543 - 200, 210 - 100, 548 - 200, 215 - 100, fill = "black", outline = "black")
        canvas.create_oval(550 - 200, 210 - 100, 555 - 200, 215 - 100, fill = "black", outline = "black")

def Victory():
    canvas.create_rectangle(0, 0, 750, 750, fill = "Blue", outline = "Blue")
    canvas.create_oval(748, 2, 743, 17, fill = "Yellow1", outline = "Orange")
    canvas.create_oval(500 - 200, 200 - 100, 600 - 200, 300 - 100, fill = "BlanchedAlmond", outline = "BlanchedAlmond")
    canvas.create_line(550 - 200, 300 - 100, 550 - 200, 480 - 100, fill = "BlanchedAlmond", width = 10)
    canvas.create_line(550 - 200, 330 - 100, 500 - 200, 480 - 100, fill = "BlanchedAlmond", width = 5)
    canvas.create_line(550 - 200, 330 - 100, 600 - 200, 480 - 100, fill = "BlanchedAlmond", width = 5)
    canvas.create_line(550 - 200, 470 - 100, 500 - 200, 720 - 100, fill = "BlanchedAlmond", width = 7)
    canvas.create_line(550 - 200, 470 - 100, 600 - 200, 720 - 100, fill = "BlanchedAlmond", width = 7)
#mouth        
    canvas.create_oval(535 - 200, 215 - 100 + 50, 565 - 200, 225 - 100 + 50, fill = "Tomato1", outline = "Tomato1")
    canvas.create_oval(535 - 200, 210 - 100 + 50, 565 - 200, 220 - 100 + 50, fill = "BlanchedAlmond", outline = "BlanchedAlmond")
#глаза
    canvas.create_oval(521 - 200, 179 - 100 + 50, 536 - 200, 196 - 100 + 50, fill = "lightblue", outline = "lightblue")
    canvas.create_oval(564 - 200, 179 - 100 + 50, 579 - 200, 196 - 100 + 50, fill = "lightblue", outline = "lightblue")
    canvas.create_oval(525.5 - 200, 183.5 - 100 + 50, 528.5 - 200, 186.5 - 100 + 50, fill = "black", outline = "black")
    canvas.create_oval(568.5 - 200, 183.5 - 100 + 50, 571.5 - 200, 186.5 - 100 + 50, fill = "black", outline = "black")
#шарик
    canvas.create_oval(205, 5, 285, 115, fill = "yellow1", outline = "yellow1")
    canvas.create_polygon(237, 125, 245, 115, 253, 125, fill = "yellow1", outline = "orange1")
    canvas.create_line(245, 125, 298, 377, fill = "orange1", width = 1)
#юбочка
    canvas.create_polygon(280, 570, 350, 370, 420, 570, fill = "DeepPink2", outline = "DeepPink1")
    canvas.create_line(550 - 200, 370, 550 - 200, 385, fill = "BlanchedAlmond", width = 10)
#бантик
    canvas.create_polygon(345, 90, 365, 102, 348, 110, fill = "DeepPink2", outline = "DeepPink1")
    canvas.create_polygon(385, 94, 365, 102, 382, 114, fill = "DeepPink2", outline = "DeepPink1")
        

c = ("АБВГДЕЖЗИЙКЛМНОПРСТУФХЦШЩЧЬЫЪЭЮЯ")

with open('Forhat4.txt', 'r', encoding = 'utf-8') as file:
    file.seek(0)
    forlet = file.read().split()
    
def createall (event):
    global T
    global let
    global K

    K = 0
    T = 0
    canvas.create_rectangle(0, 0, 750, 750, fill = "Blue", outline = "Blue")

    let = random.choice(forlet)
    let2 = ""
    for each in let:
        let2 += "*"
        
    label = tk.Label(root, text = let2, width = 40)
    label.config(bg = "White", bd = 4, fg = "Black", font = ('times', 13, 'italic'))
    label.grid(row = 2, column = 1)

    a = 1
    b = 1
    
    def though2 (let2, button):
        
        global T
        global let
        global K
        
        if (T < 7)  & (K == 0):
            
            k3 = 0
            n3 = 0
            i = 0

            for each in let:
                
                if (button.config('text')[-1]).lower() == each:
                    k3 = k3 + 1
                    i2 = 0
                    let3 = ""
                    let2 = label.config('text')[-1]
                    let2 = list(let2);
                    let2[i] = each
                    let2 = "".join(let2)
                    label.config(text = let2)
                i += 1
                    
            if (k3 == 0) & (button.config('text')[-1].lower() != ""):
                viselitsa(T)
                T = T + 1

            button.config(bg = "White", text = "")

                        
        if (T > 6) & (K == 0):
            label.config(text = '"' + let + '"' + " " + "Вы проиграли.")
            K = 1

        if (label.config('text')[-1] == let):
            label.config(text = '"' + let + '"' + " " + "Победа!!!")
            Victory()
            T = 7
            K = 2
                    
    def thought (event):
        though2 (let2, event.widget)    
    
    for each in c:
        button = tk.Button(root, text = each, width = 4)
        button.config(bg = "White", bd = 4, fg = "Black", font = ('times', 11, 'italic'))
        button.bind('<Button-1>', thought)
        a = a + 1
        if a >  17:
            a = 2
            b = b + 1
        button.grid(row = b, column = a)


button = tk.Button(root, text = "Новая игра", width = 16)
button.config(bg = "Green", bd = 4, fg = "Black", font = ('times', 12, 'italic'))
button.bind('<Button-1>', createall)
button.grid(row = 1, column = 1)

label = tk.Label(root, text = 'Удачи!!!', width = 40)
label.config(bg = "White", bd = 4, fg = "Black", font = ('times', 13, 'italic'))
label.grid(row = 2, column = 1)

canvas.grid(row = 3, column = 1)

root.mainloop()
 
