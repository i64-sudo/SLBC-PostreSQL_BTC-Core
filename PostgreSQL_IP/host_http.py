from flask import Flask, request
import socket
app = Flask(__name__)

CONN_HOST = "127.0.0.1"
CONN_PORT = 5959

def get_wallet_info(wallet):
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((CONN_HOST, CONN_PORT))
    clientSocket.send(wallet.encode())
    dataFromServer = clientSocket.recv(1024)
    dataFromServer_DECODED = dataFromServer.decode("utf-8")
    dataRECV = dataFromServer_DECODED.split()
    try:
        return str(f"{dataRECV[1]}")
    except:
        return str("0")

@app.route('/balance')
def parse_wallet():
    btc_wallet_list = request.args['active'].split(',')
    s = get_wallet_info(wallet=btc_wallet_list[0])
    return str(s)

@app.route("/get")
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.debug = True
    app.run()