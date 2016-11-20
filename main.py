import requests
from flask import Flask
app = Flask(__name__)

ipaddress = 'http://192.168.1.69:9876'


@app.route('/')
def get_data():
    return requests.get(ipaddress).content

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8899, debug=True)