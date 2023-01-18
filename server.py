from ast import arg
from matplotlib.font_manager import list_fonts
import create_socket
import threading
from collections import deque

server = create_socket.create_server_socket('localhost', 11111)
server.listen()
list_of_div = []

messages = deque()

def accept_connection():
    while True:
        client, address = server.accept()
        list_of_div.append((client, address))
        print("connection from :",address)
        manage_device((client, address))

def manage_device(device):
    # device = (client , address)
    device_recv = threading.Thread(target=recv_msg, args=[device])
    device_recv.start()

def recv_msg(device):
    client = device[0]
    while True:
        msg = client.recv(4096)
        if not msg:
            print("connection closed :", device[1])
            client.close()
            break
        msg = device[1][0] + ' : ' + msg.decode()
        messages.append(bytes(msg, 'utf-8'))

def broadcast_message():
    while True:
        if len(messages)>0:
            msg = messages.popleft()
            print(msg)
            for device in list_of_div:
                device[0].send(msg)

if __name__ == "__main__":
    connection_thread = threading.Thread(target=accept_connection)
    connection_thread.start()
    broadcast_message_thread = threading.Thread(target=broadcast_message)
    broadcast_message_thread.start()