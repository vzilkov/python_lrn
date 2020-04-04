import class_can_data
from tkinter import *

can_data = class_can_data.can_data()

root = Tk()

root.resizable(FALSE, FALSE)

#buttons
check_btn_var = BooleanVar(value=FALSE)
check_btn_var_light_up = BooleanVar(value=FALSE)

checkbutton_filters_masks = Checkbutton(root, 
                                        text='Check can filter & mask', 
                                        var=check_btn_var)
checkbutton_filters_masks.grid(row=0, column=1)

checkbutton_light_up = Checkbutton(root, text='Light up changed data', var=check_btn_var_light_up)
checkbutton_light_up.grid(row=3, column=1)

checkbutton_trace = Checkbutton(root, text='Fixed/Rolling trace')
checkbutton_trace.grid(row=4, column=1)

#Label
label_can_filter = Label(root, text='Filter:')
label_can_filter.grid(row=1, column=0)

label_can_mask = Label(root, text='Mask:')
label_can_mask.grid(row=2, column=0)

#entry
entry_can_filter = Entry(root, text='enter vals in hex 0-7FF')
entry_can_filter.grid(row=1, column=1)

entry_can_mask = Entry(root, text='enter values in hex 0-7FF')
entry_can_mask.grid(row=2, column=1)

#place root window to right
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
positionRight = int(root.winfo_screenwidth() - windowWidth)
positionDown = -30-1#int(root.winfo_screenheight() - windowHeight)
root.geometry('%sx%s'%(windowWidth, root.winfo_screenheight()))
root.geometry("+{}+{}".format(positionRight, positionDown))

'''can_data.append_can_buf(1,8,3,4,5,6,7,8,9,10)
can_data.print_data()
can_data.append_can_buf(2,1,2)
can_data.print_data()
can_data.append_can_buf(3,4,1,2,3,4)
can_data.print_data()
can_data.append_can_buf(3,3,1,2,3)
can_data.print_data()'''

root.mainloop()