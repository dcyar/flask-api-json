from flask import Flask, jsonify, request
from posts import get_posts

app = Flask(__name__)


@app.route('/posts/')
def main():
    posts = get_posts()

    return jsonify(posts), 200


@app.route('/posts/<int:index>/')
def get_post(index):
    posts = get_posts()
    post = posts[index] if len(posts) > index else "404"

    return jsonify(post), 200


@app.route('/posts/', methods=['POST'])
def add_post():
    post = request.get_json()

    posts = get_posts()

    posts.append(post)

    return jsonify(posts), 201


@app.route('/posts/<int:index>/', methods=['DELETE'])
def del_post(index):
    posts = get_posts()
    posts.pop(index)

    return jsonify(posts), 200


app.run()
