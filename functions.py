import json
from typing import Dict


def load_post(path, s):
    """Загружает посты из файла и ищет нужный"""
    with open(path, 'r', encoding='utf-8') as file:
        list_posts = json.load(file)
        file.close()
        for post in list_posts:
            single_post = post["content"].split(" ")
            s_one = "#" + s.lower()
            s_two = "#" + s.title()

            if s in single_post or s_two in single_post or s_one in single_post:
                return post
            else:
                pass
        return "Нет поста"


"""
def read_in_file():
    with open("posts.json", "r") as file:
        list_posts = json.load(file)
        file.close()
        return list_posts
"""


def write_in_file(picture, content):
    with open('posts.json', "r", encoding='utf-8') as file:
        list_posts = json.load(file)
        new_data = ({'pic': picture, 'content': content})
        list_posts.append(new_data)
        file.close()
    with open("posts.json", "w", encoding='utf-8') as write_file:
        json.dump(list_posts, write_file)
        write_file.close()






