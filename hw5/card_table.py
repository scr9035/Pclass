from blackjack import *
from PyQt4 import QtGui, QtCore, Qt

class CardTable(QtGui.QWidget):
    def __init__(self):
        super(CardTable, self).__init__()
        self.game = BlackjackGame()
        self.gamesWon = 0
        self.gamesPlayed = 0
        self.player_labels = []
        self.dealer_labels = []
        self.player_name = ''
        self.initUI()
        self.get_name()

    def initUI(self):
        self.table = QtGui.QWidget()
        hitButton = QtGui.QPushButton("Hit")
        stayButton = QtGui.QPushButton("Stay")
        
        self.games_won_lbl =  QtGui.QLabel("Games Won: " + str(self.gamesWon))
        self.games_played_lbl = QtGui.QLabel("Games Played: " + str(self.gamesPlayed))

        hitButton.clicked.connect(self.hitAction)
        stayButton.clicked.connect(self.stayAction)

        p = self.table.palette()
        p.setColor(self.table.backgroundRole(), Qt.QColor(34, 139, 34, 200))
        self.table.setPalette(p)
        self.table.setAutoFillBackground(True)

        self.grid = QtGui.QGridLayout() 
        self.setLayout(self.grid)
        self.grid.setColumnMinimumWidth(0,5)
        self.grid.setColumnMinimumWidth(7,5)
        
        self.grid.addWidget(self.table, 0, 0, 2, 8)

        
        self.start_new_game()
        self.grid.addWidget(hitButton, 2, 5)
        self.grid.addWidget(stayButton, 2, 6)
        self.grid.addWidget(self.games_played_lbl, 2, 1, 1, 2)
        self.grid.addWidget(self.games_won_lbl, 2, 3, 1, 2)


    def get_name(self):
        text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')
        if ok:
            self.player_name = str(text)

    def start_new_game(self):
        ''' Remove cards from previous game. '''
        for i in self.player_labels:
            i.setParent(None)
        for i in self.dealer_labels:
            i.setParent(None)

        ''' Update labels with game stats '''
        self.games_won_lbl.setText("Games Won: " + str(self.gamesWon))
        self.games_played_lbl.setText("Games Played: " + str(self.gamesPlayed))

        ''' Start a new game and clear card labels '''
        self.game.start_new_game()
        self.dealer_labels = []
        self.player_labels = []

        ''' Display dealer's first card and hide the second. '''
        for d in self.game.dealer_cards:
            self.dealer_labels.append(QtGui.QLabel(None))
            self.dealer_labels[-1].setPixmap(QtGui.QPixmap(d))
            if len(self.dealer_labels) == 2:
                self.hidden_card = QtGui.QLabel(self.table)
                self.hidden_card.setPixmap(QtGui.QPixmap("cards/b2fv.png"))
                self.grid.addWidget(self.hidden_card, 0, 2, 1, 1)
            else:
                self.dealer_labels[-1].setParent(self.table)
                self.grid.addWidget(self.dealer_labels[-1], 0, len(self.dealer_labels), 1, 1)

        ''' Display cards dealt to the player '''
        for p in self.game.player_cards:
            self.player_labels.append(QtGui.QLabel(self.table))
            self.player_labels[-1].setPixmap(QtGui.QPixmap(p))
            self.grid.addWidget(self.player_labels[-1], 1, len(self.player_labels)+4, 1, 1)

    def hitAction(self):
        ''' Execute a hit phase. Create a new label widget
        to place the dealt card on the game table.
        Check to see if gameFlag is not None, indicating
        an automatic end condition was encountered. '''
        gameFlag = self.game.play_game()
        self.player_labels.append(QtGui.QLabel(self.table))
        self.player_labels[-1].setPixmap(QtGui.QPixmap(self.game.player_cards[-1]))
        self.grid.addWidget(self.player_labels[-1], 1, 7-len(self.player_labels), 1, 1)
        if gameFlag == 1 or gameFlag == 0:
            self.reveal_hole_card()
            self.alert_game_end(gameFlag)

    def reveal_hole_card(self):
        ''' Flip over the dealer's hidden card '''
        self.hidden_card.setParent(None)
        self.dealer_labels[1].setParent(self.table)
        self.grid.addWidget(self.dealer_labels[1], 0, 2, 1, 1)

    def stayAction(self):
        ''' Execute a stay phase. Flip over the dealer's hidden
        card and create and attach label widgets for each of the 
        cards dealt to the dealer in the stay phase. '''
        self.reveal_hole_card()
        gameFlag = self.game.stay_game()
        for d in range(2,len(self.game.dealer_cards)):
            self.dealer_labels.append(QtGui.QLabel(self.table))
            self.dealer_labels[-1].setPixmap(QtGui.QPixmap(self.game.dealer_cards[d]))
            self.grid.addWidget(self.dealer_labels[-1], 0, len(self.dealer_labels), 1, 1)
        self.alert_game_end(gameFlag)

    def alert_game_end(self, gameFlag):
        win_message = "YOU WIN! Play again?"
        lose_message = "Dealer wins. Play again?"

        if gameFlag:
            self.gamesWon = self.gamesWon + 1
            msg = win_message
        else:
            msg = lose_message
        self.gamesPlayed = self.gamesPlayed + 1

        reply = QtGui.QMessageBox.question(self, 'Game Over',
            msg, QtGui.QMessageBox.Yes | 
            QtGui.QMessageBox.No, QtGui.QMessageBox.Yes)
        if reply == QtGui.QMessageBox.Yes:
            self.start_new_game()
        else:
            app.quit()