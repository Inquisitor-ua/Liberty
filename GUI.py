import tkinter as tk
from tkinter import messagebox

def plus():
    name1 = int(entry1.get())
    name2 = int(entry2.get())
    result.configure(text=f'Результат: {name1+name2}')
    # messagebox.showinfo('na', name1+name2)

def minys():
    name1 = int(entry1.get())
    name2 = int(entry2.get())
    result.configure(text=f'Результат: {name1-name2}')
    # messagebox.showinfo('na', name1-name2)

def mn():
    name1 = int(entry1.get())
    name2 = int(entry2.get())
    result.configure(text=f'Результат: {name1*name2}')
    # messagebox.showinfo('na', name1*name2)

def dl():
    name1 = int(entry1.get())
    name2 = int(entry2.get())
    result.configure(text=f'Результат: {name1/name2}')
    # messagebox.showinfo('na', name1/name2)

root = tk.Tk()
root.title('okno')
root.geometry('500x500')

text =tk.Label(root, text='prugai kakashka', font=('Arial',24))
text.grid(pady=25, row=0, columnspan=4)

entry1 = tk.Entry(root, width=30, font=('Arial',17))
entry1.grid(pady=20, row=1, columnspan=4)
entry2 = tk.Entry(root, width=30, font=('Arial',17))
entry2.grid(pady=20, row=2, columnspan=4)


button_plus = tk.Button(root, text=' + ', font=('Arial',17), command=plus)
button_plus.grid(pady=25, row=4, columnspan=1, column=1, padx=10)
button_minys = tk.Button(root, text=' - ', font=('Arial',17), command=minys)
button_minys.grid(pady=25, row=4, columnspan=1, column=2, padx=10)
button_mn = tk.Button(root, text=' * ', font=('Arial',17), command=mn)
button_mn.grid(pady=25, row=5, columnspan=1, column=1, padx=10)
button_dl = tk.Button(root, text=' / ', font=('Arial',17), command=dl)
button_dl.grid(pady=25, row=5, columnspan=1, column=2, padx=10)

result = tk.Label(root, text='Результат: ', font=('Arial',24))
result.grid(pady=25, row=6, columnspan=4)

# root.grid_columnconfigure(0, weight=1)
root.iconbitmap('o.ico')
root.mainloop()