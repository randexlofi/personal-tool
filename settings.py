import tkinter as tk
import time

# Window Settings
APP_TITLE = 'Personal APP'

# User Settings
USER_CITY = 'Lisbon'

# Colors
COLOR_BACKGROUND = '#1a1a1a'

COLOR_BLACK = '#0000000'
COLOR_WHITE = '#ffffff'
COLOR_LIGHTGREY = '#383838'

# Icon Paths
ICON_WINDOW = '/imgs/icons/code-signs.ico'

# Window Dimensions
def GetWindowWidth(_root):
    return _root.winfo_screenwidth()
def GetWindowHeight(_root):
    return _root.winfo_screenheight()

# Time
def GetCurrentHour():
    return time.strftime('%H:%M:%S')

def GetCurrentDate():
    return time.strftime('%d/%m/%Y')

def GetDateTime():
    return f'[{GetCurrentDate()} {GetCurrentHour()}]'