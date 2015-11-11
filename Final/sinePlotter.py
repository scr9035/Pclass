#!/usr/bin/python2.7
# run as ./lecture17.py
# chmod +x lecture17.py in case its not executable
# use ls -al to see if file has an -x-

'''Scott Riggs scr9035. Program plots a
basic sine wave function with in PyQt4 framework'''

import sys
from PyQt4 import QtGui # QtCore

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import (
                                                NavigationToolbar2QTAgg
                                                as NavigationToolbar)
import matplotlib.pyplot as plt
import numpy as np


class Window(QtGui.QDialog):
    '''sets the sine wave plotter gui framework'''
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setWindowTitle("Sign Wavz")
        self.setWindowIcon(QtGui.QIcon('nt_sine.jpg'))

        #creates figure instance to plot on
        self.figure = plt.figure()

        #Creates a Canvas Widget to display `figure`
        #it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        #this is the Navigation widget
        #it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        #button connected to `plot` method
        self.plot_btn = QtGui.QPushButton('Plot')
        self.plot_btn.clicked.connect(self.plot)

        #button connected to `clear` method
        self.clear_btn = QtGui.QPushButton('Clear')
        self.clear_btn.clicked.connect(self.clear)

        self.style_amp = QtGui.QLabel("Amplitude: ", self)
        self.style_freq = QtGui.QLabel("Frequency: ", self)
        self.style_phase = QtGui.QLabel("Phase: ", self)

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

        layout.addWidget(self.style_amp)
        layout.addWidget(self.amplitude)

        layout.addWidget(self.style_freq)
        layout.addWidget(self.frequency)

        layout.addWidget(self.style_phase)
        layout.addWidget(self.phi)
        #layout = QtGui.QHBoxLayout()
        layout.addWidget(self.plot_btn)
        layout.addWidget(self.clear_btn)
        self.setLayout(layout)

    def plot(self):
        '''method that takes in the sine wave variables
        and creates a figure axes'''
        amp = self.amp_variable()
        freq = self.freq_variable()
        phase = self.phase_variable()
        x_axis = np.arange(0, 2, .001)
        # create an axis
        axes = self.figure.add_subplot(111)
        # discards the old graph
        axes.hold(True)
        # plot data
        axes.plot(x_axis, amp*np.sin(x_axis*freq*2*np.pi + phase))
        # refresh canvas
        self.canvas.draw()


    def clear(self):
        '''cheat clear method. plots a line with y=0
        and transparent so it looks clear'''
        x_axis = np.arange(0, 2, .01)
        # create an axis
        axes = self.figure.add_subplot(111)
        axes.hold(False)
        axes.plot(x_axis, x_axis*0, 'r-', alpha=0.000001)
        self.canvas.draw()


    def amp_variable(self):
        '''sets the amplitude variable'''
        amp = str(self.amplitude.displayText())

        try:
            amp = float(amp)
        except ValueError:
            amp = 1
        return amp

    def freq_variable(self):
        '''sets the frequency variable'''
        freq = str(self.frequency.displayText())

        try:
            freq = float(freq)
        except ValueError:
            freq = 1
        return freq

    def phase_variable(self):
        '''sets the phase variable'''
        phase = str(self.phi.displayText())

        try:
            phase = float(phase)
        except ValueError:
            phase = 0
        return phase

if __name__ == '__main__':
    APP = QtGui.QApplication(sys.argv)

    MAIN = Window()
    MAIN.show()
    sys.exit(APP.exec_())
