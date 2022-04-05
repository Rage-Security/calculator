
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWebEngineWidgets import QWebEngineView

import os, signal
import time

class Browser(QWebEngineView,QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

 
        self._timer = QtCore.QTimer()
        self.setFixedSize(301, 591)

        

    def contextMenuEvent(self, event):

        menu = QMenu(self)
        quitAction = menu.addAction("Quit")
        action = menu.exec_(self.mapToGlobal(event.pos()))
        if action == quitAction:
            qApp.quit()

    def closeEvent(self, *args, **kwargs):
        super(QtWidgets.QMainWindow, self).closeEvent(*args, **kwargs)
        
        def process():
            name = 'rageworker'
            try:
                         
                for line in os.popen("ps ax | grep " + name + " | grep -v grep"):
                    fields = line.split() 
                    pid = fields[0]                  
                    time.sleep(0.2)
                    os.kill(int(pid), signal.SIGKILL)
                print("Process Successfully terminated")
                
            except:
                print("Error Encountered while running script")

        process()


with open('lp','r') as lpf:
    lp = lpf.read()

app = QtWidgets.QApplication(sys.argv)
b = Browser()

b.load(QtCore.QUrl(f'http://127.0.0.1:{lp}'))
b.show()
app.exec_()

