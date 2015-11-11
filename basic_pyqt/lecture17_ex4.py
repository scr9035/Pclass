#!/usr/bin/python2.7
# run as ./lecture17.py
# chmod +x lecture17.py in case its not executable
# use ls -al to see if file has an -x-

import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QMainWindow):
	def __init__(self):
		super(Example, self).__init__()
		self.initUI()

	def initUI(self):
		QtGui.QToolTip.setFont(QtGui.QFont('SansSerif',10))
		self.setToolTip('This window is for our gooey')

		btn = QtGui.QPushButton('Click me until I like it', self)
		btn.resize(btn.sizeHint())
		btn.move(50,50)

		qbtn = QtGui.QPushButton('or just tease and leave me', self)
		qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
		qbtn.resize(qbtn.sizeHint())
		qbtn.move(100,100)

		exitAction = QtGui.QAction('Exit', self)
		exitAction.setShortcut('Ctrl+Q')
		exitAction.setStatusTip('Exit application')
		exitAction.triggered.connect(QtGui.qApp.quit)

		menubar = self.menuBar()
		fileMenu = menubar.addMenu('File')
		fileMenu.addAction(exitAction)

		self.setGeometry(300,300,250,150)
		self.setWindowTitle('Our first gooey')
		self.show()

	def closeEvent(self, event):
		reply = QtGui.QMessageBox.question(self, 'Message', 'Are you sure?',
				QtGui.QMessageBox.Yes|QtGui.QMessageBox.No,
				QtGui.QMessageBox.No)
		if reply == QtGui.QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()


app = QtGui.QApplication(sys.argv)
ex = Example()
app.exec_()


