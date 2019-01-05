# from pywinauto import application
# import time
#
# app = application.Application()
# app.start("Notepad.exe")
# time.sleep(4)
# app.Notepad.edit.TypeKeys("Hello World")
#
# app.Notepad.MenuSelect("File->SaveAs")
# app.SaveAs.edit.SetText("pywinautodemo.txt")
# app.SaveAs.Save.Click()
from pywinauto.application import Application

app = Application().Start(cmd_line=u'"C:\\WINDOWS\\system32\\notepad.exe" ')
notepad = app.Notepad
notepad.Wait('ready')
notepad.ClickInput("123")

menu_item2 = notepad.MenuItem(u'&File->Save &As...')
menu_item2.Select()

# app.Kill_()