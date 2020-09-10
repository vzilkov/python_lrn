from tkinter import *
import class_can_data
can_data = class_can_data.can_data()

root = Tk()

#root.resizable(FALSE, FALSE)

#label frames:
frame_rx = LabelFrame(root, text="CAN RX", font=('Courier New', 8))

frame_mask = LabelFrame(root, text="Mask", font=('Courier New',8))
frame_filter = LabelFrame(root, text="Filter", font=('Courier New',8))

frame_tx = LabelFrame(root, text="CAN TX", font=('Courier New', 8))

frame_tx_btn = LabelFrame(root, font=('Courier New', 8))

#buttons
check_btn_var = BooleanVar(value=FALSE)
check_btn_var_prev = check_btn_var.get()

check_btn_var_light_up = BooleanVar(value=FALSE)
checkbutton_var_trace = BooleanVar(value=TRUE)
checkbutton_var_ext_id = BooleanVar(value=FALSE)
check_listen_all_var = BooleanVar(value=FALSE)

checkbutton_filters_masks = Checkbutton(frame_rx, 
                                        text='Check can filter & mask', 
                                        var=check_btn_var, font=('Courier New', 8))

checkbutton_light_up = Checkbutton(frame_rx, text='Light up changed data', var= check_btn_var_light_up, font=('Courier New', 8))

checkbutton_trace = Checkbutton(frame_rx, text='Fixed/Rolling trace', var= checkbutton_var_trace, font=('Courier New', 8))

check_ext_id_btn = Checkbutton(root, text='Extended ID', var= checkbutton_var_ext_id, font=('Courier New', 8))#TODO

check_listen_all_btn = Checkbutton(root, text='Listen all mode', var= check_listen_all_var, font=('Courier New', 8))#TODO

#checkbuttons for mask and filter:

#filter:
check_filter_list = [BooleanVar(value=FALSE) for i in range(29)]

check_flt0 = Checkbutton(frame_filter, text='0', var= check_filter_list[0], font=('Courier New', 8))
check_flt1 = Checkbutton(frame_filter, text='1', var= check_filter_list[1], font=('Courier New', 8))
check_flt2 = Checkbutton(frame_filter, text='2', var= check_filter_list[2], font=('Courier New', 8))
check_flt3 = Checkbutton(frame_filter, text='3', var= check_filter_list[3], font=('Courier New', 8))
check_flt4 = Checkbutton(frame_filter, text='4', var= check_filter_list[4], font=('Courier New', 8))
check_flt5 = Checkbutton(frame_filter, text='5', var= check_filter_list[5], font=('Courier New', 8))
check_flt6 = Checkbutton(frame_filter, text='6', var= check_filter_list[6], font=('Courier New', 8))
check_flt7 = Checkbutton(frame_filter, text='7', var= check_filter_list[7], font=('Courier New', 8))
check_flt8 = Checkbutton(frame_filter, text='8', var= check_filter_list[8], font=('Courier New', 8))
check_flt9 = Checkbutton(frame_filter, text='9', var= check_filter_list[9], font=('Courier New', 8))
check_flt10 = Checkbutton(frame_filter, text='10', var= check_filter_list[10], font=('Courier New', 8))
'''check_flt11_var = BooleanVar(value=FALSE)
check_flt11 = Checkbutton(frame_rx, text='11 bit', var= check_flt11_var)
check_flt0_var = BooleanVar(value=FALSE)
check_flt0 = Checkbutton(frame_rx, text='0 bit', var= check_flt0_var)
check_flt0_var = BooleanVar(value=FALSE)
check_flt0 = Checkbutton(frame_rx, text='0 bit', var= check_flt0_var)
check_flt0_var = BooleanVar(value=FALSE)
check_flt0 = Checkbutton(frame_rx, text='0 bit', var= check_flt0_var)
check_flt0_var = BooleanVar(value=FALSE)
check_flt0 = Checkbutton(frame_rx, text='0 bit', var= check_flt0_var)
check_flt0_var = BooleanVar(value=FALSE)
check_flt0 = Checkbutton(frame_rx, text='0 bit', var= check_flt0_var)
check_flt0_var = BooleanVar(value=FALSE)
check_flt0 = Checkbutton(frame_rx, text='0 bit', var= check_flt0_var)
check_flt0_var = BooleanVar(value=FALSE)
check_flt0 = Checkbutton(frame_rx, text='0 bit', var= check_flt0_var)
check_flt0_var = BooleanVar(value=FALSE)
check_flt0 = Checkbutton(frame_rx, text='0 bit', var= check_flt0_var)
check_flt0_var = BooleanVar(value=FALSE)
check_flt0 = Checkbutton(frame_rx, text='0 bit', var= check_flt0_var)
check_flt0_var = BooleanVar(value=FALSE)
check_flt0 = Checkbutton(frame_rx, text='0 bit', var= check_flt0_var)
check_flt0_var = BooleanVar(value=FALSE)
check_flt0 = Checkbutton(frame_rx, text='0 bit', var= check_flt0_var)
check_flt0_var = BooleanVar(value=FALSE)
check_flt0 = Checkbutton(frame_rx, text='0 bit', var= check_flt0_var)
check_flt0_var = BooleanVar(value=FALSE)
check_flt0 = Checkbutton(frame_rx, text='0 bit', var= check_flt0_var)
check_flt0_var = BooleanVar(value=FALSE)
check_flt0 = Checkbutton(frame_rx, text='0 bit', var= check_flt0_var)
check_flt0_var = BooleanVar(value=FALSE)
check_flt0 = Checkbutton(frame_rx, text='0 bit', var= check_flt0_var)#29 bits'''
#mask:
check_mask_list = [BooleanVar(value=FALSE) for i in range(29)]

