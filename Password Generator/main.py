from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import json
import os




# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_name.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        },
    }
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \n"
                                                              f"Password: {password} \nIs it ok to save?")

        if is_ok:
            try:
                with open("user_data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)

            except FileNotFoundError:
                with open("user_data.json", "w") as data_file:
                    # Saving the updated data
                    json.dump(new_data, data_file, indent=4)

            else:
                # Updating the old data with new data
                data.update(new_data)

                with open("user_data.json", "w") as data_file:
                    # Saving the updated data
                    json.dump(data, data_file, indent=4)

            finally:
                website_name.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)
                website_name.focus()

# ------------------------ FIND PASSWORD -------------------------- #


def find_password():
    website = website_name.get()
    try:
        with open("user_data.json", 'r') as data_file:
            data = json.load(data_file)
            password = data[website]

    except FileNotFoundError:
        messagebox.showwarning(title="Error", message=f"No details found for the searched website exist")

    except KeyError:
        messagebox.showwarning(title="Error", message=f"No details found for the searched website exist")

    else:
        messagebox.showinfo(title=website, message=f"Email: {password['email']} \nPassword: {password['password']}")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=190)
logo = PhotoImage(file="I:\sem 4\password manager\password\logo.png")
canvas.create_image(100, 95, image=logo)
canvas.grid(column=1, row=0)

# Labels

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entry's

website_name = Entry(width=34)
website_name.grid(column=1, row=1)
website_name.focus()

email_entry = Entry(width=52)
email_entry.grid(column=1, row=2, columnspan=2)
# email_entry.insert(0, "pratiknawale03@gmail.com")

password_entry = Entry(width=34)
password_entry.grid(column=1, row=3)


# Get the current working directory
current_directory = os.getcwd()

print("Current Directory:", current_directory)

# Buttons

button = Button(text="Generate Password", command=generate_password)
button.grid(column=2, row=3)

add_button = Button(text="Add", width=44, command=save_data)
add_button.grid(column=1, row=4, columnspan=3)

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1)
window.mainloop()
