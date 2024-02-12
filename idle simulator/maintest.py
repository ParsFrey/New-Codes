from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from subprocess import Popen, PIPE
import main1

Form, Window = uic.loadUiType("main.ui")
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)

def f5():
    r = open(main1)

def fun():
    f = open("data.txt", "w")
    print("save shod!")
    t = form.textEdit.toPlainText()
    f.write(t)
    f.close()


process = Popen(['python','data.py'],stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()
print(stdout)

form.save_button.clicked.connect(fun)
form.F5simulator.clicked.connect(f5)


window.show()
app.exec()
