import autoit

def test_autoit_notePad():
        autoit.run("notepad.exe")
        autoit.win_wait_active("[CLASS:Notepad]", 3)
        autoit.control_send("[CLASS:Notepad]", "Edit1", "hello world{!}")
        autoit.win_close("[CLASS:Notepad]")
        autoit.control_click("[Class:#32770]", "Button2")

def test_LME():
        autoit.run("C:\Program Files (x86)\Aldon\Aldon LM 6.6\Affiniti.exe")
        autoit.win_wait_active("[CLASS:Notepad]", 3)
        autoit.control_send("[CLASS:Notepad]", "Edit1", "hello world{!}")
        autoit.win_close("[CLASS:Notepad]")
        autoit.control_click("[Class:#32770]", "Button2")