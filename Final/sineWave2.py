#!/usr/bin/python2.7
# run as ./lecture17.py
# chmod +x lecture17.py in case its not executable
# use ls -al to see if file has an -x-

import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):

	def __init__(self):
		super(Window, self).__init__()
		self.setGeometry(150,150,500,300)
		self.setWindowTitle("Sign Wavz")
		self.setWindowIcon(QtGui.QIcon('nt_sine.jpg'))
		self.show()

app = QtGui.QApplication(sys.argv)
GUI = Window()
sys.exit(app.exec_())