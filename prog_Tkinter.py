from tkinter import *

class mainwindow():
    def __init__(self):
        self.root = Tk()
        width = 900
        height = 480
        self.root.geometry("%dx%d"%(width, height))
        #self.root.resizable(FALSE, FALSE)

root = mainwindow().root

#label frames:
frame_rx = LabelFrame(root, text="CAN RX")

frame_mask = LabelFrame(root, text="Mask")
frame_filter = LabelFrame(root, text="Filter")

frame_tx = LabelFrame(root, text="CAN TX")

frame_tx_btn = LabelFrame(root, text='Tx frame')

#buttons
check_btn_var = BooleanVar(value=FALSE)
check_btn_var_prev = check_btn_var.get()

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

#checkbuttons for mask and filter:

#filter:
check_filter_list = [BooleanVar(value=FALSE) for i in range(30)]
check_filter_list_new = []
for i in range(30):
    check_filter_list_new.append(Checkbutton(frame_filter, text='%d'%i, var= check_filter_list[i]))
'''check_flt0 = Checkbutton(frame_filter, text='0', var= check_filter_list[0])
check_flt1 = Checkbutton(frame_filter, text='1', var= check_filter_list[1])
check_flt2 = Checkbutton(frame_filter, text='2', var= check_filter_list[2])
check_flt3 = Checkbutton(frame_filter, text='3', var= check_filter_list[3])
check_flt4 = Checkbutton(frame_filter, text='4', var= check_filter_list[4])
check_flt5 = Checkbutton(frame_filter, text='5', var= check_filter_list[5])
check_flt6 = Checkbutton(frame_filter, text='6', var= check_filter_list[6])
check_flt7 = Checkbutton(frame_filter, text='7', var= check_filter_list[7])
check_flt8 = Checkbutton(frame_filter, text='8', var= check_filter_list[8])
check_flt9 = Checkbutton(frame_filter, text='9', var= check_filter_list[9])
check_flt10 = Checkbutton(frame_filter, text='10', var= check_filter_list[10])'''
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

check_mask0 = Checkbutton(frame_mask, text='0', var= check_mask_list[0])
check_mask1 = Checkbutton(frame_mask, text='1', var= check_mask_list[1])
check_mask2 = Checkbutton(frame_mask, text='2', var= check_mask_list[2])
check_mask3 = Checkbutton(frame_mask, text='3', var= check_mask_list[3])
check_mask4 = Checkbutton(frame_mask, text='4', var= check_mask_list[4])
check_mask5 = Checkbutton(frame_mask, text='5', var= check_mask_list[5])
check_mask6 = Checkbutton(frame_mask, text='6', var= check_mask_list[6])
check_mask7 = Checkbutton(frame_mask, text='7', var= check_mask_list[7])
check_mask8 = Checkbutton(frame_mask, text='8', var= check_mask_list[8])
check_mask9 = Checkbutton(frame_mask, text='9', var= check_mask_list[9])
check_mask10 = Checkbutton(frame_mask, text='10', var= check_mask_list[10])

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
label_can_filter = Label(frame_rx, text='Filter:')

label_can_mask = Label(frame_rx, text='Mask:')

#entry
entry_can_filter_string = StringVar(root, '0')

entry_can_filter = Entry(frame_rx, text='enter vals in hex 0-7FF', textvariable = entry_can_filter_string, state=DISABLED)#0x3FFFFFF - 29bit CAN2.0B
entry_can_filter_string_prev = entry_can_filter_string.get()

entry_can_mask_string = StringVar(root, '0')
entry_can_mask = Entry(frame_rx, text='enter values in hex 0-7FF', textvariable = entry_can_mask_string, state=DISABLED)
entry_can_mask_string_prev = entry_can_mask_string.get()

#clear button
def clear_data():
    print("Clear data")
    
clear_btn = Button(frame_rx, text='Reset RX data', command=clear_data)

label_id = Label(frame_tx, text='ID (hex):', height=4)
label_len = Label(frame_tx, text='length:', height=4)
#label_data = Label(frame_tx, text='data:', height=4)
txt_id = Entry(frame_tx, width=7)
txt_id.insert(0, '0')

from tkinter import ttk
txt_len_var = 0
combobox_length = ttk.Combobox(frame_tx, values=[0,1,2,3,4,5,6,7,8], textvariable=txt_len_var, width=2)
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

txt_data0 = ttk.Combobox(frame_tx, values=vals, width=5)
txt_data1 = ttk.Combobox(frame_tx, values=vals, width=5)
txt_data2 = ttk.Combobox(frame_tx, values=vals, width=5)
txt_data3 = ttk.Combobox(frame_tx, values=vals, width=5)
txt_data4 = ttk.Combobox(frame_tx, values=vals, width=5)
txt_data5 = ttk.Combobox(frame_tx, values=vals, width=5)
txt_data6 = ttk.Combobox(frame_tx, values=vals, width=5)
txt_data7 = ttk.Combobox(frame_tx, values=vals, width=5)

txt_data0.insert(0, '0x0')
txt_data1.insert(0, '0x1')
txt_data2.insert(0, '0x2')
txt_data3.insert(0, '0x3')
txt_data4.insert(0, '0x4')
txt_data5.insert(0, '0x5')
txt_data6.insert(0, '0x6')
txt_data7.insert(0, '0x7')

baudrate_val = ttk.Combobox(root, values=[10,20,50,80,100,125,250,500,1000], width=4)
baudrate_val.insert(0,'500')
baudrate_val_prev = int(baudrate_val.get(),16)

def set_tx_settings():
 window = Toplevel(root)
 window.wm_attributes("-topmost",1)
 window.title('CAN tx settings')
 window.geometry("200x200")
 Label(window, text='can settings label').pack()
 window.lift(aboveThis=root)

button_tx = Button(frame_tx_btn, text='Tx msg', 
                            height=2, 
                             
                            width=9, command=set_tx_settings)


#place root window to right
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
positionRight = int(root.winfo_screenwidth() - windowWidth)
positionDown = int(root.winfo_screenheight() - windowHeight)

#textbox & scrollbar:
ybar = Scrollbar(root, width=30)
textbox = Text(root, width=80, height=root.winfo_screenheight())
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

'''check_flt0.grid(column=5, row=7)
check_flt1.grid(column=4, row=7)
check_flt2.grid(column=3, row=7)
check_flt3.grid(column=2, row=7)
check_flt4.grid(column=1, row=7)
check_flt5.grid(column=6, row=6)
check_flt6.grid(column=5, row=6)
check_flt7.grid(column=4, row=6)
check_flt8.grid(column=3, row=6)
check_flt9.grid(column=2, row=6)
check_flt10.grid(column=1, row=6)'''

for i in range(30):
    if i < 11:
        check_filter_list_new[i].grid(column=11-i, row=7)
    else:
        check_filter_list_new[i].grid(column=29-i, row=6)

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

button_tx.grid(column=0,row=0)
baudrate_val.pack(side=TOP)

check_ext_id_btn.pack(side=TOP)

check_listen_all_btn.pack(side=TOP)

#root.attributes('-fullscreen', True)

def period():
    global filter_value_prev, mask_value_prev, check_listen_all_var, check_mode_var_prev
    global check_mask_list, check_filter_list
    global check_btn_var_prev, check_btn_var
    
    rcv_can_data = None#mcp2515.can_rx_func()
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
    
    if check_mode_var != Normal_mode and (check_listen_all_var.get() == False):
        print('Normal Mode entered')
        
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
