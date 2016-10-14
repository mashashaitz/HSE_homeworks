from random import randint

a = randint(0, 100)
t = False
while t == False:
    i = int(input('put a number here '))
    if a == i:
        t = True
        print('Well done')
    elif a > i:
        print('My number is bigger. Try again ')
    else:
        print('My number is smaller. Try again ')