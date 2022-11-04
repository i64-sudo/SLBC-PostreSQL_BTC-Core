import socket
 
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