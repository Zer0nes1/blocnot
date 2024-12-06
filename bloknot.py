from tkinter import *

root=Tk()
root.title('Текстовый редактор')
root.geometry('600x700')

main_menu=Menu(root)


# файл
file_menu=Menu(main_menu, tearoff=0)
file_menu.add_command(label='Открыть')
file_menu.add_command(label='Сохранить')
file_menu.add_command(label='Закрыть')
root.config(menu=file_menu)

main_menu.add_cascade(label='Файл',menu=file_menu)

root.config(menu=main_menu)




f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

text_fild=Text(f_text, bg='white',fg='black', padx=10,pady=10, wrap=WORD,insertbackground='black', selectbackground='blue', spacing3=10,width=30)
text_fild.pack(expand=1, fill=BOTH, side=LEFT)

scroll=Scrollbar(f_text, command=text_fild.yview)
scroll.pack(side=LEFT, fill=Y)
text_fild.config(yscrollcommand=scroll.set)

root.mainloop()