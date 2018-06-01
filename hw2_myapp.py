import telebot
import random
import conf
import flask
from pymystem3 import Mystem
m = Mystem()


punctuation = '\'"/.,<>:;[]{}\\|1234567890`~!@#$%^&*()_+-=?!«»…—'


WEBHOOK_URL_BASE = "https://{}:{}".format(conf.WEBHOOK_HOST, conf.WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/{}/".format(conf.TOKEN)


bot = telebot.TeleBot(conf.TOKEN, threaded=False)
bot.remove_webhook()
bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH)


app = flask.Flask(__name__)

stickers = []



@bot.message_handler(commands=['start', 'help'])
def info(message):
    user = message.chat.id
    bot.send_message(user, 'Привет, этот бот  отвечает предложением, в котором все слова заменены на какие-то случайные другие слова той же части речи и с теми же грамматическими характеристиками, что и в вашем предложении, или кидает рандомный стикер.')


def get_word_list():
    f = open("1grams-3.txt", 'r', encoding = "utf-8")
    word_list = f.read().split()
    f.close()
    return word_list


def get_grammar(word):
    word_grammar = ''
    if 'analysis' in m.analyze(word)[0]:
        if m.analyze(word)[0]['analysis'] != []:
            word_grammar = m.analyze(word)[0]['analysis'][0]['gr']
        else:
            word_grammar = 'non existent'
    else:
        word_grammar = 'non existent'

    return word_grammar


@bot.message_handler(content_types=['text'])
def random_word(message):
    text = message.text

    original_words = text.split()
    word_list = get_word_list()
    original_words_grammar = []
    new_words = original_words
    random.shuffle(word_list)
    word_quantity = len(original_words)
    for original_word in original_words:
        original_words_grammar.append(get_grammar(original_word))
    for random_word in word_list:
        if word_quantity == 0:
            break
        random_word_grammar = get_grammar(random_word)
        if random_word_grammar in original_words_grammar:
            for i, original_word in enumerate(original_words):
                if original_words_grammar[i] == random_word_grammar:
                    new_words[i] = random_word
                    if original_word[-1] in punctuation:
                        new_words[i] += original_word[-1]
                    if original_word[0] in punctuation:
                        new_words[i] = original_word[0] + new_words[i]
                    original_words_grammar[i] = 'already new'
                    word_quantity -= 1
                    if len(original_word) >= 3:
                        break


    user = message.chat.id
    masha = 251564037
    new_text = ''
    for new_word in new_words:
        new_text += new_word + ' '
    new_text = new_text.capitalize()
    bot.send_message(user, new_text)
    if user != masha:
        bot.send_message(masha, text + '\n' + new_text + '\n' + str(user))


@bot.message_handler(content_types=['sticker'])
def sticker_police(message):
    user = message.chat.id
    masha = 251564037
    stickers.append(message.sticker.file_id)
    sticker_to_send = random.choice(stickers)
    bot.send_sticker(user, sticker_to_send)
    if user != masha:
        bot.send_sticker(masha, sticker_to_send)
        bot.send_message(masha, str(user))


@app.route('/', methods=['GET', 'HEAD'])
def index():
    return 'please, visit the telegram bot @masha_first_bot'


@app.route(WEBHOOK_URL_PATH, methods=['POST'])
def webhook():
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        flask.abort(403)

