import win32api
import win32gui, win32con

def test_pywin32():
    win32api.MessageBox(0,"Hello Pywin32","Messagebox", win32con.MB_OK| win32con.MB_ICONWARNING)