check_mask0 = Checkbutton(frame_mask, text='0', var= check_mask_list[0], font=('Courier New', 8))
check_mask1 = Checkbutton(frame_mask, text='1', var= check_mask_list[1], font=('Courier New', 8))
check_mask2 = Checkbutton(frame_mask, text='2', var= check_mask_list[2], font=('Courier New', 8))
check_mask3 = Checkbutton(frame_mask, text='3', var= check_mask_list[3], font=('Courier New', 8))
check_mask4 = Checkbutton(frame_mask, text='4', var= check_mask_list[4], font=('Courier New', 8))
check_mask5 = Checkbutton(frame_mask, text='5', var= check_mask_list[5], font=('Courier New', 8))
check_mask6 = Checkbutton(frame_mask, text='6', var= check_mask_list[6], font=('Courier New', 8))
check_mask7 = Checkbutton(frame_mask, text='7', var= check_mask_list[7], font=('Courier New', 8))
check_mask8 = Checkbutton(frame_mask, text='8', var= check_mask_list[8], font=('Courier New', 8))
check_mask9 = Checkbutton(frame_mask, text='9', var= check_mask_list[9], font=('Courier New', 8))
check_mask10 = Checkbutton(frame_mask, text='10', var= check_mask_list[10], font=('Courier New', 8))

def lock_mask_and_filter():
    check_mask0.config(state=DISABLED)
    check_mask1.config(state=DISABLED)
    check_mask2.config(state=DISABLED)
    check_mask3.config(state=DISABLED)
    check_mask4.config(state=DISABLED)
    check_mask5.config(state=DISABLED)
    check_mask6.config(state=DISABLED)
    check_mask7.config(state=DISABLED)
    check_mask8.config(state=DISABLED)
    check_mask9.config(state=DISABLED)
    check_mask10.config(state=DISABLED)
    
    check_flt0.config(state=DISABLED)
    check_flt1.config(state=DISABLED)
    check_flt2.config(state=DISABLED)
    check_flt3.config(state=DISABLED)
    check_flt4.config(state=DISABLED)
    check_flt5.config(state=DISABLED)
    check_flt6.config(state=DISABLED)
    check_flt7.config(state=DISABLED)
    check_flt8.config(state=DISABLED)
    check_flt9.config(state=DISABLED)
    check_flt10.config(state=DISABLED)
    
