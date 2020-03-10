from tkinter import *

#test
import random
from colorama import init 
#from termcolor import colored 
from os import system, name 

import os

root = Tk()
root.geometry("1024x600")
root.resizable(FALSE, FALSE)
os.system('cls')
check_btn_var = BooleanVar(value=FALSE)
check_btn_var_light_up = BooleanVar(value=FALSE)

#textbox = Text(root, heigh=30, width=80)
#textbox.tag_config('changed', background ='GREY', foreground='white')
#textbox.config(state='disabled')
#scroll_text = Scrollbar(orient=VERTICAL, command=textbox.yview)
#textbox.configure(yscrollcommand=scroll_text.set)
#scroll_text.pack(side="right", fill="y")

#fontstyle = ('sans-serif', 11)
#label_can_data_text = Label(root, text='  ID      Length      Data1      Data2      Data3       Data4      Data5      Data6       Data7       Data8', font=fontstyle)
#label_can_data_text.config(font=fontstyle)

#buttons
checkbutton_filters_masks = Checkbutton(root, 
                                        text='Check can filter & mask', 
                                        var=check_btn_var)

checkbutton_light_up = Checkbutton(root, text='Light up changed data', var=check_btn_var_light_up)

checkbutton_trace = Checkbutton(root, text='Fixed/Rolling trace')

#Label
label_can_filter = Label(root, text='Filter:')

label_can_mask = Label(root, text='Mask:')

#entry
entry_can_filter = Entry(root, text='enter vals in hex 0-7FF')
entry_can_mask = Entry(root, text='enter values in hex 0-7FF')

#places
x_column_periph = 650

checkbutton_filters_masks.place(x=x_column_periph, y=10)

label_can_mask.place(x=x_column_periph, y=50)
entry_can_mask.place(x=x_column_periph+40, y=50)

entry_can_filter.place(x=x_column_periph+40, y=80)
label_can_filter.place(x=x_column_periph, y=80)

checkbutton_light_up.place(x=x_column_periph, y=110)
checkbutton_trace.place(x=x_column_periph, y=130)

count = 0
list_can_data_prev = [0,1,2,3,4,5,6,7,8,9]
dict_can_data = dict(id=0, lenght=0, data={0:10,1:11,2:12,3:13,4:14,5:15,6:16,7:17})

print_can_data = [{'id':11, 'lenght':8, 'data':{0:1,1:2, 2:3, 3:4, 4:5, 5:6, 6:7,7:8}}]

def printing():
    global count
    global check_btn_var, check_btn_var_light_up
    global list_can_data_prev
    #start test
<<<<<<< HEAD
    os.system('cls')
    print(print_can_data, sep='\n')
    add_data = {'id':2, 'lenght':7, 'data':{0:11,1:12, 2:13, 3:14, 4:15, 5:16, 6:17,7:18}}
    print_can_data.append(add_data)

=======
    #dict_can_data = {'id': 0, 'lenght':8, 'data':{0:10,1:11,2:12,3:13,4:14,5:15,6:16,7:17}}
    system('cls')
    print(dict_can_data[3])
    for i in range(5):
        dict_can_data[i] = dict(id=i, lenght=8, data={0:10+i,1:11,2:12,3:13,4:14,5:15,6:16,7:17})
        for j in range(8):
            dict_can_data[i]['data'][j] = random.randrange(0,0x0F)
        
    for i in range(5):
        print(dict_can_data[i])
    print('====================================================================')
>>>>>>> 2a5847c3fb7b4d954c3bf0d21a6215949fe0ab33
    '''list_can_data = [1, 2, random.randrange(0,0xFF), random.randrange(0,0xFF), random.randrange(0,0xFF),
                     random.randrange(0,0xFF), random.randrange(0,0xFF), random.randrange(0,0xFF), random.randrange(0,0xFF), random.randrange(0,0xFF)]

    #print('ID\tLength\tData1\tData2\tData3\tData4\tData5\tData6\tData7\tData8\n')
    
    if list_can_data != list_can_data_prev and check_btn_var_light_up.get() is True:
        for i in range(8):
            if list_can_data[i] != list_can_data_prev[i]:
                print(colored(hex(list_can_data_prev[i]), None, 'on_magenta'), end='\t')
            else:
                print(hex(list_can_data_prev[i]), end='\t')
    else:
        print(*list_can_data_prev, sep='\t')

    list_can_data_prev = list_can_data'''
    
    #end test

    if check_btn_var.get() is False: #if checkbtn pressed
        entry_can_filter.config(state=DISABLED)
        entry_can_mask.config(state=DISABLED)
    else:
        entry_can_filter.config(state=NORMAL)
        entry_can_mask.config(state=NORMAL)
    
    root.after(500, printing)


root.after(500, printing)
root.mainloop()