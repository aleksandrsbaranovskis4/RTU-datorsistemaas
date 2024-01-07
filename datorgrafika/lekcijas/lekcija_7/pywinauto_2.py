from pywinauto.application import Application
import time

app = Application(backend="uia").start(r"C:\Users\baran\AppData\Roaming\Zoom\bin\Zoom.exe").connect(title="Zoom")
time.sleep(1)
prg = app.window(title="Zoom")
time.sleep(1)

prg.print_control_identifiers