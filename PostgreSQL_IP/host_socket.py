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

print(f"[+] Socket host is running on {HOST}:{PORT}")
while(True):
    (clientConnected, clientAddress) = serverSocket.accept()
    print("Accepted a connection request from %s:%s"%(clientAddress[0], clientAddress[1]))
    dataFromClient = clientConnected.recv(1024)
    dataFromClient_DECODED = dataFromClient.decode()
    GET_DATABASE_REQUEST = GetBTC(addrU=dataFromClient_DECODED)
    clientConnected.send(bytes(f"{GET_DATABASE_REQUEST[0]} {GET_DATABASE_REQUEST[1]}", "utf-8"))
    print("Accepted a database request from %s:%s"%(clientAddress[0], clientAddress[1]))
