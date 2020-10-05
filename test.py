from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QDialog
import sys

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi('main.ui', self)
        
    def loaddata(self):
        self.tableWidget.resizeColumnsToContents()
        from random import randrange
        for i in range(0, 100, 1):
            row = mainwindow.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem('%X'% randrange(0x200)))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem('%X'% randrange(255)))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem('%X'% randrange(255)))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem('%X'% randrange(255)))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem('%X'% randrange(255)))
            self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem('%X'% randrange(255)))
            self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem('%X'% randrange(255)))
            self.tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem('%X'% randrange(255)))
            self.tableWidget.setItem(row, 8, QtWidgets.QTableWidgetItem('%X'% randrange(255)))
            self.tableWidget.setItem(row, 9, QtWidgets.QTableWidgetItem('%X'% randrange(255)))
            self.tableWidget.setItem(row, 10, QtWidgets.QTableWidgetItem('%X'% row))


app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)

#for i in range(0,10, 1):
#    mainwindow.tableWidget.setColumnWidth(i,75)
mainwindow.tableWidget.setFixedWidth(680)
mainwindow.loaddata()
    
widget.show()
try:
    sys.exit(app.exec_())
except:
    print('Exiting')
'''
class Ui(QtWidgets.QDialog, form):
    def __init__(self):
        super(Ui, self).__init__()
        self.setupUi(self)
        self.button1.clicked.connect(self.print_btn_pressed)
    
    def print_btn_pressed(self):
        if(self.checkBox.checkState()):
            self.rcv_can_msgs.append("ChkBtn true\n")
        else:
            #cursor = self.textCursor()
            #cursor.insertText('Cursor enters text')
            #cursor.movePosition(QtGui)
            #print('Anchor position %d'%self.rcv_can_msgs.setTextCursor(0))
            self.rcv_can_msgs.insertPlainText("ChkBtn false\n")

    def checkBox_pressed(self, txt):
        print('%s' % txt)

app = QtWidgets.QApplication([])
main_window = Ui()
main_window.show()
sys.exit(app.exec())'''