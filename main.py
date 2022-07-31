import random, time
from flask import Flask, request, send_from_directory
import requests, os, socket
from constants import GATEWAY_FQDN
app = Flask(__name__)
random.seed(5991)

@app.route('/dashboard/<path:path>', methods=['GET'])
def dashboard(path):
    return send_from_directory('dashboard', path)

@app.route('/api', methods=['GET'])
def api():
    # not ideal, but postback so we can use Docker's internal networking easier.
    return requests.get(f"http://{GATEWAY_FQDN}/proxy/room-reader/room").json()

@app.route('/api/<name>', methods=['GET'])
def room_api(name:str):
    # not ideal, but postback so we can use Docker's internal networking easier.
    return requests.get(f"http://{GATEWAY_FQDN}/proxy/room-reader/room/{name}").json()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80 if os.environ.get("CONTAINER", False) else 5000)