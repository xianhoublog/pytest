import jpype

startJVM(r'C:\Program Files\Java\jre1.8.0_73\bin\server\jvm.dll', '-ea', r'-Djava.class.path=D:\02_Devtools\03_sikuli\sikulixapi.jar')
app = JClass('org.sikuli.script.App')
Screen = JClass('org.sikuli.script.Screen')
screen = Screen()
screen.doubleClick('1.png')