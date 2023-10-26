import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk

import screeninfo



#window
window = ttk.Window(themename = 'journal')
window.title('Display Resolution Switcher Settings')
window.geometry('900x250')
window.resizable(0,0)

#title
title_label = tk.Label(master = window, text = 'Settings', font = 'Arial 24 bold')
title_label.pack()

#Information Aquired Prior To Openning
monitorCount = len(screeninfo.get_monitors())
monInfos = []
tk.Label(master=window, text=f"Number of Connected Monitors: {monitorCount}", font = 'Arial 16 bold').pack()

for monitor in screeninfo.get_monitors():
    tk.Label(master=window, text=f" {monitor}", font = 'Arial 10', width=650).pack()


#logic
def settingsLogic():

    print(f"Number of Attatched Monitors: {monitorCount}")
    for monitor in screeninfo.get_monitors():
        monitorArray = str(monitor).split("(")[1].split(")")[0].split(",")
        newMonitoryArray = []
        for info in monitorArray:
            newMonitoryArray.append(info.split("="))
        monInfos.append(newMonitoryArray)

    print(monInfos)











# run
window.after(200, settingsLogic)
window.mainloop()