def unlock_mask_and_filter():
    check_mask0.config(state=NORMAL)
    check_mask1.config(state=NORMAL)
    check_mask2.config(state=NORMAL)
    check_mask3.config(state=NORMAL)
    check_mask4.config(state=NORMAL)
    check_mask5.config(state=NORMAL)
    check_mask6.config(state=NORMAL)
    check_mask7.config(state=NORMAL)
    check_mask8.config(state=NORMAL)
    check_mask9.config(state=NORMAL)
    check_mask10.config(state=NORMAL)
    
    check_flt0.config(state=NORMAL)
    check_flt1.config(state=NORMAL)
    check_flt2.config(state=NORMAL)
    check_flt3.config(state=NORMAL)
    check_flt4.config(state=NORMAL)
    check_flt5.config(state=NORMAL)
    check_flt6.config(state=NORMAL)
    check_flt7.config(state=NORMAL)
    check_flt8.config(state=NORMAL)
    check_flt9.config(state=NORMAL)
    check_flt10.config(state=NORMAL)
    
#Label
label_can_filter = Label(frame_rx, text='Filter:', font=('Courier New', 8))

label_can_mask = Label(frame_rx, text='Mask:', font=('Courier New', 8))

#entry
entry_can_filter_string = StringVar(root, '0')

entry_can_filter = Entry(frame_rx, text='enter vals in hex 0-7FF', textvariable = entry_can_filter_string, state=DISABLED, font=('Courier New', 8))#0x3FFFFFF - 29bit CAN2.0B
entry_can_filter_string_prev = entry_can_filter_string.get()

entry_can_mask_string = StringVar(root, '0')
entry_can_mask = Entry(frame_rx, text='enter values in hex 0-7FF', textvariable = entry_can_mask_string, state=DISABLED)
entry_can_mask_string_prev = entry_can_mask_string.get()

#clear button
def clear_data():
    can_data.clear()
    
clear_btn = Button(frame_rx, text='Reset RX data', command=clear_data, font=('Courier New', 8))

label_id = Label(frame_tx, text='ID (hex):', height=4, font=('Courier New', 8))
label_len = Label(frame_tx, text='length:', height=4, font=('Courier New', 8))
#label_data = Label(frame_tx, text='data:', height=4, font=('Courier New', 8))
txt_id = Entry(frame_tx, width=7, font=('Courier New', 8))
txt_id.insert(0, '0')

from tkinter import ttk
txt_len_var = 0
combobox_length = ttk.Combobox(frame_tx, values=[0,1,2,3,4,5,6,7,8], textvariable=txt_len_var, width=2, font=('Courier New', 8))
combobox_length.set(8)
txt_len = Entry(frame_tx, width=3, justify=CENTER)

label_data0 = Label(frame_tx, text='data0', font=('Courier New', 8))
label_data1 = Label(frame_tx, text='data1', font=('Courier New', 8))
label_data2 = Label(frame_tx, text='data2', font=('Courier New', 8))
label_data3 = Label(frame_tx, text='data3', font=('Courier New', 8))
label_data4 = Label(frame_tx, text='data4', font=('Courier New', 8))
label_data5 = Label(frame_tx, text='data5', font=('Courier New', 8))
label_data6 = Label(frame_tx, text='data6', font=('Courier New', 8))
label_data7 = Label(frame_tx, text='data7', font=('Courier New', 8))

vals = [hex(i) for i in range(0xFF+1)]

txt_data0 = ttk.Combobox(frame_tx, values=vals, width=5, font=('Courier New', 8))
txt_data1 = ttk.Combobox(frame_tx, values=vals, width=5, font=('Courier New', 8))
txt_data2 = ttk.Combobox(frame_tx, values=vals, width=5, font=('Courier New', 8))
txt_data3 = ttk.Combobox(frame_tx, values=vals, width=5, font=('Courier New', 8))
txt_data4 = ttk.Combobox(frame_tx, values=vals, width=5, font=('Courier New', 8))
txt_data5 = ttk.Combobox(frame_tx, values=vals, width=5, font=('Courier New', 8))
txt_data6 = ttk.Combobox(frame_tx, values=vals, width=5, font=('Courier New', 8))
txt_data7 = ttk.Combobox(frame_tx, values=vals, width=5, font=('Courier New', 8))

