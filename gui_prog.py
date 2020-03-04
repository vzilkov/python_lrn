from tkinter import *

root = Tk()
root.geometry("1024x600")
root.resizable(FALSE, FALSE)

check_btn_var = BooleanVar(value=FALSE)

textbox = Text(root, heigh=30, width=40)
#textbox.grid(row=0, column=0)
textbox.pack(side=LEFT)

#buttons
checkbutton_filters_masks = Checkbutton(root, 
                                        text='Check can filter & mask', 
                                        var=check_btn_var)
#checkbutton_filters_masks.grid(row=0, column=3)

checkbutton_light_up = Checkbutton(root, text='Light up changed data')
#checkbutton_light_up.grid(row=2, column=1)

checkbutton_trace = Checkbutton(root, text='Fixed/Rolling trace')
#checkbutton_trace.grid(row=2, column=2)

#Label
label_can_filter = Label(root, text='Filter:')
#label_can_filter.grid(row=0, column=1)

label_can_mask = Label(root, text='Mask:')
#label_can_mask.grid(row=1, column=1)

#entry
entry_can_filter = Entry(root, text='enter vals in hex 0-7FF')
#entry_can_filter.grid(row=0, column=2)


entry_can_mask = Entry(root, text='enter vals in hex 0-7FF')
#entry_can_mask.grid(row=1, column=2)

checkbutton_filters_masks.place(x=500, y=10)

label_can_mask.place(x=500, y=50)
entry_can_mask.place(x=540, y=50)

entry_can_filter.place(x=540, y=80)
label_can_filter.place(x=500, y=80)

count = 0


def printing():
    global count
    global check_btn_var
    
    textbox.insert('0.0', 'print %d' % ((count)) + entry_can_filter.get() + '\n')

    if check_btn_var.get() is True: #if checkbtn pressed
        textbox.insert('0.0', 'checkbutton pressed' + '\n')
        entry_can_filter.config(state=DISABLED)
        entry_can_mask.config(state=DISABLED)
        
    else:
        entry_can_filter.config(state=NORMAL)
        entry_can_mask.config(state=NORMAL)
        count += 1
    
    root.after(50, printing)


root.after(100, printing)
root.mainloop()