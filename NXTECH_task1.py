import pyautogui
import tkinter as tk
from tkinter.filedialog import *
import time

# create the tkinter window 
root = tk.Tk()
canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.pack()


# Define a function to capture screen and save the image
def takeScreenshot():
    # Hiding the tk window while taking the screeshot
    root.withdraw()
    time.sleep(1.0)
    # Capture the screen
    myscreenshot = pyautogui.screenshot()
    # Save the screenshot with a specific name 
    save_path = asksaveasfilename()
    # Save the captures file
    myscreenshot.save(save_path + "_screenshot.png")
    print("Screenshot saved")



# create a button 
mybutton = tk.Button(text="Take a screenshot",command=takeScreenshot,font=10)
canvas1.create_window(150,150,window=mybutton)



# Run the mainloop
tk.mainloop()