from tkinter import *
import class_can_data
can_data = class_can_data.can_data()

root = Tk()

#root.resizable(FALSE, FALSE)

#label frames:
frame_rx = LabelFrame(root, text="CAN RX")
frame_tx = LabelFrame(root, text="CAN TX")

#buttons
check_btn_var = BooleanVar(value=FALSE)
check_btn_var_light_up = BooleanVar(value=FALSE)
checkbutton_var_trace = BooleanVar(value=TRUE)

checkbutton_filters_masks = Checkbutton(frame_rx, 
                                        text='Check can filter & mask', 
                                        var=check_btn_var)

checkbutton_light_up = Checkbutton(frame_rx, text='Light up changed data', var= check_btn_var_light_up)

checkbutton_trace = Checkbutton(frame_rx, text='Fixed/Rolling trace', var= checkbutton_var_trace)

#Label
label_can_filter = Label(frame_rx, text='Filter:')

label_can_mask = Label(frame_rx, text='Mask:')

#entry
entry_can_filter = Entry(frame_rx, text='enter vals in hex 0-7FF')

entry_can_mask = Entry(frame_rx, text='enter values in hex 0-7FF')

button_tx_can_msg = Button(frame_tx, text='Transmit CAN data', height=4, font=('Courier New', 14))
label_id = Label(frame_tx, text='ID (hex):', height=4, font=('Courier New', 14))
label_len = Label(frame_tx, text='length (0..8):', height=4, font=('Courier New', 14))
label_data = Label(frame_tx, text='data (hex):', height=4, font=('Courier New', 14))
txt_id = Entry(frame_tx, width=7)

from tkinter import ttk
combobox_length = ttk.Combobox(frame_tx, values=[0,1,2,3,4,5,6,7,8], width=2, font=('Courier New', 14))
combobox_length.set(8)
txt_len = Entry(frame_tx, width=1)

txt_data = Entry(frame_tx, width=16, justify=CENTER)

#place root window to right
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
positionRight = int(root.winfo_screenwidth() - windowWidth)
positionDown = int(root.winfo_screenheight() - windowHeight)

#textbox & scrollbar:
ybar = Scrollbar(root, width=30)
textbox = Text(root, width=60, height=root.winfo_screenheight(), font=('Courier New', 16))
ybar.config(command=textbox.yview)
textbox.config(yscrollcommand=ybar.set)

#packs:
textbox.pack(side=LEFT)
ybar.pack(side=LEFT, fill=BOTH)

frame_rx.pack(side=TOP)

checkbutton_light_up.pack(side=TOP)
checkbutton_trace.pack(side=TOP)
checkbutton_filters_masks.pack(side=TOP)
label_can_filter.pack(side=TOP)
entry_can_filter.pack(side=TOP)
label_can_mask.pack(side=TOP)
entry_can_mask.pack(side=TOP)

frame_tx.pack(side=TOP)

button_tx_can_msg.pack(side=RIGHT)
label_id.pack(side=LEFT)
txt_id.pack(side=LEFT)
label_len.pack(side=LEFT)
combobox_length.pack(side=LEFT)
label_data.pack(side=LEFT)
txt_data.pack(side=LEFT)

#root.attributes('-fullscreen', True)

from class_spi_to_can import *
mcp2515 = spi_to_can_brd_exchange(1000)
mcp2515.set_config_mode(0,0)
mcp2515.set_normal_mode(500)

def period():
    global mcp2515
    print('check_errors_rec_tec', mcp2515.check_errors_rec_tec())
    rcv_can_data = mcp2515.can_rx_func()
    if rcv_can_data != None:
        for i in range(len(rcv_can_data)):
            can_data.append_can_buf(rcv_can_data[i]['id'],rcv_can_data[i]['length'], rcv_can_data[i]['data'])
    #mcp2515.spi_close()
    #print('spi closed')
    
    if checkbutton_var_trace.get():
        textbox.delete('0.0', END)
    else:
        import datetime
        textbox.insert('0.0', datetime.datetime.now())
    
    import tabulate
    textbox.insert('0.0', tabulate.tabulate(can_data.can_data_dict, headers='keys', tablefmt='grid'))
    
    if check_btn_var.get() is False: #if checkbtn pressed
        entry_can_filter.config(state=DISABLED)
        entry_can_mask.config(state=DISABLED)
    else:
        entry_can_filter.config(state=NORMAL)
        entry_can_mask.config(state=NORMAL)

    #if check_btn_var_light_up.get() is True:#light up button:

    root.after(60, period)

root.after(300, period)
root.mainloop()