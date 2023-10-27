import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk
from functools import partial

import screeninfo



#window
window = ttk.Window(themename = 'journal')
window.title('Display Resolution Switcher Settings')
window.geometry(f'500x{50+ (150 * len(screeninfo.get_monitors()))}')
window.resizable(0,0)

#title
title_label = tk.Label(master = window, text = 'Settings', font = 'Arial 24 bold')
title_label.pack()

#Monitor Object Class
class monitorInfoBody():
    def __init__(self, array) -> None:
        self.id = 0 #TEMPORARY FIX THIS YOU BAFFOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOON
        self.name = array[6][1].replace('\\', '').replace('.', '').replace("'", '')
        self.width = array[2][1]
        self.height = array[3][1]
        self.newWidth = self.width
        self.newHeight = self.height
        self.widthEntry = None
        self.heightEntry = None

def assignEntries(monitor, widthEntry, heightEntry):
    monitor.widthEntry = widthEntry
    monitor.heightEntry = heightEntry
    return


#Information Aquired Prior To Openning -------------------------------------------------------------------
monitorCount = len(screeninfo.get_monitors())
monInfos = []
tk.Label(master=window, text=f"Number of Connected Monitors: {monitorCount}", font = 'Arial 16 bold').pack()

def startUp():
    print(f"Number of Attatched Monitors: {monitorCount}")
    for id, monitor in enumerate(screeninfo.get_monitors()):
        monitorArray = str(monitor).split("(")[1].split(")")[0].split(",")
        newMonitoryArray = []
        for info in monitorArray:
            newMonitoryArray.append(info.split("="))
        monClass = monitorInfoBody(newMonitoryArray)
        
        monClass.id = id
        monInfos.append(monClass)

    for monitor in monInfos:
        widthEntry = None
        heightEntry = None

        tk.Label(master=window, text=f"{monitor.id} {monitor.name}: {monitor.width}x{monitor.height}", font = 'Arial 10', width=650).pack()
        defaultButton = tk.Button(master=window, text=f"Set Default {monitor.name}", command=partial(buildSettingsFromMon, monitor, True)).pack()

        widthEntry = tk.Entry(master=defaultButton)
        widthEntry.insert(0 ,str(monitor.newWidth))

        widthEntry.pack()

        heightEntry = tk.Entry(master=defaultButton)
        heightEntry.insert(0, str(monitor.newHeight))
        heightEntry.pack()

        enabledButton = tk.Button(master=window, text=f"Set Enabled {monitor.name}", command=partial(buildSettingsFromMon, monitor, False)).pack()

        assignEntries(monitor, widthEntry, heightEntry)



#---------------------------------------------------------------------------------------------------------


def buildSettingsFile(id, width, height, default):
    string = f"nircmd setdisplay monitor:{id} {width} {height} 32 \n"

    monitor = monInfos[id]
    print(monitor.widthEntry.get())
    file = ""

    match default:
        case True:
            file = "DefaultSettings"
        case False:
            file = "EnabledSettings"
            width = monitor.widthEntry.get()
            height = monitor.heightEntry.get()
            

    string = f"nircmd setdisplay monitor:{id} {width} {height} 32 \n"

    current = []
    with open(f"{file}.txt", 'r') as f:
        
        current = f.readlines()
        print(current)
        try:
            current[id] = string
        except:
            for i in range(len(current),id+1):
                current.append("")
            current[id] = string

    with open(f"{file}.txt", 'w') as f:
        #print(current)
        for line in current:
            f.writelines(line)
    return

def buildSettingsFromMon(monitor, default):
    buildSettingsFile(monitor.id, monitor.width, monitor.height, default)
    return



# run
def initProc():
    startUp()
    window.mainloop()

initProc()