import tkinter as tk
import settings
import databaseManager as dbM

# Variables

isLoggedIn = False

# Functions

def Login(_user, _pwd):
    global isLoggedIn
    if _user == dbM.CheckUserInDB(_user):
        if _pwd == dbM.CheckUserPwd(_user):
            isLoggedIn = True   
        else:
            return
    else:
        return

# LOGIN

user = input('user: ')
pwd = input('user: ')
Login(user, pwd)

# User Interface

if isLoggedIn:
    root = tk.Tk()

    root.title(settings.APP_TITLE)

    root.configure(bg=settings.COLOR_BACKGROUND)
    root.minsize(settings.GetWindowWidth(root) // 3, settings.GetWindowHeight(root) // 3)
    root.maxsize(settings.GetWindowWidth(root), settings.GetWindowHeight(root))


    lbl_welcome = tk.Label(
        root,
        text=f'Welcome, {user}',
        padx=10, pady=10,
        font='Arial 10',
        bg=settings.COLOR_BACKGROUND,
        fg=settings.COLOR_WHITE
    )
    lbl_welcome.grid(column=0, row=0)


    root.mainloop()