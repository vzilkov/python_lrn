from tkinter import *

#test
import random

root = Tk()
root.geometry("1024x600")
root.resizable(FALSE, FALSE)

check_btn_var = BooleanVar(value=FALSE)

textbox = Text(root, heigh=30, width=80)
textbox.tag_config('changed', background ='GREY', foreground='white')
textbox.config(state='disabled')
#scroll_text = Scrollbar(orient=VERTICAL, command=textbox.yview)
#textbox.configure(yscrollcommand=scroll_text.set)
#scroll_text.pack(side="right", fill="y")

fontstyle = ('sans-serif', 11)
label_can_data_text = Label(root, text='  ID      Length      Data1      Data2      Data3       Data4      Data5      Data6       Data7       Data8', font=fontstyle)
label_can_data_text.config(font=fontstyle)
textbox.pack(side=LEFT)

#buttons
checkbutton_filters_masks = Checkbutton(root, 
                                        text='Check can filter & mask', 
                                        var=check_btn_var)

checkbutton_light_up = Checkbutton(root, text='Light up changed data')

checkbutton_trace = Checkbutton(root, text='Fixed/Rolling trace')

#Label
label_can_filter = Label(root, text='Filter:')

label_can_mask = Label(root, text='Mask:')

#entry
entry_can_filter = Entry(root, text='enter vals in hex 0-7FF')
entry_can_mask = Entry(root, text='enter values in hex 0-7FF')

#places
x_column_periph = 650

textbox.place(x=0, y=20)
label_can_data_text.place(x=0, y=0)

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
    global check_btn_var

    #start test

    list_can_data = [1, 2, random.randrange(0,0xFF), random.randrange(0,0xFF), random.randrange(0,0xFF),
                     random.randrange(0,0xFF), random.randrange(0,0xFF), random.randrange(0,0xFF), random.randrange(0,0xFF), random.randrange(0,0xFF)]

    global list_can_data_prev

    textbox.config(state='normal')
    column_text = 0
    for i in range(10):
        textbox.insert(0.0, '%x\t' % (list_can_data[i]))
        #print('Textbox index : ', textbox.get(2), ' Column num: ', column_text)
        column_text +=1
    textbox.config(state='disabled')
    #textbox.yview('end')
    textbox.insert('2.0', '\n')
    
    count += 1
    '''textbox.insert('0.0', '%x\t%x\t%x\t%x\t%x\t%x\t%x\t%x\t%x\t' % 
                (list_can_data[1], list_can_data[2], list_can_data[3], list_can_data[4],
                list_can_data[5], list_can_data[6], list_can_data[7], list_can_data[8], list_can_data[9]) + '\n')'''

    if count == 255:
        count = 0
    #end test


    if check_btn_var.get() is False: #if checkbtn pressed
        entry_can_filter.config(state=DISABLED)
        entry_can_mask.config(state=DISABLED)
        
    else:
        entry_can_filter.config(state=NORMAL)
        entry_can_mask.config(state=NORMAL)
    
        
    root.after(50, printing)


root.after(100, printing)
root.mainloop()