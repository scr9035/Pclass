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

		extractAction = QtGui.QAction("&Exit", self)
		extractAction.setShortcut("Ctrl+Q")
		extractAction.setStatusTip('Exit the Generator')
		extractAction.triggered.connect(self.close_application)
		
		self.statusBar()

		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu('&File')
		fileMenu.addAction(extractAction)

		self.home()

	def home(self):
		btn = QtGui.QPushButton('Quit', self)
		btn.clicked.connect(self.close_application)
		btn.resize(btn.sizeHint())
		btn.move(100,100)


		extractAction = QtGui.QAction(QtGui.QIcon('qnice.png'), 
									  'Hit it and quit it', self)
		extractAction.triggered.connect(self.close_application)

		self.toolBar = self.addToolBar("Extraction")
		self.toolBar.addAction(extractAction)


		self.show()

	def close_application(self):
		choice = QtGui.QMessageBox.question(self, 'Extract!',
											"Get into the chopper?",
											QtGui.QMessageBox.Yes | 
											QtGui.QMessageBox.No)
		if choice == QtGui.QMessageBox.Yes:
			print("Extracting Now")
			sys.exit()
		else:
			pass


def run():
	app = QtGui.QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())

run()