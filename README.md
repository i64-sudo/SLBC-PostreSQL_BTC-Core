## ![alt text](https://raw.githubusercontent.com/Zurek0x/SLBC-PostreSQL_BTC-Core/main/readme.data/postgresql-monitoring-.webp)
## ✅Short Length Bitcoin Core - Better Bitcoin Core✅
Short Length Bitcoin Core or *SLBC* is a clone of the Bitcoin Core that has been shortened, compressed, cutted and applied to PostgreSQL Database, Unlike the Bitcoin Core that is 400Gb that stores ***Transactions, Wallets, Wallet ID's, Blocks, Hashes, Etc*** Our database only contains the functional requirements for most public projects like ***Wallets, Wallet ID's, Wallet Balances, Etc***.

## ✅File Comparisons✅
> * **Bitcoin Core (2009 - 2023 - Uncompressed) - 400GB**
> * **Bitcoin Core Contains [:Transactions, Wallets, Wallet ID's, Transaction Blocks, Mneomic Phrases, Etc:]**
> * **PostreSQL Core (2009 - 2023 - Compressed) - 26-33GB**
> * **PostreSQL Core Contains [:Wallets, Wallet ID's, Balances:]**


## ✅Block Installation✅
We utilize what we call BLOCKS for our database, Essentially we dump the bitcoin core **400Gb** and swap out everything only for the essentials we need like ***Wallets, Wallet ID's, Wallet Balances*** Saving us over **370Gb of Data** and publish it under a specific date, We dump new BLOCKS every day or two at the link here -> **http://addresses.loyce.club/**

## ✅Support✅
* **Windows 10/11 22H1+22H2 (TESTED - OK)**
* **Debian Based Linux Distro's (Ubuntu/Lubuntu/Debnian TESTED - OK)**

## ✅SETUP✅

## ℹ️ NOTICE ℹ️
**This ISN'T a guide on how to fully setup a bitcoin database, We are just providing the necessary info to setup and start a server for beginners, For long term support you will need Basic > Advanced knowledge with Python & PostgreSQL to insure that
Your server is running well, Your database is running well and to fix issues and bugs that may occur.
If there is a minor error, Do not create a issue in our issues tab.**

## ℹ️ Install PostgreSQL ℹ️

https://github.com/Zurek0x/SLBC-PostreSQL_BTC-Core/blob/main/readme.data/185788464-b4d02e62-1069-4a29-83d4-95bb2cbc9e51.mp4

## ℹ️ Create Table ℹ️
```sql
CREATE TABLE hunter(
address VARCHAR(80) not null,
balance VARCHAR(30) not null
);
```
https://github.com/Zurek0x/SLBC-PostreSQL_BTC-Core/blob/main/readme.data/185788481-044d26ed-213e-4a86-8c8d-118395f85225.mp4


## ℹ️ Install Flask psycopg2 waitress ℹ️
```python
pip install flask
pip install psycopg2
pip install waitress
```
https://github.com/Zurek0x/SLBC-PostreSQL_BTC-Core/blob/main/readme.data/185788486-e08b1685-db89-4af1-b6a5-9267798ac20c.mp4


## ℹ️ Import and Use ℹ️

Import your list off addresses with Balance.The  first time that you try to import PostgreSQL will give you error reguarding Binary Path in the Preferences dialog. To Resolve  Correct The Binary Path pgAdmin 4  PostgreSQL 14. We need to set the bin path of the PostgreSQL installation which is not done at the time of installation. You will need to update the PATH on your PostgreSQL. 

```
C:\Program Files\PostgreSQL\15\bin
```

https://github.com/Zurek0x/SLBC-PostreSQL_BTC-Core/blob/main/readme.data/185788493-6b38bdbd-d327-4606-926d-54c2ea898cb1.mp4 ❗**VIDEO IS GLITCHED, DOWNLOAD TO WATCH**❗

# 💡 Index Database 💡

You will Find Without indexing the Databse the Request will be slow. More Information ( https://www.tutorialspoint.com/postgresql/postgresql_indexes.htm )

## 💥Unique Indexes💥

Unique indexes are used not only for performance, but also for data integrity. A unique index does not allow any duplicate values to be inserted into the table. The basic syntax is as follows −
```sql
CREATE UNIQUE INDEX index_name
on table_name (column_name);
```
## 💥Partial Indexes💥

A partial index is an index built over a subset of a table; the subset is defined by a conditional expression (called the predicate of the partial index). The index contains entries only for those table rows that satisfy the predicate. The basic syntax is as follows −
```sql
CREATE INDEX index_name
on table_name (conditional_expression);
```

https://github.com/Zurek0x/SLBC-PostreSQL_BTC-Core/blob/main/readme.data/185800209-0e772b64-dd85-41b3-aaec-99d0952d73e6.mp4

```sql
CREATE INDEX index_hunter
ON hunter (address, balance);
```

# 🦞API Usage🦞
The best way to use the PostgreSQL Index/Classes is to implement it within your code.
```python
# Python Example #
import psycopg2

# PostgreSQL Server Settings #
final_balance = 'balance'
address = 'address'
conn = psycopg2.connect(dbname="bitcoin", user='postgres',

                        password='1234', host='localhost', port=5432)
cursor = conn.cursor()
table = "hunter"

# Function to Get BTC and Return Value of Wallet #
def GetBTC(addrU):
    try:
        query = "SELECT * FROM " + table + " WHERE address = '" + addrU + "';"
        cursor.execute(query)
        try:
            res = cursor.fetchall()
            return res[0]
        except: 
            return ['0', '0']
    except:
        return -1

r = GetBTC("1FeexV6bAHb8ybZjqQMjJrcCrHGW9sb6uF")
print("whole value" + str(r))
print("address" + str(r[0]))
print("balance" + str(r[1]))
```
# 🦞Usage with FLASK/HTTP🦞
## ⚠️Note On Error⚠️
You must run the Socket host (host_socket.py) inside of the "PostgreSQL_IP" Folder before
Starting the flask server.
```python

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
```
# 🦞Connecting with FLASK/HTTP🦞 #
```
http://127.0.0.1:5000/balance?active=1FeexV6bAHb8ybZjqQMjJrcCrHGW9sb6uF
```
# 🦞Usage with SOCKETS & SERVER🦞 #
```python
import socket
import psycopg2

HOST = "127.0.0.1"
PORT = 5959

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((HOST,PORT))
serverSocket.listen()


final_balance = 'balance'
address = 'address'
conn = psycopg2.connect(dbname="bitcoin", user='postgres',
                        password='1234', host='localhost', port=5432)
cursor = conn.cursor()
table = "hunter"
def GetBTC(addrU):
    try:
        query = "SELECT * FROM " + table + " WHERE address = '" + addrU + "';"
        cursor.execute(query)
        try:
            res = cursor.fetchall()
            return res[0]
        except: 
            return ['0', '0']
    except:
        return -1


while(True):
    (clientConnected, clientAddress) = serverSocket.accept()
    print("Accepted a connection request from %s:%s"%(clientAddress[0], clientAddress[1]))
    dataFromClient = clientConnected.recv(1024)
    dataFromClient_DECODED = dataFromClient.decode()
    GET_DATABASE_REQUEST = GetBTC(addrU=dataFromClient_DECODED)
    clientConnected.send(bytes(f"{GET_DATABASE_REQUEST[0]} {GET_DATABASE_REQUEST[1]}", "utf-8"))
    print("Accepted a database request from %s:%s"%(clientAddress[0], clientAddress[1]))
```
# 🦞Connecting with SOCKETS & SERVER🦞 #
```python
import socket
import random
 
CONN_HOST = "127.0.0.1"
CONN_PORT = 5959

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((CONN_HOST, CONN_PORT))


data = str("1FeexV6bAHb8ybZjqQMjJrcCrHGW9sb6uF")

clientSocket.send(data.encode())
dataFromServer = clientSocket.recv(1024)
dataFromServer_DECODED = dataFromServer.decode("utf-8")
dataRECV = dataFromServer_DECODED.split()
print("whole value: " + str(dataRECV))
print("address: " + str(dataRECV[0]))
print("balance: " + str(dataRECV[1]))

while True:
    pass
```
# ⚙️Extra Information⚙️
> * ℹ️ **The SQL Language - https://www.postgresql.org/docs/current/sql.html**
> * ℹ️ **Server Administration - https://www.postgresql.org/docs/current/admin.html**
> * ℹ️ **Server Administration - https://www.postgresql.org/docs/current/admin.html**
> * ℹ️ **Client Interfaces - https://www.postgresql.org/docs/current/client-interfaces.html**
> * ℹ️ **Server Programming - https://www.postgresql.org/docs/current/server-programming.html**
> * ℹ️ **Reference - https://www.postgresql.org/docs/current/reference.html**
> * ℹ️ **Internals - https://www.postgresql.org/docs/current/internals.html**
> * ℹ️ **Appendixes - https://www.postgresql.org/docs/current/appendixes.html**

# LICENSED WITH MIT #
