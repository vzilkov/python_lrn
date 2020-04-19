'''import tkinter
root = tkinter.Tk()
textbox = tkinter.Text(root, width=90, height=root.winfo_screenheight(), font=('Courier New', 16))
textbox.pack(side=tkinter.LEFT)
#textbox.mark_set("insert", "2.0")
textbox.insert("@%d,%d" % (8,1), "Hello!!!")
textbox.insert("@%d,%d" % (4,8), "Bye!!!")
#textbox.insert('1.0', 'Hello!!!')
#textbox.insert('10.4', 'Hello!!!')
root.mainloop()'''
from tkinter import *

root = Tk()
import tabulate
import class_can_data
can_data = class_can_data.can_data()
text = Text(root)
text.insert(INSERT, "\nHello, world!\n")
text.insert(END, "This is a phrase.\n")
text.insert(END, "Bye bye...")
text.pack(expand=1, fill=BOTH)
# adding a tag to a part of text specifying the indices


#can_data.append_can_buf(0,0)
can_data.append_can_buf(1,1,[10,1,2,3,4,5,6,7])
can_data.append_can_buf(2,2,[0,1,2,3,4,5,6,7])
can_data.append_can_buf(3,3,[0,1,2,3,4,5,6,7])
can_data.append_can_buf(4,4,[0,1,2,3,4,5,6,7])
can_data.append_can_buf(5,5,[0,1,2,3,4,5,6,7])
can_data.append_can_buf(6,6,[0,1,2,3,4,5,6,7])
can_data.append_can_buf(7,7,[0,1,2,3,4,5,6,7])
can_data.append_can_buf(8,8,[0,1,2,3,4,5,6,7])

text.insert('0.0', tabulate.tabulate(can_data.can_data_dict, headers='keys', tablefmt='grid'))
index = can_data.can_data_dict['id'].index(1)
for i in range(can_data.can_data_dict['length'][index]):
    print(i)
text.tag_add("start", "4.16", "4.17")
text.tag_config("start", background="blue", foreground="yellow")
text.tag_add("start", "4.22", "4.23")
text.tag_config("start", background="blue", foreground="yellow")
text.tag_add("start", "4.25", "4.26")
text.tag_config("start", background="blue", foreground="yellow")
root.mainloop()