import requests
from flask import Flask
app = Flask(__name__)


@app.route('/')
def test():
    return "hello world"

@app.route('/some-url')
def get_data():
    return requests.get('http://example.com').content

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8888, debug=True)