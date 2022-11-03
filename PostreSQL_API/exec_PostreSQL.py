import flask_app.app

# Server Info #
password='1234'
host='localhost'
port=5432
final_balance = 'balance'
address = 'address'
dbname="bitcoin"
user='postgres'

if __name__ == "__main__":
    flask_app.app.RAN(password, host, port, final_balance, address, dbname, user)