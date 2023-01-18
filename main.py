from ipaddress import ip_address
import tkinter as tk
from tkinter import Text, ttk
import create_socket
import threading
import socket

port_number = '11111'
server_ip_address = 'localhost'

client = None

def recv_msg():
    while True and client:
        msg = client.recv(4096)
        if not msg:
            break
        # if msg.decode().split(':')[0].strip() == socket.gethostbyname(server_ip_address):
        #     continue
        reply_entry.insert('end', msg.decode() + '\n')

def send():
    if client :
        data = message.get()
        client.send(bytes(data, 'utf-8'))

def start():
    tmp_ip_addr = ip_address.get()
    tmp_port_num = port.get()
    if tmp_ip_addr and tmp_port_num:
        global server_ip_address
        global port_number
        server_ip_address = tmp_ip_addr
        port_number = tmp_port_num
        global client 
        client = create_socket.create_client_socket(tmp_ip_addr, int(tmp_port_num))
        recv_msg_thread = threading.Thread(target=recv_msg)
        recv_msg_thread.start()


root = tk.Tk()
root.title("Chat App")
main_frame = ttk.Frame(root)
main_frame.grid(column=0, row=0)


ttk.Label(main_frame, text="IP: ").grid(column=0,row=0)
ttk.Label(main_frame, text="PORT: ").grid(column=2,row=0)
ip_address = tk.StringVar(value=server_ip_address)
port = tk.StringVar(value=port_number)
ip_entry = ttk.Entry(main_frame, textvariable=ip_address, width=10)
ip_entry.grid(column=1,row=0)
port_entry = ttk.Entry(main_frame, textvariable=port, width=10)
port_entry.grid(column=3,row=0)
ttk.Button(main_frame, text="Start", command=start).grid(column=4,row=0)

ttk.Label(main_frame, text="Message: ").grid(column=0,row=1)
message = tk.StringVar()
message_entry = ttk.Entry(main_frame, textvariable=message, width=10)
message_entry.grid(column=1,row=1,columnspan=2)
ttk.Button(main_frame, text='Send', command=send).grid(column=3,row=1)
ttk.Label(main_frame, text="Reply: ").grid(column=0,row=2)

reply_entry = Text(main_frame, width=20, height=10, wrap='word')
reply_entry.grid(column=1,row=2, rowspan=3)


for child in main_frame.winfo_children():
    child.grid_configure(padx=3, pady=3)

main_frame.bind('<Return>', send)
message_entry.focus()

root.mainloop()