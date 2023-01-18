import socket
import sys

def create_server_socket(host, port):
    sender = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sender.bind((host, port))
    except:
        print("Error!")
        print("Try again...")
        # sys.exit(1)
    return sender

def create_client_socket(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
    except:
        print("Error!")
        print("Try again...")
        # sys.exit(1)
    return s