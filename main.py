import tkinter as tk

def create_window():
    # Создание окна
    root = tk.Tk()
    # - Настройки окна
    root.title('Calculator')
    # Утановить геометрию (начальный размер и позицию окна)
    root.geometry('1000x600')
    # Минимальный размер окна
    root.minsize(400, 300)
    # Максимальный размер окна
    root.maxsize(1920, 1080)
    # Разрешить или заблокировать возможность изсенять размер окна
    root.resizable(width=True, height=True)
    # Цвет фона
    root.config(bg='#0062ff')
    return root

root = create_window()

def plus():
    number1 = int(entry1.get())
    number2 = int(entry2.get())
    sum = number1 + number2
    entry3.insert(tk.END, str(sum))

def minus():
    number1 = int(entry1.get())
    number2 = int(entry2.get())
    min = number1 - number2
    entry3.insert(tk.END, str(min))

def mult():
    number1 = int(entry1.get())
    number2 = int(entry2.get())
    mult = number1 * number2
    entry3.insert(tk.END, str(mult))

def div():
    if int(entry2.get()) == 0:
       entry3.delete(0, tk.END)
       entry3.insert(0, 'На ноль делить нельзя!')
    number1 = int(entry1.get())
    number2 = int(entry2.get())
    div = number1 / number2
    entry3.insert(tk.END, str(div))


def mplus():
    number1 = int(entry1.get())
    number2 = int(entry2.get())
    mplus =  number1 + number2
    entry1.delete(0, tk.END)
    entry1.insert(tk.END, str(mplus))

def mminus():
    number1 = int(entry1.get())
    number2 = int(entry2.get())
    mminus =  number1 - number2
    entry1.delete(0, tk.END)
    entry1.insert(tk.END, str())

def clear():
    number1 = int(entry1.get())
    number2 = int(entry2.get())
    c = entry1.delete(0, tk.END)
    c = entry2.delete(0, tk.END)
    c = entry3.delete(0,tk.END)

def degree():
    number1 = int(entry1.get())
    number2 = int(entry2.get())
    degree = number1 ** number2
    entry3.insert(tk.END, str(degree))





text1 = tk.Label(text='Введите числа', font=('Arial', 26,'bold'), fg='black')
text1.pack()
entry1 = tk.Entry(font=('Arial' , 24, 'bold'), width=25, fg='green', bg='purple')
entry1.pack(pady=20)
entry2 = tk.Entry(font=('Arial', 24, 'bold'),width=25, fg='green', bg='purple')
entry2.pack(pady=20)

text2 = tk.Label(text='Выберите действия', font=('Arial', 26,'bold'), fg='black')
text2.pack()
btn_frame = tk.Frame()
btn_frame.pack()
btn_plus = tk.Button(master=btn_frame, text="+", font=('Arial', 20), fg='black', bg='gold', width=4, height=1, command=plus)
btn_plus.grid(row=1, column=1)
btn_minus = tk.Button(master=btn_frame,text="-", font=('Arial', 20), fg='black', bg='gold', width=4, height=1, command=minus)
btn_minus.grid(row=1, column=5)
btn_mult = tk.Button(master=btn_frame, text="*", font=('Arial', 20), fg='black', bg='gold', width=4, height=1, command=mult)
btn_mult.grid(row=1, column=3)
btn_div = tk.Button(master=btn_frame, text="/", font=('Arial', 20), fg='black', bg='gold', width=4, height=1, command=div)
btn_div.grid(row=1, column=4)
btn_plus = tk.Button(master=btn_frame, text="M+", font=('Arial', 20), fg='black', bg='gold', width=4, height=1, command=mplus)
btn_plus.grid(row=5, column=1)
btn_minus = tk.Button(master=btn_frame,text="C", font=('Arial', 20), fg='black', bg='gold', width=4, height=1, command=clear)
btn_minus.grid(row=5, column=5)
btn_mult = tk.Button(master=btn_frame, text="M-", font=('Arial', 20), fg='black', bg='gold', width=4, height=1, command=mminus)
btn_mult.grid(row=5, column=3)
btn_div = tk.Button(master=btn_frame, text="^", font=('Arial', 20), fg='black', bg='gold', width=4, height=1, command=degree)
btn_div.grid(row=5, column=4)

text3 = tk.Label(text='Ответ', font=('Arial', 26,'bold'), fg='black')
text3.pack()
entry3 = tk.Entry(font=('Arial', 24, 'bold'), width=25, fg='green', bg='purple')
entry3.pack()
root.mainloop()