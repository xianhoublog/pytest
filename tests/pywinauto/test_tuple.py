from __future__ import print_function
from pywinauto.application import Application
import sys, os
import pywinauto
from pywinauto import Desktop
import time

def test_notepad():

        app = Application(backend="uia").start("notepad.exe")
        app.UntitledNotepad.type_keys("%FX")

        app.UntitledNotepad.menu_select("File->SaveAs")
        app.SaveAs.ComboBox5.select("UTF-8")
        app.SaveAs.edit1.set_text("Example-utf8.txt")
        app.SaveAs.Save.click()

        app.Open.Open.click()  # opening large file
        app.Open.wait_not('visible')  # make sure "Open" dialog became invisible
        # wait for up to 30 seconds until data.txt is loaded
        app.window(title='data.txt - Notepad').wait('ready', timeout=30)

def test_calculator():
        app = Application(backend="uia").start('notepad.exe')
        dlg_spec=app.window(title='Untitled - Notepad')
        print(dlg_spec)

        print("tests passed")
        print(dlg_spec.wrapper_object())
        print(dlg_spec.wrapper_object().minimize())  # while debugging
        app.window(title_re='.* - Notepad$').window(class_name='Edit')

def test_install_7zip():
        """
        Install script for 7zip 9.20 (64-bit)
        Requirements:
          - Win7 or Win8.1 x64, 64-bit Python
          - pywinauto 0.5.2+
          - 7z920-x64.msi is in the same folder as the script
          - UAC is fully disabled
        """

        os.chdir(os.path.join(os.getcwd(), os.path.dirname(sys.argv[0])))


        # app = pywinauto.Application().start('7z1806-x64.msi')
        app = Application().Start(
                cmd_line=u'"C:\\Users\\nduan\\Downloads\\7z1806-x64.msi" \\i "C:\\Users\\nduan\\Downloads\\7z1806-x64.msi" ')
        # app = Application(backend="uia").start('7z1806-x64.msi')
        Wizard = app['Windows Installer']
        Wizard.OK.click()


        Wizard = app['7-Zip 9.20 (x64 edition) Setup']
        Wizard.NextButton.click()

        Wizard['I &accept the terms in the License Agreement'].wait('enabled').check_by_click()
        Wizard.NextButton.click()

        Wizard['Custom Setup'].wait('enabled')
        Wizard.NextButton.click()

        Wizard.Install.click()

        Wizard.Finish.wait('enabled', timeout=30)
        Wizard.Finish.click()
        Wizard.wait_not('visible')

        # final check
        if os.path.exists(r"C:\Program Files\7-Zip\7zFM.exe"):
                print('OK')
        else:
                print('FAIL')

def test_calulator():


        app = Application(backend="uia").start('C:\\Program Files (x86)\\Aldon\\Aldon LM 6.6\\Affiniti.exe')

        dlg = Desktop(backend="uia").Calculator
        dlg.type_keys('2*3=')
        dlg.print_control_identifiers()

        dlg.minimize()
        Desktop(backend="uia").window(title='Calculator', visible_only=False).restore()

def test_LME():
        app = Application().Start(cmd_line=u'"C:\\Program Files (x86)\\Aldon\\Aldon LM 6.6\\Affiniti.exe" ')
        window = app['User Signon']
        time.sleep(5)
        window.Wait('ready')
        window['User Name:Edit'].Restore()
        window.PrintControlIdentifiers()
        # window['User Name:Edit'].type_keys('nduan')
        window['Password:Edit'].type_keys('R0cket777777')
        window.OK.click()
        Parts = app['Parts']

        time.sleep(5)
        Parts.PrintControlIdentifiers()

        # window = app.Dialog
        # window.Wait('ready')
        # app.Dialog.print_control_identifiers()
        # window.Properties.print_control_identifiers()
        # edit = window.Edit
        # edit.ClickInput('nduan')
        # edit2 = window.Edit()
        # edit2.ClickInput('R0cket777777')
        # window.Properties.OK.click()
        # # button = window.OK
        # # button.Click()
        # afxc = app.Parts
        # afxc.SetFocus()

