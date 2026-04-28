import tkinter as t 

from tkinter import filedialog,messagebox

a=t.Tk()
a.title('text editor')
a.geometry('600x400')


text=t.Text(
    a,
    wrap=t.WORD,
    font=('bold',20)
            )

text.pack(expand=True,fill=t.BOTH)

def create_new_file():
    text.delete(1.0,t.END)

def open_file():
    file=filedialog.askopenfilename(
    default='.txt',
    filetypes=[('text','*.txt')])

    if file:
        with open(file,'r') as f:
            text.delete(1.0,t.END)
            text.insert(t.END,f.read())

def save_file():
    file=filedialog.asksaveasfile(
        default='.txt',
        filetypes=[('text','*.txt')]
    )


a.mainloop()