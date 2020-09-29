from tkinter import *
mainWindow = Tk() 

mainWindow.title("PHI Scanning Automation")
canvas_width=1280
canvas_height=720
mainWindow.geometry(f"{canvas_width}x{canvas_height}")
mainWindow.minsize(canvas_width,canvas_height)
mainWindow.maxsize(canvas_width,canvas_height)

f2 = Frame(mainWindow,bg='white',borderwidth=1,relief=SUNKEN) #as we want to pack frame in mainwindow
f2.pack(side=TOP,fill='x')

l=Label(f2,text='PHI SCANNING',font="Helvetica 16 bold",bg='white')
l.pack()

f3 = Frame(mainWindow,bg='white',borderwidth=1,relief=SUNKEN) #as we want to pack frame in mainwindow
f3.pack(side=TOP,anchor='nw')

username = Label(f3, text='User Name',bg='white')
password = Label(f3, text='Password',bg='white')
host = Label(f3, text='Host',bg='white')
service = Label(f3, text='Service Name',bg='white')
port = Label(f3, text='Port',bg='white')
username.grid(row=2)
password.grid(row=3)
host.grid(row=4)
service.grid(row=5)
port.grid(row=6)

user_val = StringVar()
pass_val = StringVar()
host_val = StringVar()
service_val = StringVar()
port_val = StringVar()

user_entry = Entry(f3, textvariable=user_val)
pass_entry = Entry(f3, textvariable=pass_val)
host_entry = Entry(f3, textvariable=host_val)
service_entry = Entry(f3, textvariable=service_val)
port_entry = Entry(f3, textvariable=port_val)

user_entry.grid(row=2, column=1)
pass_entry.grid(row=3, column=1)
host_entry.grid(row=4, column=1)
service_entry.grid(row=5, column=1)
port_entry.grid(row=6, column=1)

def getvals():
    print(user_val.get())
    print(pass_val.get())

cred_save=IntVar()
save_creds=Checkbutton(f3,text='Wanna save creds !!',variable=cred_save).grid(row=7,column=1)
Button(f3,text='Submit', command=getvals).grid(column=1)
mainWindow.mainloop() 
