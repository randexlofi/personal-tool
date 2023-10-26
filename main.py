import tkinter as tk
import settings
import databaseManager as dbM

root = tk.Tk()
root.title(settings.APP_TITLE)

# CODE
lbl_welcome = tk.Label(
    root,
    text=f'WELCOME TO: {settings.APP_TITLE}',
    padx=5, pady=5,
    font=''
).grid(column=0, row=0)

root.mainloop()