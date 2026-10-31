from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Book Inventory")
root.geometry("600x400")

style = ttk.Style()
style.theme_use("clam")
style.configure(
    "Custom.TButton",
    background="blue",
    foreground="white",
)

Label(root, text="Book Title:").place(x=40, y=60)
Label(root, text="Author:").place(x=40, y=120)
Label(root, text="Price:").place(x=40, y=180)

title_entry = Entry(root, width=40)
title_entry.place(x=150, y=60)

author_entry = Entry(root, width=40)
author_entry.place(x=150, y=120)

price_entry = Entry(root, width=40)
price_entry.place(x=150, y=180)


def save_book():
    title = title_entry.get()
    author = author_entry.get()
    price = price_entry.get()
    print("Title:", title)
    print("Author:", author)
    print("Price:", price)


save_btn = ttk.Button(
    root, text="Save Book", style="Custom.TButton", width=30, command=save_book
)
save_btn.place(x=150, y=280)

root.mainloop()
