from tkinter import *
from tkinter import messagebox
from password_gen import password_generator
import pyperclip

FONT = ("Arial", 12,'bold')
FONT_2 = ("Arial", 12)

def generate_password():
    password = password_generator()
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

def save_password():
    website = website_entry.get()
    email = email_entry.get()
    passsword = password_entry.get()

    if len(website) == 0 or len(passsword) == 0:
        messagebox.showwarning(title="Oops", message="Please fill in all fields before saving.")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"These are the details you have entered:\nEmail: {email}\nPassword: {passsword}\nClick Ok to save, click cancel to go back")
        if is_ok:
            with open('passwords.txt',mode='a') as file:
                file.write(f"{website} | {email} | {passsword}\n")
            website_entry.delete(0,END)
            password_entry.delete(0,END)
            website_entry.focus()
            messagebox.showinfo(title="Success", message="Password saved successfully!")

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
window.geometry("600x400+550+300")


canvas = Canvas(width=200,height=200)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

website_label=Label(text="Website:",font=FONT)
website_label.grid(row=1,column=0)

website_entry = Entry(width=42,font=FONT_2)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()

email_label=Label(text="Email/Username:",font=FONT)
email_label.grid(row=2,column=0)

email_entry = Entry(width=42,font=FONT_2)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"xyz@email.com")

password_label=Label(text="Password:",font=FONT)
password_label.grid(row=3,column=0)

password_entry = Entry(width=33,font=FONT_2)
password_entry.grid(row=3,column=1)

generate_button = Button(text="Generate",font=FONT_2,command=generate_password)
generate_button.grid(row=3,column=2)

add_button = Button(text="Add",width=42,font=FONT_2,command=save_password)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()