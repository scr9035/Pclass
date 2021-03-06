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

		checkBox = QtGui.QCheckBox('Enlarge Window', self)
		checkBox.move(100,25)
		checkBox.stateChanged.connect(self.enlarge_window)

		self.progress = QtGui.QProgressBar(self)
		self.progress.setGeometry(200,8,250,20)

		self.btn = QtGui.QPushButton("Download",self)
		self.btn.move(200,120)
		self.btn.clicked.connect(self.download)

		print(self.style().objectName())
		self.styleChoice = QtGui.QLabel("Linux", self)

		comboBox = QtGui.QComboBox(self)
		comboBox.addItem("motif")
		comboBox.addItem("Linux")
		comboBox.addItem("cde")
		comboBox.addItem("Plastique")
		comboBox.addItem("Cleanlooks")
		comboBox.addItem("windowsvista")

		comboBox.move(50,250)
		self.styleChoice.move(50,150)
		comboBox.activated[str].connect(self.style_choice)


		self.show()


	def style_choice(self):
		self.styleChoice.setText(text)
		QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))

	def download(self):
		self.completed = 0

		while self.completed < 100:
			self.completed += 0.0001
			self.progress.setValue(self.completed)

	def enlarge_window(self, state):
		if state == QtCore.Qt.Checked:
			self.setGeometry(50,50,1000,600)
		else:
			self.setGeometry(150,150,500,300)




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