import _pickle as pickle
from _thread import *
from socket import *

'''
W tym pliku należy uzupełnić wątek threaded_client
Należy również zmodyfikować adres IP w zmiennej 'HOST' na swój z sieci lokalnej
'''

HOST = "localhost"
PORT = 8999

connections = 0

s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

try:
    s.bind((HOST, PORT))
except error as e:
    print(str(e))
try:
    s.listen(4)  # max. 4 users in queue
except error as e:
    print(str(e))
print("Waiting for a connection")


def threaded_client(connection, my_id):

    while True:
        data = pickle.loads(connection.recv(2048))
        print(data, my_id)

clientCounter = 0
while True:
    client, addr = s.accept()

    start_new_thread(threaded_client, (client, clientCounter))
    clientCounter += 1