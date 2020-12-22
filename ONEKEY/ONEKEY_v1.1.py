
import tkinter as tk 
import base64
 
def update_method():
    value = lb.get(lb.curselection()) 
    method.set(value) 
    return value

def translate():
    newmethod=update_method()
    var = e.get()
    t.delete("1.0","end")
    result=""
    if var!="":
        if newmethod=="Base16":
            result = base64.b16encode(bytes(var.encode('utf-8'))).decode('utf-8')
        elif newmethod=="Base32":
            result = base64.b32encode(bytes(var.encode('utf-8'))).decode('utf-8')
        elif newmethod=="Base64":
            result = base64.b64encode(bytes(var.encode('utf-8'))).decode('utf-8')
        elif newmethod=="Base85":
            result = base64.b85encode(bytes(var.encode('utf-8'))).decode('utf-8')
    t.insert('insert', result)

window = tk.Tk()
 
window.title('ONEKEY')
 
window.geometry('420x290') 
 
e = tk.Entry(window, show = None)

e.place(x=30, y=60, anchor='nw')

method = tk.StringVar() 
l = tk.Label(window,font=('Arial', 12), width=10, textvariable=method)

l.place(x=30, y=30, anchor='nw');
 
choice = tk.StringVar()
choice.set(("Base16","Base32","Base64","Base85"))
lb = tk.Listbox(window, listvariable=choice,height=4)
lb.select_set(2)

lb.place(x=230, y=30, anchor='nw')

value = lb.get(lb.curselection()) 
method.set(value) 

b1 = tk.Button(window, text='Get my key', width=10, height=1, command=translate)
b1.place(x=30, y=90, anchor='nw')

t = tk.Text(window, height=10,width=50)
t.place(x=30, y=130, anchor='nw')
 
window.mainloop()