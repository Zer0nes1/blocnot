from tkinter import *

root=Tk()
root.title('Текстовый редактор')
root.geometry('600x700')

f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

text_fild=Text(f_text, bg='white',fg='black', padx=10,pady=10, wrap=WORD,insertbackground='black', selectbackground='blue', spacing3=10,width=30)
text_fild.pack(expand=1, fill=BOTH, side=LEFT)

scroll=Scrollbar(f_text, command=text_fild.yview)
scroll.pack(side=LEFT, fill=Y)
text_fild.config(yscrollcommand=scroll.set)

root.mainloop()