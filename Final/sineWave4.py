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

		extractAction = QtGui.QAction("&Get to the choppa")
		extractAction.setShortcut("Ctrl+Q")
		extractAction.setStatusTip('Exit the Generator')
		self.statusBar()

		self.home()

	def home(self):
		btn = QtGui.QPushButton('Quit', self)
		btn.clicked.connect(self.close_application)
		btn.resize(btn.sizeHint())
		btn.move(100,100)
		self.show()

	def close_application(self):
		sys.exit()


def run():
	app = QtGui.QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())

run()