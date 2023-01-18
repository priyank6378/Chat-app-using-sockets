import create_socket
import threading
import socket

address = ('localhost' , 11111)

client = create_socket.create_client_socket(address[0] , address[1])

def send_msg():
    while True:
        msg = input("enter message: ")
        ret = client.send(bytes(msg, 'utf-8'))
        if not ret:
            break


def recv_msg():
    while True:
        msg = client.recv(4096)
        if not msg:
            break
        # if msg.decode().split(':')[0].strip() == socket.gethostbyname(address[0]):
        #     continue
        print(msg)


if __name__ == '__main__':
    sending_thred = threading.Thread(target=send_msg)
    receving_thread = threading.Thread(target=recv_msg)
    sending_thred.start()
    receving_thread.start()