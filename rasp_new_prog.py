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
checkbutton_var_ext_id = BooleanVar(value=FALSE)
check_listen_all_var = BooleanVar(value=FALSE)

checkbutton_filters_masks = Checkbutton(frame_rx, 
                                        text='Check can filter & mask', 
                                        var=check_btn_var)

checkbutton_light_up = Checkbutton(frame_rx, text='Light up changed data', var= check_btn_var_light_up)

checkbutton_trace = Checkbutton(frame_rx, text='Fixed/Rolling trace', var= checkbutton_var_trace)

check_ext_id_btn = Checkbutton(root, text='Extended ID', var= checkbutton_var_ext_id)#TODO

check_listen_all_btn = Checkbutton(root, text='Listen all mode', var= check_listen_all_var)#TODO

#Label
label_can_filter = Label(frame_rx, text='Filter:')

label_can_mask = Label(frame_rx, text='Mask:')

#entry
entry_can_filter_string = StringVar()
entry_can_filter_string_prev = entry_can_filter_string
entry_can_filter = Entry(frame_rx, text='enter vals in hex 0-7FF', textvariable = entry_can_filter_string)#0x3FFFFFF - 29bit CAN2.0B

entry_can_mask_string = StringVar()
entry_can_mask_string_prev = entry_can_mask_string
entry_can_mask = Entry(frame_rx, text='enter values in hex 0-7FF', textvariable = entry_can_mask_string)

#clear button
def clear_data():
    can_data.clear()
    
clear_btn = Button(frame_rx, text='Reset RX data', command=clear_data)

label_id = Label(frame_tx, text='ID (hex):', height=4, font=('Courier New', 14))
label_len = Label(frame_tx, text='length:', height=4, font=('Courier New', 14))
#label_data = Label(frame_tx, text='data:', height=4, font=('Courier New', 14))
txt_id = Entry(frame_tx, width=7)
txt_id.insert(0, '0')

from tkinter import ttk
txt_len_var = 0
combobox_length = ttk.Combobox(frame_tx, values=[0,1,2,3,4,5,6,7,8], textvariable=txt_len_var, width=2, font=('Courier New', 14))
combobox_length.set(8)
txt_len = Entry(frame_tx, width=3, justify=CENTER)

label_data0 = Label(frame_tx, text='data0')
label_data1 = Label(frame_tx, text='data1')
label_data2 = Label(frame_tx, text='data2')
label_data3 = Label(frame_tx, text='data3')
label_data4 = Label(frame_tx, text='data4')
label_data5 = Label(frame_tx, text='data5')
label_data6 = Label(frame_tx, text='data6')
label_data7 = Label(frame_tx, text='data7')

vals = [hex(i) for i in range(0xFF+1)]

txt_data0 = ttk.Combobox(frame_tx, values=vals, width=5, font=('Courier New', 16))
txt_data1 = ttk.Combobox(frame_tx, values=vals, width=5, font=('Courier New', 14))
txt_data2 = ttk.Combobox(frame_tx, values=vals, width=5, font=('Courier New', 14))
txt_data3 = ttk.Combobox(frame_tx, values=vals, width=5, font=('Courier New', 14))
txt_data4 = ttk.Combobox(frame_tx, values=vals, width=5, font=('Courier New', 14))
txt_data5 = ttk.Combobox(frame_tx, values=vals, width=5, font=('Courier New', 14))
txt_data6 = ttk.Combobox(frame_tx, values=vals, width=5, font=('Courier New', 14))
txt_data7 = ttk.Combobox(frame_tx, values=vals, width=5, font=('Courier New', 14))

txt_data0.insert(0, '0x0')
txt_data1.insert(0, '0x1')
txt_data2.insert(0, '0x2')
txt_data3.insert(0, '0x3')
txt_data4.insert(0, '0x4')
txt_data5.insert(0, '0x5')
txt_data6.insert(0, '0x6')
txt_data7.insert(0, '0x7')

baudrate_val = ttk.Combobox(root, values=[10,20,50,80,100,125,250,500,1000], width=4, font=('Courier New', 14))
baudrate_val.insert(0,'500')
baudrate_val_prev = int(baudrate_val.get(),16)

