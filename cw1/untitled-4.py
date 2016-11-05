from random import randint

def if_a_needed_num_or_not_that_much(x):
    tr = False
    for num in range (1, 101):
        if x == str(num):
            tr = True
    
    return tr

t = False
while 4 < 5:
    if t == False:
        a = randint(0, 100) + 1
        t = True
        print('\n\n\nI\'ve chosen a number from 1 to 100, could you guess it? ')
    
    s = input('\nPut a number in here, \nTo stop the game press enter, to restart enter \'I give up\'\n')
    
    if s == '':
        break
    
    elif s == 'I give up' or s == 'i give up' or s == 'give up' or s == 'GO FUCK YOURSELF WITH SUCH A NUMBER' or s == '\'I give up\'':
        print('My number was ', a)
        t = False
        continue 
    
    elif if_a_needed_num_or_not_that_much(s) == False:
        print('OOO!!! I\'m afraid that something has gone terribly wrong! Excuse me...')
        continue
    
    i = int(s)
    
    if a == i:
        t = False
        print('WELL DONE!!! ')
    
    elif a > i:
        print('My number is bigger. Try again \n')
    
    else:
        print('My number is smaller. Try again \n ')