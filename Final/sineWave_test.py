#!/usr/bin/python2.7
# run as ./lecture17.py
# chmod +x lecture17.py in case its not executable
# use ls -al to see if file has an -x-

import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):

	def __init__(self):
		super(Window, self).__init__()
		self.setGeometry(500,500,500,500)
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


		makeSinPlot = QtGui.QAction(QtGui.QIcon('qnice.png',
									self)
		makeSinPlot.triggered.connect(self.sine_wave_plot)


		self.show()

	def close_application(self):
		sys.exit()


	def sine_wave_plot(self):
		Xrange = np.arange(0, 10, .1)
		A = 1
		theta = 0
		phi = 0
		sineFun = A*np.sin(Xrange + phi)
		plt.figure()
		plt.plot(Xrange, sineFun)
		#save as png file


def run():
	app = QtGui.QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())

run()