import tkinter as tk
FONT= ('courier', 12,'bold')

window = tk.Tk()
window.title("New Window")
window.minsize(300,150)

miles_entry = tk.Entry()
miles_entry.config(width=10)
miles_entry.grid(column=1,row=0)

miles_label = tk.Label(text = "Miles", font=FONT)
miles_label.grid(column=2,row=0)

conversion_label = tk.Label(text = "is equal to", font=FONT)
conversion_label.grid(column=0,row=1)

def convert():
    miles = miles_entry.get()
    km = 1.60934*int(miles)
    km_label.config(text=round(km,2))
    return km

km_label = tk.Label(text = f"0", font=FONT)
km_label.grid(column=1,row=1)

km_label_text = tk.Label(text = f"Kilometers", font=FONT)
km_label_text.grid(column=2,row=1)

calculate = tk.Button(text="Calculate", command=convert)
calculate.grid(column=1,row=2)

window.mainloop()
