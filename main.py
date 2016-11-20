import requests
from flask import Flask
app = Flask(__name__)


@app.route('/')
def test():
    return "hello world"

@app.route('/some-url')
def get_data():
    return requests.get('http://example.com').content