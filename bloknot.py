from tkinter import *
from tkinter import filedialog, messagebox
from tkinter import simpledialog



def new_file():
    text_fild.delete('1.0', END)  # Очистка текстового поля
    root.title("Новый файл - Текстовый редактор")

def notepad_exit():
    answer=messagebox.askokcancel('Выход','Вы точно хотите выйти?')
    if answer:
        root.destroy()

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Текстовые файлы", "*.txt")])
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            text_fild.delete(1.0, END)
            text_fild.insert(1.0, file.read())
        root.title(f"{file_path} - Текстовый редактор")

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Текстовые файлы", "*.txt")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text_fild.get(1.0, END))
        root.title(f"{file_path} - Текстовый редактор")

def cut_text():
    text_fild.event_generate("<<Cut>>")  

def copy_text():
    text_fild.event_generate("<<Copy>>")  

def paste_text():
    text_fild.event_generate("<<Paste>>") 

def change_window_size():
    try:
        # Запрос ввода нового размера окна
        new_width = int(simpledialog.askstring("Ввод", "Введите ширину окна:"))
        new_height = int(simpledialog.askstring("Ввод", "Введите высоту окна:"))
        root.geometry(f"{new_width}x{new_height}")
    except (ValueError, TypeError):  # Учитываем пустой ввод или неправильные данные
        messagebox.showerror("Ошибка", "Введите корректные числовые значения!")

root=Tk()
root.title('Текстовый редактор')
root.geometry('600x700')

main_menu=Menu(root)


# файл
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label="Новый", command=new_file)
file_menu.add_command(label='Открыть', command=open_file)
file_menu.add_command(label='Сохранить', command=save_file)
file_menu.add_command(label='Закрыть',command=notepad_exit)
root.config(menu=file_menu)

# редактировать
view_menu=Menu(main_menu,tearoff=0)
view_menu.add_command(label="Вырезать", command=cut_text)
view_menu.add_command(label="Копировать", command=copy_text)
view_menu.add_command(label="Вставить", command=paste_text)

# Меню "Настройки"
settings_menu = Menu(main_menu, tearoff=0)
settings_menu.add_command(label="Изменить размер окна", command=change_window_size)


main_menu.add_cascade(label='Файл',menu=file_menu)
main_menu.add_cascade(label='Редактировать',menu=view_menu)
main_menu.add_cascade(label="Настройки", menu=settings_menu)

root.config(menu=main_menu)




f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

text_fild=Text(f_text, bg='white',fg='black', padx=10,pady=10, wrap=WORD,insertbackground='black', selectbackground='blue', spacing3=10,width=30)
text_fild.pack(expand=1, fill=BOTH, side=LEFT)

scroll=Scrollbar(f_text, command=text_fild.yview)
scroll.pack(side=LEFT, fill=Y)
text_fild.config(yscrollcommand=scroll.set)

root.mainloop()