from tkinter import *

#test
import random
from colorama import init 
from termcolor import colored 

root = Tk()
root.geometry("1024x600")
root.resizable(FALSE, FALSE)

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

def printing():
    global count
    global check_btn_var, check_btn_var_light_up
    global list_can_data_prev
    #start test

    matrix = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
            [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]]
    print(len(matrix))
    a = [20,21,22,23,24,25,26,27,28,29]
    matrix.append(a)
    for row in range(10)
        print(*matrix)
    '''list_can_data = [1, 2, random.randrange(0,0xFF), random.randrange(0,0xFF), random.randrange(0,0xFF),
                     random.randrange(0,0xFF), random.randrange(0,0xFF), random.randrange(0,0xFF), random.randrange(0,0xFF), random.randrange(0,0xFF)]

    print('ID\tLength\tData1\tData2\tData3\tData4\tData5\tData6\tData7\tData8\n')
    
    if list_can_data != list_can_data_prev and check_btn_var_light_up.get() is True:
        for i in range(10):
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
    
    root.after(100, printing)


root.after(400, printing)
root.mainloop()