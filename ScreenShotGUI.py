import pyautogui
import time

def screenshot():
    time.sleep(3)
    img = pyautogui.screenshot()
    img.save("screenshot.png")
    img.show()

screenshot()