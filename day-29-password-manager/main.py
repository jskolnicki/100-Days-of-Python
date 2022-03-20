import tkinter
import os
import random
from tkinter import messagebox
import pyperclip


os.chdir(os.path.dirname(__file__))

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
special_chars = ['!','@','#','$','%','^','&','*','(',')']
all_chars = characters + numbers + special_chars

def generate_password():
    global password_entry, username_entry
    password_entry.delete(0,'end')
    password_chars = []
    password_chars.append(random.choice(characters))
    password_chars.append(random.choice(numbers))
    password_chars.append(random.choice(special_chars))
    [password_chars.append(random.choice(all_chars)) for letter in range(random.randint(12,16))]
    random.shuffle(password_chars)
    new_password = "".join(password_chars)
    pyperclip.copy(new_password)
    return password_entry.insert(0,new_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    if len(website_entry.get()) > 0 and len(username_entry.get()) > 0 and len(password_entry.get()) > 0 :
        new_password = f"{website_entry.get()} | {username_entry.get()} | {password_entry.get()}\n"
        try:
            is_ok = messagebox.askyesno(title="Save Password", message=f'Website: {website_entry.get()}\nUsername: {username_entry.get()}\nPassword: {password_entry.get()}\n\nAre you sure you want to save?')
            if is_ok:
                with open("data.txt", "a") as file_object:
                    file_object.write(new_password)
                    messagebox.showinfo(title="Success!",message="Your password has been saved.")
                    website_entry.delete(0,'end')
                    password_entry.delete(0,'end')
        except:
             messagebox.showinfo(title="Oops!",message="Something went wrong. Password not saved.")
    
    else:
        messagebox.showinfo(title="Oops!",message="You must fill out all of the fields.")


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg='light gray')


canvas = tkinter.Canvas(width=200, height=200, bg='light gray', highlightthickness=0)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image= logo_img)

canvas.grid(row=0, column=1)

website_label = tkinter.Label(text="Website: ", bg='light gray')
website_label.grid(row=1, column= 0, pady=2)

website_entry = tkinter.Entry(width=54)
website_entry.grid(row=1,column=1, columnspan=2, sticky='w')
website_entry.focus()

username_label = tkinter.Label(text="Email/Username: ", bg='light gray')
username_label.grid(row=2, column= 0, pady=2)

username_entry = tkinter.Entry(width=54)
username_entry.grid(row=2,column=1, columnspan=2, sticky='w')
username_entry.insert(0,"jaredskolnicki@gmail.com")


password_label = tkinter.Label(text="Password: ", bg='light gray')
password_label.grid(row=3, column= 0, pady=1)

password_entry = tkinter.Entry(width= 35)
password_entry.grid(row=3,column=1, sticky='w')

generate_password_button = tkinter.Button(text="Generate Password", command= generate_password, width= 15, height= 1)
generate_password_button.grid(row=3, column=2, pady=2)

add_button = tkinter.Button(text="Add", command= save_password, width=46)
add_button.grid(row=4,column=1, columnspan=2, sticky='w', pady=1)

window.mainloop()