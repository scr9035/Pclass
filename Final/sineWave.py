#!/usr/bin/python2.7
# run as ./lecture17.py
# chmod +x lecture17.py in case its not executable
# use ls -al to see if file has an -x-

import sys
from PyQt4 import QtGui, QtCore

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setGeometry(150,150,500,300)
window.setWindowTitle("Sign Wavz")
window.show()
app.exec_()