txt_data0.insert(0, '0x0')
txt_data1.insert(0, '0x1')
txt_data2.insert(0, '0x2')
txt_data3.insert(0, '0x3')
txt_data4.insert(0, '0x4')
txt_data5.insert(0, '0x5')
txt_data6.insert(0, '0x6')
txt_data7.insert(0, '0x7')

baudrate_val = ttk.Combobox(root, values=[10,20,50,80,100,125,250,500,1000], width=4, font=('Courier New', 8))
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
    
button_tx_can_msg = Button(frame_tx_btn, text='Transmit\nCAN data', 
                           height=2, font=('Courier New', 8),
                           width=9,
                           command=send_data)
def set_tx_sett_destroy():
 destroy()

def set_tx_settings():
 window = Toplevel(root)
 window.wm_attributes("-topmost",1)
 window.title('CAN tx settings')
 window.geometry("200x200")
 Label(window, text='can settings label').pack()
 window.lift(aboveThis=root)

 btn_close = Button(window, command=set_tx_sett_destroy, text='close window')
 btn_close.pack()
 #window.destroy()

button_tx_settings = Button(frame_tx_btn, text='Tx setttings', 
				height=2, 
				font=('Courier New',8), 
				width=9, command=set_tx_settings)


#place root window to right
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
positionRight = int(root.winfo_screenwidth() - windowWidth)
positionDown = int(root.winfo_screenheight() - windowHeight)

#textbox & scrollbar:
ybar = Scrollbar(root, width=30)
textbox = Text(root, width=50, height=root.winfo_screenheight(), font=('Courier New', 8))
ybar.config(command=textbox.yview)
textbox.config(yscrollcommand=ybar.set)

#packs:
textbox.pack(side=LEFT)
ybar.pack(side=LEFT, fill=BOTH)

frame_rx.pack(side=TOP)
frame_mask.pack(side=TOP)
frame_filter.pack(side=TOP)
frame_tx_btn.pack(side=TOP)
'''checkbutton_light_up.pack(side=TOP) checkbutton_trace.pack(side=TOP) checkbutton_filters_masks.pack(side=TOP) 
label_can_filter.pack(side=TOP) entry_can_filter.pack(side=TOP) label_can_mask.pack(side=TOP) 
entry_can_mask.pack(side=TOP) clear_btn.pack(side=TOP)''' 
checkbutton_light_up.grid(column=0, row=0) 
checkbutton_trace.grid(column=0, row=1) 
checkbutton_filters_masks.grid(column=0, row=2) 
label_can_filter.grid(column=0, row=3)
#entry_can_filter.pack(side=TOP)
#label_can_mask.pack(side=TOP)
#entry_can_mask.pack(side=TOP)
clear_btn.grid(column=0, row=3)

check_flt0.grid(column=5, row=7)
check_flt1.grid(column=4, row=7)
check_flt2.grid(column=3, row=7)
check_flt3.grid(column=2, row=7)
check_flt4.grid(column=1, row=7)
check_flt5.grid(column=6, row=6)
check_flt6.grid(column=5, row=6)
check_flt7.grid(column=4, row=6)
check_flt8.grid(column=3, row=6)
check_flt9.grid(column=2, row=6)
check_flt10.grid(column=1, row=6)

check_mask0.grid(column=5, row=5)
check_mask1.grid(column=4, row=5)
check_mask2.grid(column=3, row=5)
check_mask3.grid(column=2, row=5)
check_mask4.grid(column=1, row=5)
check_mask5.grid(column=6, row=4)
check_mask6.grid(column=5, row=4)
check_mask7.grid(column=4, row=4)
check_mask8.grid(column=3, row=4)
check_mask9.grid(column=2, row=4)
check_mask10.grid(column=1, row=4)

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

button_tx_can_msg.grid(column=1, row=0)
button_tx_settings.grid(column=0,row=0)
baudrate_val.pack(side=TOP)

check_ext_id_btn.pack(side=TOP)

check_listen_all_btn.pack(side=TOP)

#root.attributes('-fullscreen', True)

print('starting CAN configuration:')

