#Найти предложения длиннее 10 слов,
#и для этих предложений распечатать слова, начинающиеся с заглавной буквы
#Нужно взять какой-нибудь файл с достаточно большим текстом,
#прочитать его, поделить на предложения (просто по знакам конца предложения),
#удалить знаки препинания.
#Затем в зависимости от варианта сделать следующее
#(обязательно использовать list comprehensions и formatting)

symbols = '\'"/.,<>:;[]{}\\|1234567890`~!@#$%^&*()_+-=?!«»…—'
capital_letters = 'QWERTYUIOPASDFGHJKLZXCVBNMЙЦУКЕНГШЩЗХЪЁФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
template = 'Предложение № {0}, слово с заглавной буквы № {1} - это "{2}".\n'

def open_file():
    f = open("oister.txt", 'r', encoding = "utf-8")
    st = f.read()
    f.close()
    return st


def clean(st):
    arr_dirty = st.replace('.,!?…', '.').split('.')
    arr_cleaner = [sentence.replace(symbols, '') for sentence in arr_dirty]
    arr_less_10 = [sentence for sentence in arr_cleaner if len(sentence.split()) >= 10]
    arr = [sentence.split() for sentence in arr_cleaner]
    return arr


def find_capitals(arr):
    for indx, sentence in enumerate(arr):
                i = 0
                for word in sentence:
                    if word[0] in capital_letters:
                        i += 1
                        print(template.format(indx + 1, i, word))


def main():
    st = open_file()
    arr = clean(st)
    find_capitals(arr)
    
	
main()
