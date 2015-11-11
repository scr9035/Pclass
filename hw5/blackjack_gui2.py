#!/usr/bin/python2.7
# run as ./lecture17.py
# chmod +x lecture17.py in case its not executable
# use ls -al to see if file has an -x-

import sys
from PyQt4 import QtGui, QtCore, Qt
from card_table import *
import stats_db  
#import statsGooey

class BlackjackApp(QtGui.QMainWindow):
    
    def __init__(self):
        super(BlackjackApp, self).__init__()
        self.initUI()        
        
    def initUI(self):
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        self.setToolTip('Play Gooey Blackjack!')

        exitAction = QtGui.QAction('Exit', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(app.quit)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        fileMenu.addAction(exitAction)

        w = self.statsBS
        statsAction = QtGui.QAction('Stats', self)
        statsAction.setShortcut('Ctrl+S')
        statsAction.setStatusTip('See how the dealer always wins')
        statsAction.triggered.connect(w)
    

        gameMenu = menubar.addMenu('Game') 
        gameMenu.addAction(statsAction)

        
        statbar = self.statusBar()

        self.c = CardTable()
        self.setCentralWidget(self.c)

        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('Gooey Blackjack')
        self.show()


    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure?", QtGui.QMessageBox.Yes | 
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:

            if self.c.gamesPlayed > 0:
                stats_db.insert_stat(self.c.player_name, 
                                     self.c.gamesWon, self.c.gamesPlayed) 
            event.accept()
        else:
            event.ignore()      


    def statsBS(self):
        #app = QtGui.QApplication(sys.argv)
        self.widget = QtGui.QWidget()
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

        for i in range(1, 6): # change to 6
            for j in range(4):
                # keep a reference to the buttons
                buttons[(i, j)] = QtGui.QPushButton(str(statsDB[i-1][j]))
                # add to the layout
                layout.addWidget(buttons[(i, j)], i, j)

        self.widget.setWindowTitle('Statistics')
        self.widget.setLayout(layout)
        self.widget.show()
        #sys.exit(app.exec_())


    
app = QtGui.QApplication(sys.argv)
b_app = BlackjackApp()
app.exec_()