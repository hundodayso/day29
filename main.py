from tkinter import *

FONT_NAME = "Arial"
FONT_SIZE = 10
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    with open('storage.txt', 'a') as file:
        string = str(website_label',')
        file.write(str(website_label) + ',' +   )




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

generate_button = Button(text="Generate Password", font=(FONT_NAME, FONT_SIZE, "bold"))
generate_button.grid(column=2, row=3, sticky=W)

##Add button
add_button = Button(text="Add", font=(FONT_NAME, FONT_SIZE, "bold"), width=36, command=save)
add_button.grid(column=0, row=4, columnspan=3, pady=10)


window.mainloop()