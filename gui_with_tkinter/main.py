import tkinter as tk

window = tk.Tk()
window.title("New Window")
window.minsize(600,600)

label1 = tk.Label(text = "This is a Label", font=('courier', 20,'bold'))
label1.pack()

def button_click():
    word = entry1.get()
    label1.config(text=word)

button1 = tk.Button(text="Button", command=button_click)
button1.pack()

entry1 = tk.Entry()
entry1.config(width=10)
entry1.pack()
print(entry1.get())
window.mainloop()
