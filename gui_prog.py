from tkinter import *

#test
import random
from colorama import init 
#from termcolor import colored 
from os import system, name 
import pandas
import os
import tabulate

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
#dict_can_data = dict(id=0, lenght=0, data=[0:10,1:11,2:12,3:13,4:14,5:15,6:16,7:17])

#print_can_data = [{'id':11, 'lenght':8, 'data':{0:21,1:22, 2:23, 3:24, 4:25, 5:26, 6:27,7:28}}]
print_can_data = {0: {'id': 11, 'lenght': 8, 
'data0': 21, 'data1': 22, 'data2': 23, 'data3': 24, 
'data4': 25, 'data5': 26, 'data6': 27, 'data7': 28}}

saved_can_bus_data = []

class can_bus_pkg:
    def __init__(self, can_id, can_lenght, *can_data):
        self.can_id = can_id
        self.can_lenght = can_lenght
        self.can_data = can_data
    

    def print_vals(self):
        print('Class vars:')
        print('can_id=', self.can_id)
        print('can_lenght=', self.can_lenght)
        print('can_data=', self.can_data)


def printing():
    global count
    global check_btn_var, check_btn_var_light_up
    global list_can_data_prev
    #start test

    os.system('cls')
    #os.system('clear')

    global saved_can_bus_data
    a = can_bus_pkg(random.randrange(0,5),random.randrange(0,8),[random.randrange(0,111),random.randrange(0,111),random.randrange(0,111),random.randrange(0,111)])
    if len(saved_can_bus_data) == 0:
        saved_can_bus_data.append(a)
        print('=============================Empty list==============================')
    
    for obj in saved_can_bus_data:
        if obj.can_id == a.can_id:
            obj.can_lenght = a.can_lenght
            obj.can_data = a.can_data
            
        else:
            saved_can_bus_data.append(a)
            break

    i=0
    for obj in saved_can_bus_data:
        print(i,' ID: ', obj.can_id, ' lenght: ', obj.can_lenght, ' data: ', obj.can_data)
        i+=1


    #print(print_can_data)
    df = pandas.DataFrame(print_can_data)
    #print(df.to_markdown())
    #print(df)
    #df.to_excel("output.xlsx")
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