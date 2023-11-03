import tkinter as tk
from tkinter import Menu
from tkinter.messagebox import askyesno

#SELF IMPORTS
import settings
import databaseManager as dbM
import weatherAPI as weather

# Variables

isLoggedIn = False

# Functions

def Login(_user, _pwd):
    global isLoggedIn
    if _user == dbM.CheckUserInDB(_user):
        if _pwd == dbM.CheckUserPwd(_user):
            isLoggedIn = True   
        else:
            print('Your user or password is not correct! Try again.')
    else:
        print('Your user or password is not correct! Try again.')

# LOGIN
user = input('user: ')
pwd = input('password: ')
Login(user, pwd)

# User Interface

if isLoggedIn:
    root = tk.Tk()

    root.title(settings.APP_TITLE)

    root.configure(bg=settings.COLOR_BACKGROUND)
    root.minsize(settings.GetWindowWidth(root) // 3, settings.GetWindowHeight(root) // 3)
    root.maxsize(settings.GetWindowWidth(root) // 3, settings.GetWindowHeight(root) // 3)
    root.resizable(False, False)
    root.iconbitmap('./imgs/icons/code-signs.ico')

    #Show and INIT the bar menu
    mainMenu = Menu(root)
    root.config(menu=mainMenu)
    openMenu = Menu(mainMenu, tearoff=False)

    openMenu.add_command(
        label='Logout',
        command=root.destroy
    )
    mainMenu.add_cascade(
        label=user,
        menu=openMenu
    )

    # 1 line
    lbl_welcome = tk.Label(
        root,
        text=settings.APP_TITLE.upper(),
        padx=10, pady=10,
        font='Arial 10',
        bg=settings.COLOR_BACKGROUND,
        fg=settings.COLOR_WHITE
    )
    lbl_welcome.place(x=0, y=0)

    # Clock
    def UpdateClock():
        lbl_hours.config(text=settings.GetCurrentHour())
        root.after(1000, UpdateClock)

    lbl_hours = tk.Label(
        root,
        padx=10, pady=10,
        font='Arial 10',
        bg=settings.COLOR_BACKGROUND,
        fg=settings.COLOR_WHITE
    )
    lbl_hours.place(x=(settings.GetWindowWidth(root) // 3)-75, y=0)
    UpdateClock()

    # 2 line
    btn_mainButton = tk.Button(
        root,
        text='DON\'T CLICK ME!',
        bg=settings.COLOR_LIGHTGREY,
        fg=settings.COLOR_WHITE,
        padx=10, pady=5,
        bd=0,
        command=root.destroy
    )
    btn_mainButton.place(x=0, y=50)

    def UpdateWeather():
        lbl_weather.config(text=f"{weather.GetTemp(settings.USER_CITY)} ºC")
        root.after(300000, UpdateClock) # 5 min update time (300000)

    lbl_weather = tk.Label(
        root,
        #text=f"{weather.GetTemp('Viseu')} ºC",
        padx=10, pady=10,
        font='Arial 10',
        bg=settings.COLOR_BACKGROUND,
        fg=settings.COLOR_WHITE
    )
    lbl_weather.place(x=(settings.GetWindowWidth(root) // 3)-75, y=30)
    UpdateWeather()


    root.mainloop()