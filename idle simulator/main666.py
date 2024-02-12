from PyQt6 import QtCore, QtGui, QtWidgets
from subprocess import Popen, PIPE

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(857, 638)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.F5simulator = QtWidgets.QPushButton(parent=self.centralwidget, clicked = lambda: self.press_it())
        self.F5simulator.setGeometry(QtCore.QRect(380, 440, 91, 61))
        self.F5simulator.setStyleSheet("background-color: rgb(186, 186, 186);\n"
"font: 18pt \"MS Shell Dlg 2\";")
        self.F5simulator.setObjectName("F5simulator")
        self.Result = QtWidgets.QLabel(parent=self.centralwidget)
        self.Result.setGeometry(QtCore.QRect(450, 30, 361, 361))
        self.Result.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Result.setObjectName("Result")
        self.save_button = QtWidgets.QPushButton(parent=self.centralwidget, clicked = lambda: self.fun())
        self.save_button.setGeometry(QtCore.QRect(50, 480, 161, 41))
        self.save_button.setStyleSheet("background-color: rgb(154, 154, 154);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.save_button.setObjectName("save_button")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)#, clicked = lambda: self.write_it())
        self.lineEdit.setGeometry(QtCore.QRect(40, 30, 361, 361))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 857, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        


    def press_it(self):
        self.Result.setText("استاد من هرکاري کردم نتوتستم ازش ايدل در بيارم اين نهايت تلاشمونه")

    #def write_it(self):
        #self.The_Code.setText()

    def fun():
        f = open("data.txt", "w")
        print("save shod!")
        t = form.textEdit.toPlainText()
        f.write(t)
        f.close()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.F5simulator.setText(_translate("MainWindow", "F5"))
        self.Result.setText(_translate("MainWindow", "you can see the code here. (after pressing the F5)"))
        self.save_button.setText(_translate("MainWindow", "SAVE"))
        self.lineEdit.setText(_translate("MainWindow", "write your code here."))

process = Popen(['python','data.py'],stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()
print(stdout)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
