import json
import time

import redis
from flask import Flask

app = Flask(__name__)
r = redis.Redis(host='redis-server', port=6379, decode_responses=True)


@app.route('/')
def say_hello():
    data = r.get('index')
    if data is not None:
        data = json.loads(data)
        # 600 seconds == 10 minutes
        if time.time() - data['time'] <= 600:
            return data['html']

    data = (
        '<p>Hello, World, I am a Flask app!</p>'
        '<p><a href="/about">About this app</a></p>'
    )
    r.set('index', json.dumps({'html': data, 'time': time.time()}))
    return data


@app.route('/about')
def about():
    data = r.get('about')
    if data is not None:
        data = json.loads(data)
        # 600 seconds == 10 minutes
        if time.time() - data['time'] <= 600:
            return data['html']

    data = (
        '<p>This application is running on the Flask web framework.</p>'
        '<p>Learn more about Flask here: '
        '<a href="https://flask.palletsprojects.com/">Flask documentation</a></p>'
        '<p><a href="/">Back to home</a></p>'
    )
    r.set('about', json.dumps({'html': data, 'time': time.time()}))
    return data
