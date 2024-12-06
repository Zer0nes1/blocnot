from tkinter import *

root=Tk()
root.title('Текстовый редактор')
root.geometry('600x700')

f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

text_fild=Text(f_text, bg='white',fg='black')
text_fild.pack(expand=1, fill=BOTH, side=LEFT)

root.mainloop()