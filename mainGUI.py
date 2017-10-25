from Tkinter import *
import tkFileDialog
import tkMessageBox
def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()

def save_file():
    save_diag = tkFileDialog.asksaveasfilename()
    if save_diag:
        obj = open(str(save_diag),"w")
        obj.write(text.get("1.0",END))
        obj.close()

def open_file():
    open_diag = tkFileDialog.askopenfilename()
    if open_diag:
        obj = open(str(open_diag),"r")
        text.delete("1.0",END)
        text.insert("1.0",obj.read())
        obj.close()

def new_file():
	if(len(text.get("1.0",END)) > 1):
		tkMessageBox.showinfo("Code For All", "Please save your existing text")
		save_file()
	text.delete("1.0",END)

root = Tk()
root.title("Code For All")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=new_file)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save", command=save_file)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)
editmenu.add_separator()
editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
text = Text(root,font="Verdana")
text.focus_set()
text.pack(side=LEFT,expand=True, fill='both')

scroll = Scrollbar(root)
scroll.pack(side=RIGHT,fill=Y)
scroll.config(command=text.yview)

text.config(yscrollcommand=scroll.set)

root.mainloop()