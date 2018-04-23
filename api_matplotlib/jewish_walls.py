import urllib.request
import json
import datetime
import matplotlib
import matplotlib.pyplot as plt

def file_write(text):
    try:
        file = open('jewish_wall.txt', 'r', encoding = "utf-8")
        file_text = file.read()
        file.close()
    except FileNotFoundError:
        file = open('jewish_wall.txt', 'w', encoding = "utf-8")
        file.write(text)
        file.close()
    else:
        file = open('jewish_wall.txt', 'w', encoding = "utf-8")
        file.write(file_text)
        file.write('\n')
        file.write(text)
        file.close()

def draw_everyting(lengths, ages, cities):
    f, (graph_lengths, graph_ages, graph_cities) = plt.subplots(1, 3)

    for post in lengths:
        graph_lengths.scatter(post[0], post[1], s=20, c='red')
    graph_lengths.set_xlabel("Длина поста")
    graph_lengths.set_title("Пост-Коммент")

    ages_dict = {}
    
    for post in ages:
        if (post[0] < 120) and (post[0] not in ages_dict):
            ages_dict[post[0]] = [1, post[1]]
        elif (post[0]) < 120:
            ages_dict[post[0]][1] = ((ages_dict[post[0]][0] * ages_dict[post[0]][1]) + post[1]) 
            ages_dict[post[0]][0] += 1
            ages_dict[post[0]][1] = ages_dict[post[0]][1]/ages_dict[post[0]][0]
    
    for age in sorted(ages_dict):
        graph_ages.bar(age, ages_dict[age][1])
    graph_ages.set_xlabel("Возрасты")
    graph_ages.set_title("Возраст-Коммент")

    cities_dict = {}

    for post in cities:
        if post[0] not in cities_dict:
            cities_dict[post[0]] = [1, post[1]]
        else:
            cities_dict[post[0]][1] = ((cities_dict[post[0]][0] * cities_dict[post[0]][1]) + post[1]) 
            cities_dict[post[0]][0] += 1
            cities_dict[post[0]][1] = cities_dict[post[0]][1]/cities_dict[post[0]][0]

    x = 0
    for city in sorted(cities_dict):
        graph_cities.bar(x, cities_dict[city][1])
        x += 1
    graph_cities.set_xlabel("Города")
    graph_cities.set_xticklabels(sorted(cities_dict))
    graph_cities.set_ylabel("Средняя длина комментария")
    graph_cities.set_title("Город-Коммент")
    graph_cities.yaxis.set_label_position('right')
    plt.show()

def main():
    offset = 0
    post_info = []
    lengths = []
    ages = []
    cities = []
    post_id = ''
    while offset < 200:
        post_req = urllib.request.Request('https://api.vk.com/method/wall.get?owner_id=-732033&v=5.74&access_token=d57c41d9d57c41d9d57c41d9cad51e0496dd57cd57c41d98fa1c8449133f6ce263b50c1&count=100&offset=' + str(offset))    
        post_response = urllib.request.urlopen(post_req)
        post_result = post_response.read().decode('utf-8')
        post_data = json.loads(post_result)
        post_info += post_data['response']['items']
        for post in post_data['response']['items']:
            post_id = int(post['id'])
            offset_comm = 0
            file_write(post['text'])

            post_length = len(post['text'].split())

            comment_quantity = 0
            comment_length_summary = 0
            average_comment_length = 0
            
            while offset_comm < 200:
                req_comm = urllib.request.Request('https://api.vk.com/method/wall.getComments?owner_id=-732033&post_id=' + str(post_id) + '&v=5.74&access_token=d57c41d9d57c41d9d57c41d9cad51e0496dd57cd57c41d98fa1c8449133f6ce263b50c1&count=100&offset=' + str(offset))
                response_comm = urllib.request.urlopen(req_comm)
                comm_result = response_comm.read().decode('utf-8')
                comm_data = json.loads(comm_result)
                comment_quantity += comm_data['response']['count']
        
                for comment in comm_data['response']['items']:
                    file_write(comment['text'])

                    comment_length = len(comment['text'].split())
                    commenter_id = comment['from_id']
                    if int(commenter_id) >= 0:
                        user_req = urllib.request.Request('https://api.vk.com/method/users.get?user_ids=' + str(commenter_id) + '&fields=bdate,home_town&v=5.7&access_token=d57c41d9d57c41d9d57c41d9cad51e0496dd57cd57c41d98fa1c8449133f6ce263b50c1')
                        user_response = urllib.request.urlopen(user_req)
                        user_result = user_response.read().decode('utf-8')
                        user_data = json.loads(user_result)
                        try:
                            user_city = user_data['response'][0]['home_town']
                            if user_city != '':
                                cities.append([user_city, comment_length])
                        except KeyError:
                            user_city = ''
                        try:
                            user_age = 2018 - int(str(user_data['response'][0]['bdate']).split('.')[-1])
                            ages.append([user_age, comment_length])
                        except KeyError:
                            user_age = 0
                    comment_length_summary += comment_length
                offset_comm += 100
            if comment_quantity != 0:
                average_comment_length = comment_length_summary/comment_quantity
               
            lengths.append([post_length, average_comment_length])
        offset += 100

        draw_everyting(lengths, ages, cities)
        

main()
