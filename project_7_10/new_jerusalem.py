import urllib.request
import re
import time
import html
import os
import csv
import sys


trash = 'ИМЕНА БИБЛИОТЕКА ИЕРУСАЛИМСКОГО ЖУРНАЛА БЛАГОДАРИМ'


regSpace = re.compile('\s{2,}', re.DOTALL)


time.sleep(2)


class web_articles:
    def __init__(self, url, name, author):
        self.url = url
        self.name = name
        self.author = author
        

class web_categories:
    articles = []
    def __init__(self, name, html):
        self.name = name
        self.html = html

        

class web_pages:
    categories = []
    def __init__(self, url, year, number):
        self.url = url
        self.year = year
        self.number = number


def find_urls():

    pages = []
    
    page = urllib.request.urlopen('http://magazines.russ.ru/ier/2017/56')
    page_read = page.read().decode('utf-8')

    reg_journals = re.compile('<td><a href="/ier/([0-9]{4})/([0-9]{2})">[0-9]*?</a></td>')
    years_numbers = reg_journals.findall(page_read)

    for year_number in years_numbers:
        year = year_number[0]
        number = year_number[1]
        url = 'http://magazines.russ.ru/ier/' + year + '/' + number

        page = web_pages(url, year, number)

        pages.append(page)

    return pages


def find_categories(url):   
    categories = []

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
       html = response.read().decode('utf-8')
   
    reg_categories = re.compile('(([А-ЯЁ ]*)</h6>.*?(<h6>)|(</div><!--end page-->))', flags= re.DOTALL)
    titles = reg_categories.findall(html)

    for title in titles:
        if title[1] not in trash and 'href' in title[0]:
            name = title[1]
            html = title[0]
            categories.append(web_categories(name, html))

    return categories


def find_articles(html):
    articles = []
    reg_categories = re.compile('<strong>(.*?)</strong>(\s)*<a href="(.*?)">(.*?)</a>')
    titles = reg_categories.findall(html)

    for title in titles:
        url = 'http://magazines.russ.ru' + title[2]
        name = title[3]
        author = title[0]
        articles.append(web_articles(url, name, author))

    return articles


def get_text(url):
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
       html = response.read().decode('utf-8')


    regTag = re.compile('<.*?>', re.DOTALL)
    regScript = re.compile('<script.*?>.*?</script>', re.DOTALL)
    regComment = re.compile('<!--.*?-->', re.DOTALL)
    regN = re.compile('\n{2,}', re.DOTALL)
    regSpace = re.compile(' {2,}', re.DOTALL)
    regAnd = re.compile('&.*?;', re.DOTALL)
    regBlank = re.compile('\s{2,}', re.DOTALL)

    clean_html = regScript.sub("", html)
    clean_html = regComment.sub("", clean_html)
    clean_html = regTag.sub("", clean_html)
    clean_html = clean_html.replace('*', '')
    clean_html = regAnd.sub("", clean_html)
    clean_html = regSpace.sub(" ", clean_html)
    clean_html = regN.sub("\n", clean_html)
    clean_html = regBlank.sub("\n", clean_html)

    reg_versia_pechati = re.compile('\nВерсия для печати.*', re.DOTALL)
    reg_jer_journal = re.compile('(\n)?Журнальный зал:.*Опубликовано в журнале:.*?[0-9 ,]+\n', re.DOTALL)
    try:
        clean_html = reg_versia_pechati.sub("", clean_html)
    except:
        return 

    try:
        clean_html = reg_jer_journal.sub("", clean_html)
    except:
        return 
    
    return clean_html


def folders(page, category, article, text):
        
        root = 'Иерусалимский_журнал'
        category_new = category.name.replace(' ', '_').replace('.', '').replace('"', '').replace('«', '').replace('»', '').replace('!', '').replace(',', '').replace('?', '')
        article_new = article.name.replace(' ', '_').replace('.', '').replace('"', '').replace('«', '').replace('»', '').replace('!', '').replace(',', '').replace('?', '')
        
        os.path.abspath('.')
        
        path = root + os.sep + 'plain' + os.sep + page.year + os.sep + page.number + os.sep + category_new
        path_2 = root + os.sep + 'mystem-xml' + os.sep + page.year + os.sep + page.number + os.sep + category_new
        path_3 = root + os.sep + 'mystem-plain' + os.sep + page.year + os.sep + page.number + os.sep + category_new 
        if not os.path.exists(path):
            os.makedirs(path)
        if not os.path.exists(path_2):
            os.makedirs(path_2)
        if not os.path.exists(path_3):
            os.makedirs(path_3)
            
        f = open(path + os.sep + article_new + '.txt', 'w', encoding = "utf-8")
        f.write(text)

        os.system(r"./mystem " + "-c -d " + path + os.sep + article_new + '.txt' + " " + path_2 + os.sep + article_new + '.xml')
        os.system(r"./mystem " + "-c -d " + path + os.sep + article_new + '.txt' + " " + path_3 + os.sep + article_new + '.txt')

        f.close()
        f = open(path + os.sep + article_new + '.txt', 'w', encoding = "utf-8")
        if article.author == '':
            f.write('@au Noname\n' + '@ti ' + article.name + '\n' + '@da ' + page.year + '\n' + '@topic ' + category.name + '\n' + '@url ' + article.url + '\n' + text)
        else:
            f.write('@au ' + article.author + '\n' + '@ti ' + article.name + '\n' + '@da ' + page.year + '\n' + '@topic ' + category.name + '\n' + '@url ' + article.url + '\n' + text)
        f.close()


def csv_create(page, category, article):
    print('love')


def main():
    
    pages = find_urls()
    
    for page in pages:
        page.categories = find_categories(page.url)
        for category in page.categories:
            category.articles = find_articles(category.html)

    os.path.abspath('.')
    if not os.path.exists('Иерусалимский_журнал'):
        os.makedirs('Иерусалимский_журнал')
    csvfile = open('Иерусалимский_журнал/metadata.csv', 'w', encoding = 'utf-8')
    writer = csv.writer(csvfile, delimiter='\t')
    row_common = ['', '', 'публицистика', '', '', '', 'нейтральный', 'н-возраст', 'н-уровень', 'республиканская', 'Иерусалимский_журнал', '', 'газета', 'Россия', 'Иерусалим', 'ru']
    rows = []
    for page in pages:
        for category in page.categories:
            for article in category.articles:
                row = []
                path = 'Иерусалимский_журнал' + os.sep + 'plain' + os.sep + page.year + os.sep + page.number + os.sep + category.name.replace(' ', '_').replace('.', '').replace('"', '').replace('«', '').replace('»', '').replace('!', '').replace(',', '').replace('?', '') + os.sep + article.name.replace(' ', '_').replace('.', '').replace('"', '').replace('«', '').replace('»', '').replace('!', '').replace(',', '').replace('?', '') + '.txt'

                row.append(path)
                if article.author == '':
                    row.append('Noname')
                else:
                    row.append(article.author)
                for i in range(2):
                    row.append(row_common[i])
                row.append(article.name)
                row.append('unknown')
                for i in range(2, 5):
                    row.append(row_common[i])
                row.append(category.name)
                for i in range(5, 10):
                    row.append(row_common[i])
                row.append(article.url)
                for i in range(10, 12):
                    row.append(row_common[i])
                row.append(page.year)
                for i in range(12, len(row_common)):
                    row.append(row_common[i])

                rows.append(row)
    writer.writerows(rows)
                
    csvfile.close()

    for page in pages:
        for category in page.categories:
            for article in category.articles:
                folders(page, category, article, get_text(article.url))

    

main()
