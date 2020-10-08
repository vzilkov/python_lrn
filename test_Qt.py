from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QDialog
import sys
import threading
from time import sleep
from grpc_class import *
import queue

#can_data_queue = queue.Queue()

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('main.ui', self)
        #self.Qt
        self.rcv_data_func_en = True
        self.cnt = 0
        self.pushButton_clear.clicked.connect(self.clear_items_tabletWidget)

    def tx_data_func(self):
        can_data = []
        can_data.append(self.lineEdit_data_0.text())
        '''can_data[1] = self.lineEdit_data_1.text()
        can_data[2] = self.lineEdit_data_2.text()
        can_data[3] = self.lineEdit_data_3.text()
        can_data[4] = self.lineEdit_data_4.text()
        can_data[5] = self.lineEdit_data_5.text()
        can_data[6] = self.lineEdit_data_6.text()
        can_data[7] = self.lineEdit_data_7.text()'''
        ID = self.lineEdit_id.text()
        Len = int(self.comboBox_len.currentText())
        if ID:
            print('***** ID ', (int(ID, 16)))
        if Len:
            print('***** Length ', (int(Len)))

    def clear_items_tabletWidget(self):
        self.tableWidget.clearContents()
        self.cnt = 0
        #while self.tableWidget.rowCount():
            #self.tabletWidget.removeRow(self.tableWidget.rowCount())

    def rcv_data_func(self):
        while self.rcv_data_func_en:
            self.tx_data_func()
            try:
                data_buf = can_data_queue.get(timeout=2)
                if data_buf:
                    row = 0
                    self.tableWidget.insertRow(row)
                    self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem('%X'% data_buf.Id))
                    self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem('%X'% data_buf.Len))

                    count = 0
                    for i in data_buf.Data:
                        self.tableWidget.setItem(row, count+2, QtWidgets.QTableWidgetItem('%X'% i))
                        count += 1

                    self.tableWidget.setItem(row, 10, QtWidgets.QTableWidgetItem('%d'% self.cnt))
                    self.tableWidget.setItem(row, 11, QtWidgets.QTableWidgetItem('RX'))

                    self.tableWidget.resizeColumnsToContents()

                    self.cnt += 1
                    #sleep(0.01)
            except:
                print('Queue timeout occured rcv_data_func')

app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)

class_grpc = grpc_response_stream_rcv()

#mainwindow.tableWidget.setFixedWidth(680)
widget.show()

class_grpc.start_receive_stream()

cons = threading.Thread(target = mainwindow.rcv_data_func)
cons.start()

try:
    #mainwindow.tx_data_func()
    sys.exit(app.exec_())
except:
    print('Exiting')
finally:
    class_grpc.stop_thread()
    mainwindow.rcv_data_func_en = False
    sys.exit(app.exec_())
    print('finally')