import class_spi_to_can
def send_data():
    ID='0x'+txt_id.get()
    ID=int(ID,16)
    print('ID = 0x%X'%ID)
    
    length = int(combobox_length.get())
    print('Length = %X'%length)
    data = []
    if length>0 and length<=8:
        i=1
        if i==1 and i<=length:
            buf = int(txt_data0.get(),16)
            data.append(buf)
            i+=1
        if i==2 and i<=length:
            buf = int(txt_data1.get(),16)
            data.append(buf)
            i+=1
        if i==3 and i<=length:
            buf = int(txt_data2.get(),16)
            data.append(buf)
            i+=1
        if i==4 and i<=length:
            buf = int(txt_data3.get(),16)
            data.append(buf)
            i+=1
        if i==5 and i<=length:
            buf = int(txt_data4.get(),16)
            data.append(buf)
            i+=1
        if i==6 and i<=length:
            buf = int(txt_data5.get(),16)
            data.append(buf)
            i+=1
        if i==7 and i<=length:
            buf = int(txt_data6.get(),16)
            data.append(buf)
            i+=1
        if i==8 and i<=length:
            buf = int(txt_data7.get(),16)
            data.append(buf) 
        print('data======',data)
        global can_data
        mcp2515.can_tx_func(ID,length,data)
    elif length == 0:
        mcp2515.can_tx_func(ID,length,data)
    
button_tx_can_msg = Button(frame_tx, text='Transmit\nCAN data', 
                           height=3, font=('Courier New', 10),
                           width=9,
                           command=send_data)

#place root window to right
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
positionRight = int(root.winfo_screenwidth() - windowWidth)
positionDown = int(root.winfo_screenheight() - windowHeight)

#textbox & scrollbar:
ybar = Scrollbar(root, width=30)
textbox = Text(root, width=60, height=root.winfo_screenheight(), font=('Courier New', 15))
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
clear_btn.pack(side=TOP)

frame_tx.pack(side=TOP)

label_id.grid(column=0, row=1)
txt_id.grid(column=1, row=1)
label_len.grid(column=2, row=1)
combobox_length.grid(column=3, row=1)

row_var = 2
column_var = 0

label_data0.grid(column=column_var,   row=row_var)
label_data1.grid(column=column_var+1, row=row_var)
label_data2.grid(column=column_var+2, row=row_var)
label_data3.grid(column=column_var+3, row=row_var)
label_data4.grid(column=column_var+4, row=row_var)
label_data5.grid(column=column_var+5, row=row_var)
label_data6.grid(column=column_var+6, row=row_var)
label_data7.grid(column=column_var+7, row=row_var)

txt_data0.grid(column=column_var,   row=row_var+1)
txt_data1.grid(column=column_var+1, row=row_var+1)
txt_data2.grid(column=column_var+2, row=row_var+1)
txt_data3.grid(column=column_var+3, row=row_var+1)
txt_data4.grid(column=column_var+4, row=row_var+1)
txt_data5.grid(column=column_var+5, row=row_var+1)
txt_data6.grid(column=column_var+6, row=row_var+1)
txt_data7.grid(column=column_var+7, row=row_var+1)

button_tx_can_msg.grid(column=column_var+8, row=4)

baudrate_val.pack(side=TOP)

check_ext_id_btn.pack(side=TOP)

check_listen_all_btn.pack(side=TOP)

#root.attributes('-fullscreen', True)

from class_spi_to_can import *
mcp2515 = spi_to_can_brd_exchange(5000)
mcp2515.set_config_mode(0,0)
mcp2515.set_normal_mode(500)

def period():
    global mcp2515
    
    #print('check_errors_rec_tec', mcp2515.check_errors_rec_tec())
    rcv_can_data = mcp2515.can_rx_func()
    if rcv_can_data != None:
        for i in range(len(rcv_can_data)):
            can_data.append_can_buf(hex(rcv_can_data[i]['id']), rcv_can_data[i]['length'], (rcv_can_data[i]['data']))
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
        mcp2515.set_mask(0)
        mcp2515.set_filter(0)
    else:
        entry_can_filter.config(state=NORMAL)
        entry_can_mask.config(state=NORMAL)
        mcp2515.set_mask(7)
        mcp2515.set_filter(7)
        
    global baudrate_val_prev
    baudrate_current = int(baudrate_val.get())
    if baudrate_val_prev != baudrate_current:
        print('Baudrate = %d'%baudrate_current)
        baudrate_val_prev = baudrate_current
        #mcp2515.set_normal_mode(baudrate_current)
    #if check_btn_var_light_up.get() is True:#light up button:

    '''global checkbutton_var_ext_id
    checkbutton_var_ext_id_cur = checkbutton_var_ext_id.get()
    if checkbutton_var_ext_id_cur != checkbutton_var_ext_id:
        print('Check button changed value')
        checkbutton_var_ext_id = checkbutton_var_ext_id_cur'''
    #333933 - pc, 329037 - rasp, counts send-rcv data, rcv percentage is 98.5%
    #121192 - pc, 120318 - rasp, counts send-rcv data, rcv percentage is 99.3%
    
    global entry_can_filter_string, entry_can_filter_string_prev, entry_can_mask_string, entry_can_mask_string_prev
    
    if entry_can_filter_string != entry_can_filter_string_prev:
        entry_can_filter_string_prev = entry_can_filter_string
        hex(entry_can_filter_string_prev)

    root.after(15, period)

root.after(150, period)
root.mainloop()