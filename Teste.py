import tkinter as tk 
def evaluanete(event);
    result label.config(text=str(eval(entry.get())))
root = tk.TK()
root.title("calculadora Simples")
entry = tk.Entry(root)
entry.bind("<Return>" , evaluate)
entry.pack()
result_label = tk.label(root, text="")
result_label.pack()
root.geometry("250x80")
root.mainloop