from class_spi_to_can import *
mcp2515 = spi_to_can_brd_exchange(5000)
mcp2515.set_config_mode()
mcp2515.set_baudrate(500)
mcp2515.set_normal_mode()

def change_filter(filter_val):
    global mcp2515
    mcp2515.set_config_mode()
    mcp2515.set_filter(filter_val)
    mcp2515.set_normal_mode()
    
def change_mask(mask_val):
    global mcp2515
    mcp2515.set_config_mode()
    mcp2515.set_mask(mask_val)
    mcp2515.set_normal_mode()

def change_filter_and_mask(filter_val, mask_val):
    global mcp2515
    mcp2515.set_config_mode()
    mcp2515.set_filter(filter_val)
    mcp2515.set_mask(mask_val)
    mcp2515.set_normal_mode()

filter_value_prev = 0
mask_value_prev = 0
check_mode_var_prev = 0xFF

def period():
    global filter_value_prev, mask_value_prev, check_listen_all_var, check_mode_var_prev
    global mcp2515, check_mask_list, check_filter_list
    global check_btn_var_prev, check_btn_var
    
    rcv_can_data = mcp2515.can_rx_func()
    if rcv_can_data != None:
        for i in range(len(rcv_can_data)):
            can_data.append_can_buf(hex(rcv_can_data[i]['id']), rcv_can_data[i]['length'], (rcv_can_data[i]['data']))
    
    if checkbutton_var_trace.get():
        textbox.delete('0.0', END)
    else:
        import datetime
        textbox.insert('0.0', datetime.datetime.now())
    
    import tabulate
    textbox.insert('0.0', tabulate.tabulate(can_data.can_data_dict, headers='keys', tablefmt='grid'))
    
    Listen_only_mode = 0x60
    Normal_mode = 0
    
    check_mode_var = mcp2515.check_current_operation_mode()
    if check_mode_var != Normal_mode and (check_listen_all_var.get() == False):
        print('Normal Mode entered')
        if check_mode_var_prev != check_mode_var:
            mcp2515.set_config_mode()
            mcp2515.set_normal_mode()
            check_mode_var_prev = check_mode_var
    elif (check_mode_var != Listen_only_mode) and (check_listen_all_var.get() == True):
        print('Listen all Mode entered')
        if check_mode_var_prev != check_mode_var:
            mcp2515.set_config_mode()
            mcp2515.set_listen_only_mode()
            check_mode_var_prev = check_mode_var
    
    if check_mode_var == Normal_mode and check_btn_var.get() == True:
        check_btn_var_prev = check_btn_var.get()
        entry_can_filter.config(state=NORMAL)
        entry_can_mask.config(state=NORMAL)
        unlock_mask_and_filter()
        count = 0
        mask_buf = 0
        filter_buf = 0
       
        for i in check_mask_list:
            mask_buf |= (int(bool(i.get()))<<count)
            count +=1
     
        count = 0
        for i in check_filter_list:
            filter_buf |= (int(bool(i.get()))<<count)
            count +=1
        
        if filter_value_prev != filter_buf or mask_value_prev != mask_buf:
            filter_value_prev = filter_buf
            mask_value_prev = mask_buf
            change_filter_and_mask(filter_buf, mask_buf)
    else:
        entry_can_filter.config(state=DISABLED)
        entry_can_mask.config(state=DISABLED)
        lock_mask_and_filter()
        if check_btn_var_prev != check_btn_var.get():
            check_btn_var_prev = check_btn_var.get()
            change_filter_and_mask(0,0)
            filter_value_prev = 0
            mask_value_prev = 0
    
    global baudrate_val_prev
    baudrate_current = int(baudrate_val.get())
    if baudrate_val_prev != baudrate_current:
        print('Baudrate = %d'%baudrate_current)
        baudrate_val_prev = baudrate_current
    
    #if check_btn_var_light_up.get() is True:#light up button:

    #333933 - pc, 329037 - rasp, counts send-rcv data, rcv percentage is 98.5%
    #121192 - pc, 120318 - rasp, counts send-rcv data, rcv percentage is 99.3%

    root.after(20, period)

root.after(150, period)
root.mainloop()
