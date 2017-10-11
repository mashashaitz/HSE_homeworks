import re

def clean(html) :
    
    text = re.sub('[\d,.]', '', html)
    text = re.sub('\s+', ' ', text)
    return text

with open('Forhat.txt') as file:
    text = file.read()

text = clean(text)

with open('Forhat2.txt', 'w') as file:
            file.write(text)

