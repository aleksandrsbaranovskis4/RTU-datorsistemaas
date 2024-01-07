from pywinauto.application import Application
app = Application(backend="uia").start(r"calc.exe").connect(title="Kalkulators", timeout=10)

prg = app.window(title="Kalkulators")
prg.print_control_identifiers()

#print("Ā")