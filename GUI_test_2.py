import random
import base64
from tkinter import Tk, Label, Button, Entry, StringVar, DISABLED, NORMAL, END, W, E

class Base:
    def __init__(self, master):
        self.master = master
        master.title("Fluorite-Base-testing")
        self.input=None
        self.message = "Chose to encode or decode."
        self.label_text = StringVar()
        self.label_text.set(self.message)
        self.label = Label(master, textvariable=self.label_text)

        self.result = ""
        self.label_text = StringVar()
        self.label_text.set(self.message)
        self.label = Label(master, textvariable=self.label_text)

        vcmd = master.register(self.validate)
        self.entry = Entry(master, validate="key")
        self.Encode_button = Button(master, text="Encode", command=self.encode,state=NORMAL)
        self.Decode_button = Button(master, text="Decode", command=self.decode,state=NORMAL)
        self.Quit_button = Button(master, text="Quit", command=master.quit,state=NORMAL)
        self.reset_button = Button(master, text="Reset", command=self.reset, state=NORMAL)

        self.label.grid(row=0, column=0, columnspan=2, sticky=W+E)
        self.entry.grid(row=1, column=0, columnspan=2, sticky=W+E)
        self.Encode_button.grid(row=2, column=1)
        self.Decode_button.grid(row=2, column=2)
        self.reset_button.grid(row=2, column=3)
        self.Quit_button.grid(row=2,column=4)

    def validate(self, new_text):
        if not new_text: # the field is being cleared
            self.input = None
            return True

        try:
            if type(self.input)==str:
                return True
            else:
                return False
        except ValueError:
            return False

    def encode(self):
        result = base64.b64encode(bytes(self.input.encode('utf-8'))).decode('utf-8')
        self.result = result

    def decode(self):
        result = base64.b64decode(bytes(self.input.encode('utf-8'))).decode('utf-8')
        self.result = result

    def reset(self):
        self.input.delete(0, END)

root = Tk()
my_gui = Base(root)
root.mainloop()