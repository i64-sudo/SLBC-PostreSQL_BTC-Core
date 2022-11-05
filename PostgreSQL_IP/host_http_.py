#!/usr/bin/python3
from flask import Flask
from flask import request
import socket
import logging
from waitress import serve
#from gevent.pywsgi import WSGIServer

app = Flask(__name__)

final_balance = 'final_balance'
number_transaction = 'n_tx'
total_received = 'total_received'

CONN_HOST = "127.0.0.1"
CONN_PORT = 5959

def get_transaction_by_wallet(wallet):
    return "1"

def get_wallet_info(wallet):
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((CONN_HOST, CONN_PORT))
    clientSocket.send(wallet.encode())
    dataFromServer = clientSocket.recv(1024)
    dataFromServer_DECODED = dataFromServer.decode("utf-8")
    dataRECV = dataFromServer_DECODED.split()
    #return ['0','0','0','0']
    
    #res = cursor.fetchall()
    #print(res)
    #if len(res) == 0:
    #    return ['0', '0', '0', '0']
    #else:
    #    return res[0]
    try:
        res = [wallet, dataRECV[0]]
        #print(res[0])
        return res[0]
    except: 
        return ['0', '0', '0', '0']

@app.route('/balance')
def parse_wallet():
    btc_wallet_list = request.args['active'].split(',')
    result = "{"
    for wallet in btc_wallet_list:
        wallet_info = get_wallet_info(wallet)
        transaction_sum = 0
        n_transaction = 0
        balance = wallet_info[1]
        result += "\"" + str(wallet) + "\":{\"" + final_balance + "\":" + str(balance) + ",\"" + number_transaction + "\":" + str(n_transaction) + ",\"" + total_received + "\":" + str(transaction_sum) + "},"
    result = result[:-1] + "}"
    result = result.replace("None", "0")
    response = app.make_response(result)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response 


@app.route("/get")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    #app.run(host= '0.0.0.0')
    logging.getLogger('waitress').setLevel(logging.ERROR)
    serve(app, host='0.0.0.0', port=7777)

    #serve(app)
    #http_server = WSGIServer(('', 5000), app)
    #http_server.serve_forever()