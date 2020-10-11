
import tkinter as tk 
import base64
 

def encode():
    var = e.get()
    t.delete("1.0","end")
    result=""
    if var!="":
        result = base64.b64encode(bytes(var.encode('utf-8'))).decode('utf-8')
    t.insert('insert', result)

def decode():  
    var = e.get()
    t.delete("1.0","end")
    result=""
    if var!="":
        result = base64.b64decode(bytes(var.encode('utf-8'))).decode('utf-8')
    t.insert('insert', result)

window = tk.Tk()
 
window.title('Cryptography Box base64')
 
window.geometry('500x300') 
 
e = tk.Entry(window, show = None)
e.place(x=0, y=0, anchor='nw')

b1 = tk.Button(window, text='encode', width=10, height=2, command=encode)
b2 = tk.Button(window, text='decode', width=10, height=2, command=decode)
b1.place(x=0, y=30, anchor='nw')
b2.place(x=100, y=30, anchor='nw')

t = tk.Text(window, height=10)
t.place(x=0, y=70, anchor='nw')
 
window.mainloop()