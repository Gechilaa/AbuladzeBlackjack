import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout


class Jeirani(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Rock, Paper, Scissors')
        self.setGeometry(100, 100, 300, 200)
        self.result_label = QLabel('Choose Rock, Paper, Or Scissors', self)
        self.Computer_choice_label = QLabel('', self)

        self.Rock_button = QPushButton('Rock')
        self.Paper_button = QPushButton('Paper')
        self.Scissors_button = QPushButton('Scissors')
        self.Reset_button = QPushButton('Reset')

        self.Rock_button.clicked.connect(lambda: self.play('Rock'))
        self.Paper_button.clicked.connect(lambda: self.play('Paper'))
        self.Scissors_button.clicked.connect(lambda: self.play('Scissors'))
        self.Reset_button.clicked.connect(self.reset_game)

        layout = QVBoxLayout()
        layout.addWidget(self.result_label)
        layout.addWidget(self.Computer_choice_label)
        layout.addWidget(self.Rock_button)
        layout.addWidget(self.Paper_button)
        layout.addWidget(self.Scissors_button)
        layout.addWidget(self.Reset_button)
        self.setLayout(layout)

    def play(self, user_choice):
        choices = ['Rock', 'Paper', 'Scissors']
        Computer_choice = random.choice(choices)

        self.Computer_choice_label.setText(f'Computer chose {Computer_choice}')

        if user_choice == Computer_choice:
            result = 'Its a draw!'
        elif (user_choice == 'Rock' and Computer_choice == 'Scissors') or \
                (user_choice == 'Paper' and Computer_choice == 'Rock') or \
                (user_choice == 'Scissors' and Computer_choice == 'Paper'):
            result = 'You won!!!'
        else:
            result = 'You Lose 🙁 '
        self.result_label.setText(result)


    def reset_game(self):
        self.result_label.setText('Choose Rock, Paper, Or Scissors')
        self.Computer_choice_label.setText('')


app = QApplication(sys.argv)
game = Jeirani()
game.show()
sys.exit(app.exec_())