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


a.mainloop()