import os 

def open_file():
    #codepath ="C:/Users/hp/Desktop/Python/Email_Automation_2.py" # for Windows
    codepath = "/home/user/Desktop/Python/fork_bomb.py" # for Linux/Mac
    os.startfile(codepath)

open_file()

#Readme.md for Windows User
''' 
    Install pyinstaller using pip if you haven't already:
    pip install pyinstaller
    To convert the Python script to an executable, use the following command in your terminal or command prompt:
    pyinstaller -F auto_open_file.py
    After running the command, you will find the executable file in the 'dist' directory created by PyInstaller.
    Now open the run and type shell:startup and hit enter. This will open the startup folder.
    Copy the executable file from the 'dist' directory and paste it into the startup folder.
    Now, every time you start your computer, the script will run automatically and open the specified file.
'''

#Readme.md for Linux/Mac User
''' 
    Install pyinstaller using pip if you haven't already:
    pip install pyinstaller
    To convert the Python script to an executable, use the following command in your terminal:
    pyinstaller -F auto_open_file.py
    After running the command, you will find the executable file in the 'dist' directory created by PyInstaller.
    Now, you need to add a script to your startup applications. The method varies depending on your desktop environment.
    For example, on GNOME, you can use 'gnome-session-properties' to add a new startup program.
    Add the path to the executable file from the 'dist' directory as a new startup program.
    Now, every time you start your computer, the script will run automatically and open the specified file.
'''
