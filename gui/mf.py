import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QApplication, QTabWidget, QWidget, QMainWindow, QMenuBar, QDialog, QStatusBar


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("mainform.ui", self)
        self.pushButton.clicked.connect(self.createtab)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.currentChanged.connect(self.tabChanged)
        self.tabWidget.tabCloseRequested.connect(self.tabClose)
        self.actionLoad.triggered.connect(self.fileLoad)
        self.actionLoad.setShortcut('Ctrl+O')
        self.actionSave.triggered.connect(self.fileSave)
        self.actionSave.setShortcut('Ctrl+S')
        # self.actionSave.triggered.connect(self.quit)
        # self.actionSave.setShortcut('Ctrl+X')

    # def quit(self):

    def fileSave(self):
        file = QFileDialog.getOpenFileName(self, 'Save file')[0]

    def fileLoad(self):
        file = QFileDialog.getOpenFileName(self, 'Open file')[0]

    def tabChanged(self):
        # tracking current working tab
        print("tab was changed to ", self.tabWidget.currentIndex())

    def tabClose(self, cur):
        # deletes tab
        self.tabWidget.removeTab(cur)

    def createtab(self):
        # creates tab by pushbutton with name from line edit
        name = self.lineEdit_2.text()
        self.tabWidget.addTab(loadUi("Mainwidget.ui"), name)

# class StatusBar(QStatusBar):
#     def __init__(self):
#         super(StatusBar, self).__init__()
#         while True:
#             self.statusBar.ShowMessage(self.message)
# class Dialog(QDialog):
#     def __init__(self):
#         super(Dialog, self).__init__()
#         loadUi("tab.ui", self)
#         self.buttonBox.Ok.connect(self.accepted)
#         self.name = ''
#
#     def accepted(self):
#         self.name = str(QDialog.QLabel.text(self))

app = QApplication(sys.argv)
mainwindow = MainWindow()
# mainwindow.setGeometry(0, 0, 804, 601)
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")