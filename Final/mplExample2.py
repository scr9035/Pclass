#!/usr/bin/python2.7
# run as ./lecture17.py
# chmod +x lecture17.py in case its not executable
# use ls -al to see if file has an -x-

import sys, os, random
from PyQt4 import QtGui, QtCore

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
import matplotlib.pyplot as plt
import numpy as np




class Window(QtGui.QDialog):
    def __init__(self, parent = None):
        super(Window, self).__init__(parent)
        self.setWindowTitle("Sign Wavz")
        self.setWindowIcon(QtGui.QIcon('nt_sine.jpg'))

        # a figure instance to plot on
        self.figure = plt.figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Just some button connected to `plot` method
        self.plotButton = QtGui.QPushButton('Plot')
        self.plotButton.clicked.connect(self.plot)

        # Just some button connected to `clear` method
        self.clearButton = QtGui.QPushButton('Clear')
        self.clearButton.clicked.connect(self.clear)

        self.styleChoiceA = QtGui.QLabel("Amplitude: ", self)
        self.styleChoiceF = QtGui.QLabel("Frequency: ", self)
        self.styleChoiceP = QtGui.QLabel("Phase: ", self)

        self.amplitude = QtGui.QLineEdit()
        self.amplitude.setText('1')
        self.amplitude.textChanged[str].connect(self.amp_variable)

        self.frequency = QtGui.QLineEdit()
        self.frequency.setText('1')
        self.frequency.textChanged[str].connect(self.freq_variable)

        self.phi = QtGui.QLineEdit()
        self.phi.setText('0')
        self.phi.textChanged[str].connect(self.phase_variable)
        

        # set the layout
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.addWidget(self.toolbar)

        layout.addWidget(self.styleChoiceA)
        layout.addWidget(self.amplitude)

        layout.addWidget(self.styleChoiceF)
        layout.addWidget(self.frequency)

        layout.addWidget(self.styleChoiceP)
        layout.addWidget(self.phi)

        layout.addWidget(self.plotButton)
        layout.addWidget(self.clearButton)
        self.setLayout(layout)


    

    def plot(self):

        amp = self.amp_variable()
        freq = self.freq_variable()
        phase = self.phase_variable()
       
        t = np.arange(0, 2, .01)
        # create an axis
        ax = self.figure.add_subplot(111)
        # discards the old graph
        ax.hold(True)
        # plot data
        ax.plot(t, amp*np.sin(t*freq*2*np.pi + phase))
        # refresh canvas
        self.canvas.draw()


    def clear(self):      
        t = np.arange(0, 2, .01)
        # create an axis
        ax = self.figure.add_subplot(111)
       
        ax.hold(False)
        ax.plot(t, t*0, 'r-', alpha=0.000001)
       
        self.canvas.draw()


    def amp_variable(self):
        amp = str(self.amplitude.displayText())

        try:
            amp = float(amp)
        except ValueError:
            amp = 1
        
        return amp

    def freq_variable(self):
        freq = str(self.frequency.displayText())

        try:
            freq = float(freq)
        except ValueError:
            freq = 1
        
        return freq

    def phase_variable(self):
        phase = str(self.phi.displayText())

        try:
            phase = float(phase)
        except ValueError:
            phase = 0
        
        return phase

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    main = Window()
    main.show()

    sys.exit(app.exec_())
