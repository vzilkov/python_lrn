#!/usr/bin/python3           # This is client.py file

import socket
import datetime
from time import sleep
import tkinter
# create a socket object

host = '192.168.102.175' #socket.gethostname()
port = 9999
# connection to hostname on the port.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

main_window = tkinter.Tk()


def connect_btn():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    data_str = main_window_textbox_ip.get()
    print('str data is: ', data_str)
#host has standart IP
    s.connect((data_str, port))
    print('socket opened')


def discon_btn():
    s.close()
    print('socket closed')


main_window.geometry("900x400")

main_window_btn_connect = tkinter.Button(main_window, text='Connect', command=connect_btn)
main_window_btn_connect.grid(row=0, column=0)

main_window_lable_ip_connect = tkinter.Label(main_window, text='Connect to:')
main_window_lable_ip_connect.grid(row=0, column=1)

main_window_textbox_ip = tkinter.Entry(main_window) #ENTRY is an one line textbox
main_window_textbox_ip.insert(0, host)
main_window_textbox_ip.grid(row=0, column=2)

main_window_btn_disconnect = tkinter.Button(main_window, text='Close', command=discon_btn)
main_window_btn_disconnect.grid(row=1, column=0)

main_window_text_data_output = tkinter.Text(main_window)
main_window_text_data_output.insert(tkinter.INSERT, 'Hello')
main_window_text_data_output.grid(row=2, column=0)

main_window.mainloop()

while True:

    time_cur = datetime.datetime.now()
    print(time_cur)

    # Receive no more than 1024 bytes
    msg = s.recv(1024)

    print(msg.decode('ascii'))

    sleep(0.5)