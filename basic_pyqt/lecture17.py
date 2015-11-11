#!/usr/bin/python2.7
# run as ./lecture17.py
# chmod +x lecture17.py in case its not executable

import sys

from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)
w = QtGui.QWidget()
w.resize(250, 150)
w.move(300, 300)
w.setWindowTitle('Our first gooey!')
w.show()
app.exec_()