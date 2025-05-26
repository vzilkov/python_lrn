import pyautogui as gui
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
import time

def delay():
    time.sleep(0.1)

def balena():
    print(gui.size())
    app = Application(backend="uia").connect(title_re="Mikro*", timeout=3)  # win32 or uia
    print("Prog started.")
    autom_id = 66678
    btn_name = "Copy To Clipboard"
    
    dlg_main = app.window()
    dlg_main.wait('ready', timeout=10)  # Wait for the window to be ready
    delay()
    dlg_main.set_focus()

    button_to_click = dlg_main.child_window(
        class_name="TJvImgBtn",
        title=btn_name
    )
    button_to_click.click()  # Click the button by name

def notepad():
    print(gui.size())
    app = Application(backend="win32").connect(title_re="a.txt", timeout=10, visible_only=True) # win32 not uid
    print("Notepad started.")
    time.sleep(2)
    # Example: Type some text
    dlg_main = app.top_window()
    delay()
    dlg_main.set_focus()  # Ensure the window is focused  
    delay()
    dlg_main.maximize()   # Make the window full windowed
    delay()
    send_keys('^{END}')
    delay()
    send_keys('{ENTER}')
    send_keys("Hello, this is a test of pyautogui with Notepad!", with_spaces=True)
    delay()
    send_keys('^s')
    delay() 
    dlg_main.minimize()

# notepad()
balena()