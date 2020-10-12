from tkinter import *

class mainwindow():
    def __init__(self):
        self.root = Tk()
        width = 1300
        height = 700
        self.root.geometry("%dx%d"%(width, height))
        #self.root.resizable(FALSE, FALSE)

root = mainwindow().root
root.minsize(1080, 550)
#label frames:
frame_rx = LabelFrame(root, text="CAN RX")

frame_mask = LabelFrame(root, text="Mask (hex vals 0-%X)"%0x7FF)
frame_filter = LabelFrame(root, text="Filter (hex vals 0-7FF)")

frame_tx = LabelFrame(root, text="CAN TX")

frame_tx_btn = LabelFrame(root, text='Tx frame')

#buttons
check_btn_var_filter_and_mask = BooleanVar(value=FALSE)
check_btn_var_prev = check_btn_var_filter_and_mask.get()

check_btn_var_light_up = BooleanVar(value=FALSE)
checkbutton_var_trace = BooleanVar(value=TRUE)
checkbutton_var_ext_id = BooleanVar(value=FALSE)
check_listen_all_var = BooleanVar(value=FALSE)

checkbutton_filters_masks = Checkbutton(frame_rx, 
                                        text='Check can filter & mask', 
                                        var=check_btn_var_filter_and_mask)

checkbutton_light_up = Checkbutton(frame_rx, text='Light up changed data', var= check_btn_var_light_up)

checkbutton_trace = Checkbutton(frame_rx, text='Fixed/Rolling trace', var= checkbutton_var_trace)

check_ext_id_btn = Checkbutton(root, text='Extended ID', var= checkbutton_var_ext_id)#TODO

check_listen_all_btn = Checkbutton(root, text='Listen all mode', var= check_listen_all_var)#TODO

#checkbuttons for mask and filter:

#Label
label_can_filter = Label(frame_rx, text='Filter:')

label_can_mask = Label(frame_rx, text='Mask:')

#entry
entry_can_filter_string = StringVar(root, '0')

entry_can_filter = Entry(frame_filter, text='enter vals in hex 0-7FF', textvariable = entry_can_filter_string, state=DISABLED)#0x3FFFFFF - 29bit CAN2.0B
entry_can_filter_string_prev = entry_can_filter_string.get()
entry_can_filter.grid(row=1, column=0)

entry_can_mask_string = StringVar(root, '0')
entry_can_mask = Entry(frame_mask, text='enter values in hex 0-7FF', textvariable = entry_can_mask_string, state=DISABLED)
entry_can_mask_string_prev = entry_can_mask_string.get()
entry_can_mask.grid(row=1, column=0)

clear_btn = Button(frame_rx, text='Reset RX data')#, command=clear_data)

label_id = Label(frame_tx, text='ID (hex):')
label_len = Label(frame_tx, text='Length:')

txt_id = Entry(frame_tx, width=9)
#txt_id.insert(0, '0')

#CAN TX frame
listbox_length = Listbox(frame_tx, width=3, height = 9, selectmode=SINGLE)
for i in range(8+1):
    listbox_length.insert(i, '%d' % i)

label_data = []
txt_data = []

label_id.grid(column=0, row=0)
txt_id.grid(column=0, row=1)

label_len.grid(column=0, row=2)
listbox_length.grid(column=0, row=3)

for i in range(8):
    label_data.append(Label(frame_tx, text = 'Data%d'%i))
    txt_data.append(Entry(frame_tx, width=4))
    label_data[i].grid(column=i+2, row=0)
    txt_data[i].grid(column=i+2,   row=1)

from tkinter import ttk
baudrate_val = ttk.Combobox(root, values=[10,20,50,80,100,125,250,500,1000], width = 4)
baudrate_val.insert(0,'500')
baudrate_val_prev = int(baudrate_val.get(), 16)

def set_tx_settings():
    try:
        CAN_ID = int(txt_id.get(),16)
        listbox_length_val = listbox_length.curselection()
        CAN_LEN = listbox_length_val[0]
        CAN_data = []
        for i in range(CAN_LEN):
            CAN_data.append(int(txt_data[i].get(),16))
        
        #send prepared data here, TODO
        print('CAN TX btn pressed ID %d, Len = %d, Data = '%(CAN_ID, CAN_LEN), CAN_data)
    except:
        import tkinter.messagebox
        print('Unknown data entered in TX send msg')
        tkinter.messagebox.showwarning('CAN TX data parameters', 'Check ID, Length or Data')
    
button_tx = Button(frame_tx_btn, text='Tx msg', 
                            height=2, 
                            width=8, command=set_tx_settings)

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
frame_tx.pack(side = TOP)
frame_tx_btn.pack(side=TOP)

checkbutton_light_up.grid(column=0, row=0) 
checkbutton_trace.grid(column=0, row=1) 
checkbutton_filters_masks.grid(column=0, row=2) 
label_can_filter.grid(column=0, row=3)

clear_btn.grid(column=0, row=3)

button_tx.grid(column = 0, row = 0)
baudrate_val.pack(side=TOP)
check_ext_id_btn.pack(side=TOP)
check_listen_all_btn.pack(side=TOP)

#root.attributes('-fullscreen', True)

import class_can_data
can_data = class_can_data.can_data()

#clear button
def clear_data():
    can_data.clear()
    print('Data cleared')

clear_btn.config(command=clear_data)

def period():
    global filter_value_prev, mask_value_prev
    global check_listen_all_var, check_mode_var_prev
    global check_mask_list, check_filter_list
    global check_btn_var_prev, check_btn_var_filter_and_mask
    global checkbutton_var_ext_id, can_data

    rcv_can_data = can_data.read_data()
    #print('Rcv can data = ', rcv_can_data)
    if rcv_can_data != None:
        #for i in range(len(rcv_can_data)):
        can_data.append_can_buf(hex(rcv_can_data['id']), rcv_can_data['length'], (rcv_can_data['data']))
    
    if checkbutton_var_trace.get():
        textbox.delete('0.0', END)
    else:
        import datetime
        textbox.insert('0.0', datetime.datetime.now())
    
    import tabulate
    textbox.insert('0.0', tabulate.tabulate(can_data.can_data_dict, headers='keys', tablefmt='grid'))
    
    #check_btn_var_filter_and_mask start
    if check_btn_var_filter_and_mask.get():
        entry_can_filter.config(state=NORMAL)
        entry_can_mask.config(state=NORMAL)

        if checkbutton_var_ext_id.get():
            frame_mask.config(text="Mask (hex vals 0-%X)"%0x1FFFFFFF)
            frame_filter.config(text="Filter (hex vals 0-%X)"%0x1FFFFFFF)
        else:
            frame_mask.config(text="Mask (hex vals 0-%X)"%0x7FF)
            frame_filter.config(text="Filter (hex vals 0-%X)"%0x7FF)
        a = entry_can_filter.get()
    
    else:
        a = entry_can_filter.get()
        entry_can_filter.config(state=DISABLED)
        entry_can_mask.config(state=DISABLED)
    #check_btn_var_filter_and_mask END

#Listbox start
    #listbox_length_val = listbox_length.curselection()
    #if listbox_length_val:
        #print('Listbox value = ', listbox_length_val[0])
#Listbox END
    #if check_btn_var_light_up.get() is True: #light up button:

    #333933 - pc, 329037 - rasp, counts send-rcv data, rcv percentage is 98.5%
    #121192 - pc, 120318 - rasp, counts send-rcv data, rcv percentage is 99.3%

    root.after(150, period)

root.after(250, period)
root.mainloop()
