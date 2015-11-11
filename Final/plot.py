#!/usr/bin/python2.7
# run as ./lecture17.py
# chmod +x lecture17.py in case its not executable
# use ls -al to see if file has an -x-

import sys, os, random
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtGui, QtCore

import matplotlib
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np

class AppForm(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setWindowTitle("Sign Wavz")
        self.setWindowIcon(QtGui.QIcon('nt_sine.jpg'))
        self.create_main_frame()
        #self.on_draw()

    def on_draw(self):
        amp = 1
        freq = 1
        phase = 0
        # Plot three functions
        t = np.arange(0, 2, .01)
        # Plot some functions and change the range of axes
        self.axes.plot(t, amp*np.sin(t*freq*2*np.pi + phase))
        self.axes.axis([0, 2, -1.5, 1.5])
        # Update canvas by redrawing with current state of figure
        self.canvas.draw()

    def create_main_frame(self):
        self.main_frame = QWidget()
        # Create new figure to put plots on
        self.fig = Figure()
        # Create canvas to draw figure on
        self.canvas = FigureCanvas(self.fig)
        # Canvas is a child on main_frame
        self.canvas.setParent(self.main_frame)
        
        # self.axes now references the first subplot
        self.axes = self.fig.add_subplot(111)
        # Create a matplotlib toolbar for the canvas. Set parent to main_frame
        self.mpl_toolbar = NavigationToolbar(self.canvas, self.main_frame)

        #btn_plotSine = QtGui.QPushButton('Plot Sine Wave', self)
        #btn_plotSine.clicked.connect(self.on_draw)

        btn_clear = QtGui.QPushButton('Clear', self)
        btn_clear.clicked.connect(self.__init__)     

        self.styleChoice = QtGui.QLabel("Amplitude", self)
        #self.styleChoice.move(50,350)

        self.styleChoice = QtGui.QLabel("Frequency", self)
        #self.styleChoice.move(50,450)

        self.styleChoice = QtGui.QLabel("Phase", self)
        #self.styleChoice.move(50,550)

        
        vbox = QVBoxLayout()
        vbox.addWidget(self.canvas)
        vbox.addWidget(self.mpl_toolbar)
        #vbox.addWidget(self.btn_plotSine)
        vbox.addWidget(self.btn_clear)
        self.setCentralWidget(self.main_frame)
        self.main_frame.setLayout(vbox)
        

def run():
    app = QApplication(sys.argv)
    form = AppForm()
    form.show()
    app.exec_()

run()