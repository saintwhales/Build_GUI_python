from tkinter import *
from tkinter import ttk

root = Tk()
root.title("System Login")
root.geometry("400x180")

Label(root, text="Username").grid(row=0, column=0, padx=10, pady=10)
Label(root, text="Password").grid(row=1, column=0, padx=10, pady=10)

username_entry = Entry(root, width=20)
username_entry.grid(row=0, column=1, padx=10, pady=10)

password_entry = Entry(root, width=20, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)


def login():
    username = username_entry.get()
    password = password_entry.get()
    print("Username:", username)
    print("Password:", password)


def cancel():
    root.destroy()


style = ttk.Style()
style.theme_use("clam")
style.configure(
    "green.TButton",
    background="lightgreen",
    foreground="white",
)

style = ttk.Style()
style.theme_use("clam")
style.configure(
    "salmon.TButton",
    background="salmon",
    foreground="white",
)

login_btn = ttk.Button(
    root, text="Login", style="green.TButton", width=10, command=login
)
login_btn.grid(row=2, column=0, padx=10, pady=20)

cancel_btn = ttk.Button(
    root, text="Cancel", style="salmon.TButton", width=10, command=cancel
)
cancel_btn.grid(row=2, column=1, padx=10, pady=20)

root.mainloop()
