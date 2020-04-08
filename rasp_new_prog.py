import class_can_data
from tkinter import *

can_data = class_can_data.can_data()

root = Tk()

#root.resizable(FALSE, FALSE)

#buttons
check_btn_var = BooleanVar(value=FALSE)
check_btn_var_light_up = BooleanVar(value=FALSE)
checkbutton_var_trace = BooleanVar(value=TRUE)

checkbutton_filters_masks = Checkbutton(root, 
                                        text='Check can filter & mask', 
                                        var=check_btn_var)
#checkbutton_filters_masks.grid(row=0, column=2)


checkbutton_light_up = Checkbutton(root, text='Light up changed data', var= check_btn_var_light_up)
#checkbutton_light_up.grid(row=3, column=2)


checkbutton_trace = Checkbutton(root, text='Fixed/Rolling trace', var= checkbutton_var_trace)
#checkbutton_trace.grid(row=4, column=2)


#Label
label_can_filter = Label(root, text='Filter:')
#label_can_filter.grid(row=1, column=1)


label_can_mask = Label(root, text='Mask:')
#label_can_mask.grid(row=2, column=1)


#entry
entry_can_filter = Entry(root, text='enter vals in hex 0-7FF')
#entry_can_filter.grid(row=1, column=2)


entry_can_mask = Entry(root, text='enter values in hex 0-7FF')
#entry_can_mask.grid(row=2, column=2)

#place root window to right
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
positionRight = int(root.winfo_screenwidth() - windowWidth)
positionDown = int(root.winfo_screenheight() - windowHeight)

#textbox & scrollbar:
ybar = Scrollbar(root, width=30)
textbox = Text(root, width=90, height=root.winfo_screenheight(), font=('Courier New', 16))
ybar.config(command=textbox.yview)
textbox.config(yscrollcommand=ybar.set)

#packs:
textbox.pack(side=LEFT)
ybar.pack(side=LEFT, fill=BOTH)
checkbutton_light_up.pack(side=TOP)
checkbutton_trace.pack(side=TOP)
checkbutton_filters_masks.pack(side=TOP)
label_can_filter.pack(side=TOP)
entry_can_filter.pack(side=TOP)
label_can_mask.pack(side=TOP)
entry_can_mask.pack(side=TOP)

#root.geometry('%sx%s' % (root.winfo_screenwidth(), root.winfo_screenheight()))
#root.geometry("+{}+{}".format(0, 0))

root.attributes('-fullscreen', True)

def period():
    can_data.read_data()
    #can_data.print_data()

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

    root.after(50, period)

root.after(300, period)
root.mainloop()