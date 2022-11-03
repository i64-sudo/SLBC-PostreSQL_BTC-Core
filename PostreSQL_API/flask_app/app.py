#!/usr/bin/python3
from flask import Flask
from flask import request
import psycopg2
import logging
from waitress import serve

def RAN(password, host, port, final_balance, address, dbname, user):
    app = Flask(__name__)

    log = logging.getLogger('werkzeug')
    log.disabled = True
    app.logger.disabled = True

    conn = psycopg2.connect(dbname=dbname, user=user,

                            password=password, host=host, port=port)

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

    app.debug = True
    app.run()