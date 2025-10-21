import pyautogui
import time
import tkinter as tk

def screenshot():
    time.sleep(0)
    name = f'/home/saran/Pictures/Screenshots/{time.time()}.png'
    img = pyautogui.screenshot()
    img.save(name)
    img.show()

root =tk.Tk()
root.title("Screenshot GUI")


btn = tk.Button(root,text="Take Screenshot",command=screenshot) 
btn.pack(side=tk.LEFT,pady=10,padx=5)

close = tk.Button(root,text="Quit",command=quit)
close.pack(side=tk.LEFT,pady=10,padx=5)

root.mainloop()