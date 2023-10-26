import os
import keyboard
import time
import threading


import pystray
from PIL import Image

showStatus = False

#Swticthing Mode
def switch(status=False):
    #False is default 1920x1080, 1 is 2560x1440
    fileLocation = os.getcwd()
    with open(fileLocation + "\status.txt") as f:
        if (not status):
            try:
                read = f.read()
                status = bool(int(read))
            except:
                status = True
                return
        
        

        if (status):
            os.system("nircmd setdisplay monitor:0 1920 1080 32 144") #Monitor id, width, height, colour depth, refresh rate
            status = False
        else:
            os.system("nircmd setdisplay monitor:0 2560 1440 32 144")
            status = True
            
        
        

    with open(fileLocation + "\status.txt", "w") as f:
        print(str(int(status)))
        f.write(str(int(status)))
        global showStatus
        showStatus = status
        


def after_click(icon, query):
    if str(query) == "Exit":
        switch(True)
        icon.stop()
    if str(query) == "Enabled?":
        switch()
        
        
        
#Tray Icon
image = Image.open("icon.ico")
tray = pystray.Icon("DSW", image, "Display Switcher", menu=pystray.Menu(pystray.MenuItem("Enabled?", after_click, checked=lambda MenuItem: showStatus),
                                                                        pystray.MenuItem("Exit", after_click)) )

trayThread = threading.Thread(target=tray.run)
trayThread.start()

while True:
    time.sleep(0.1)
    if(not trayThread.is_alive()):
        quit()
    if(keyboard.is_pressed("ctrl") and keyboard.is_pressed("shift") and keyboard.is_pressed("p")):
        print("Switching")
        switch()
        tray.update_menu()
        time.sleep(5)


    