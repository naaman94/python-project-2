from tkinter import *
root = Tk()
screen_width=root.winfo_screenwidth()/2
screen_height=root.winfo_screenheight()/2
root.geometry("400x150+"+str(int(screen_width-300/2))+"+"+str(int(screen_height-150/2)) )

root.title('Project 2')
def notdone():
    messagebox.showinfo('Not implemented', 'Not yet available')

def _about():
    messagebox.showinfo('About us', 'Coding Academy Orange JO')
    
top = Menu(root)
root.config(menu=top)
file = Menu(top,tearoff=0)
file.add_command(label='Reports', command=notdone)
file.add_separator()
file.add_command(label='Exit', command=root.destroy)
top.add_cascade(label='File', menu=file)

Employees = Menu(top,tearoff= 0)
Employees.add_command(label='Add', command=notdone)
Employees.add_command(label='View', command=notdone)
Employees.add_command(label='Delete', command=notdone)
top.add_cascade(label='Employees', menu=Employees)

Students = Menu(top,tearoff= 0)
Students.add_command(label='Add', command=notdone)
Students.add_command(label='View', command=notdone)
Students.add_command(label='Delete', command=notdone)
top.add_cascade(label='Students', menu=Students)

Help = Menu(top,tearoff= 0)
Help.add_command(label='About', command=_about)
top.add_cascade(label='Help', menu=Help)
root.mainloop()
