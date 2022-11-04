# Notice: The HTTP/Flask version that hosts is EXTREMELY buggy when it comes to using under multiple connections (threads) under the same IP
# Flask: Was never intended to run multiple connections under a single IP:DNS and thus causes some issues.
# Issues: There is a slight issue with Data Leaks AKA 1 Connections (1 Threads) data being leaked to another thus mixing up the return values.
# Issue2: This first issue is only affected when multiple connections are made at the EXACT same time, So only run 1 Thread with 1 Connection at a time.

# Fix?: We highly suggest using the PostgreSQL_API instead of the PostgreSQL_HST/Flask-App, The PostgreSQL_API is much more reliable and faster and has 0 Issues right now.

from flask import Flask, request
import psycopg2
app = Flask(__name__)

final_balance = 'balance'
address = 'address'
conn = psycopg2.connect(dbname="bitcoin", user='postgres',
                        password='1234', host='localhost', port=5432)
cursor = conn.cursor()
table = "hunter"

def get_transaction_by_wallet(wallet):
    return "1"

def get_wallet_info(wallet):
    query = "SELECT * FROM " + table + " WHERE address = '" + wallet + "';"
    cursor.execute(query)
    try:
        res = cursor.fetchall()
        return res[0]
    except: 
        return ['0', '0']

@app.route('/balance')
def parse_wallet():
    btc_wallet_list = request.args['active'].split(',')
    result = "{"
    for wallet in btc_wallet_list:
        wallet_info = get_wallet_info(wallet)
        balance = wallet_info[1]
        address = wallet_info[0]
        result += "\"" + str(wallet) + "\":{\"final_balance""\"" + ":" + balance  + "},"
    result = result[:-1] + "}"
    result = result.replace("None", "0")
    response = app.make_response(result)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response 

@app.route("/get")
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.debug = True
    app.run()