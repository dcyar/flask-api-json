import json


def get_posts():
    with open('data.json') as json_file:
        posts = json.load(json_file)

    return posts
