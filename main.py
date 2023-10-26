import tkinter as tk
import settings
import databaseManager as dbM

root = tk.Tk()

root.title(settings.APP_TITLE)

root.configure(bg=settings.COLOR_BACKGROUND)
root.minsize(settings.GetWindowWidth(root) // 3, settings.GetWindowHeight(root) // 3)
root.maxsize(settings.GetWindowWidth(root), settings.GetWindowHeight(root))

user = input('> ')

if user == dbM.CheckUserInDB(user):

    # CODE
    lbl_welcome = tk.Label(
        root,
        text=f'Welcome, _user',
        padx=10, pady=10,
        font='Arial 10',
        bg=settings.COLOR_BACKGROUND,
        fg=settings.COLOR_WHITE
    ).grid(column=0, row=0)

else:
    print(f'Can\'t loggin as {user}.')


root.mainloop()
