from flask import Flask

app = Flask(__name__)


@app.route('/')
def say_hello():
    return (
        '<p>Hello, World, I am a Flask app!</p>'
        '<p><a href="/about">About this app</a></p>'
    )


@app.route('/about')
def about():
    return (
        '<p>This application is running on the Flask web framework.</p>'
        '<p>Learn more about Flask here: '
        '<a href="https://flask.palletsprojects.com/">Flask documentation</a></p>'
        '<p><a href="/">Back to home</a></p>'
    )
