import requests
from flask import Flask
app = Flask(__name__)

ipaddress = 'http://192.168.1.69:9876'


@app.route('/', methods=['GET'])
def get_data():
    return requests.get(ipaddress).content

fowards = '/hits/forwards'
@app.route(fowards, methods=['GET'])
def move_forwards():
    return requests.get(ipaddress + fowards).content

motor = '/motor'
@app.route(motor, methods=['GET'])
def motor_move():
    return requests.get(ipaddress + motor).content

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8899, debug=True)