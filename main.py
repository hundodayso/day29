from tkinter import *
from tkinter import messagebox
import random
import pyperclip
FONT_NAME = "Arial"
FONT_SIZE = 10

hello = "leng"a

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8,10)
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)




    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password =  "".join(password_list)
    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD -------------------------------- #
def save():
    with open('storage.txt', 'a') as data_file:
        website = website_input.get()
        username = username_input.get()
        password = password_input.get()
        #string = str(website_input.get()) + ' | ' + str(username_input.get()) + ' | ' + str(password_input.get()) + '\n'
        if len(website) == 0 or len(username) == 0 or len(password) == 0:
            messagebox.showwarning(title="Blank fields!", message="Please do not leave any blank fields!")

        else:
            is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {username}"
                                                          f"\nPassword: {password} \n\n Is it ok to save?")
            if is_ok:
                data_file.write(f"{website} | {username} | {password}\n")
                website_input.delete(0, END)
                username_input.delete(0, END)
                password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
canvas.config(highlightthickness=0, )
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)

canvas.grid(column=1, row=0)

###Website Row
website_label = Label(text="Website:", font=(FONT_NAME, FONT_SIZE, "bold"))
website_label.grid(column=0, row=1, sticky=E)

website_input = Entry(width=35)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2, sticky=N+E+S+W)


###Username Row
username_label = Label(text="Email/Username:", font=(FONT_NAME, FONT_SIZE, "bold"))
username_label.grid(column=0, row=2, sticky=E)

username_input = Entry(width=35)
username_input.grid(column=1, row=2, columnspan=2, sticky=N+E+S+W)

##Password Row
password_label = Label(text="Password:", font=(FONT_NAME, FONT_SIZE, "bold"))
password_label.grid(column=0, row=3, sticky=E)

password_input = Entry(width=21)
password_input.grid(column=1, row=3, sticky=N+E+S+W)

generate_button = Button(text="Generate Password", font=(FONT_NAME, FONT_SIZE, "bold"), command=generate_password)
generate_button.grid(column=2, row=3, sticky=W)

##Add button
add_button = Button(text="Add", font=(FONT_NAME, FONT_SIZE, "bold"), width=36, command=save)
add_button.grid(column=0, row=4, columnspan=3, pady=10)


window.mainloop()