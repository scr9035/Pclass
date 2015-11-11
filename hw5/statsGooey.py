#!/usr/bin/python2.7
# run as ./lecture17.py
# chmod +x lecture17.py in case its not executable
# use ls -al to see if file has an -x-

import sys
from PyQt4 import QtGui
import stats_db

app = QtGui.QApplication(sys.argv)
widget = QtGui.QWidget()
layout = QtGui.QGridLayout()

statsDB = stats_db.top_percent()

buttons = {}

buttons[(0, 0)] = QtGui.QPushButton('Name')
buttons[(0, 1)] = QtGui.QPushButton('Won')
buttons[(0, 2)] = QtGui.QPushButton('Played')
buttons[(0, 3)] = QtGui.QPushButton('Percentage')

layout.addWidget(buttons[(0, 0)], 0, 0)
layout.addWidget(buttons[(0, 1)], 0, 1)
layout.addWidget(buttons[(0, 2)], 0, 2)
layout.addWidget(buttons[(0, 3)], 0, 3)

for i in range(1, 4): # change to 6
    for j in range(4):
        # keep a reference to the buttons
        buttons[(i, j)] = QtGui.QPushButton(str(statsDB[i-1][j]))
        # add to the layout
        layout.addWidget(buttons[(i, j)], i, j)

widget.setWindowTitle('Statistics')
widget.setLayout(layout)
widget.show()
sys.exit(app.exec_())
