from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *  #Пітключення модулів 

def wrong_answer():
    lose = QMessageBox()
    lose.resize(150,90)
    lose.setText("Ти не програв" + "😎😋😊")
    lose.exec_()

def right_answer():
    win = QMessageBox()
    win.setText("Ти не виграв ")     
    win.resize(150,90)
    win.exec_()



app = QApplication([]) # обєкт 

main_win =QWidget() # додаток 
main_win.resize(400,200)
main_win.setWindowTitle("Кoнкурс від Crazy People")

btn1 = QRadioButton('та')
btn2 = QRadioButton('ешкере')
btn3 = QRadioButton('канешна')
btn4 = QRadioButton('шкібіді')
question = QLabel("квас з АТБ імба" )

layoutH1 =QHBoxLayout()
layoutH2 =QHBoxLayout()
layoutH3 =QHBoxLayout()

layoutH1.addWidget(question,alignment= Qt.AlignCenter)
layoutH2.addWidget(btn1,alignment= Qt.AlignCenter)
layoutH2.addWidget(btn2,alignment= Qt.AlignCenter)
layoutH3.addWidget(btn3,alignment= Qt.AlignCenter)
layoutH3.addWidget(btn4,alignment= Qt.AlignCenter)


layoutV1 = QVBoxLayout()

layoutV1.addLayout(layoutH1)
layoutV1.addLayout(layoutH2)
layoutV1.addLayout(layoutH3)

main_win.setLayout(layoutV1)

btn1.clicked.connect(right_answer)
btn2.clicked.connect(wrong_answer)
btn3.clicked.connect(right_answer)
btn4.clicked.connect(right_answer)

main_win.show()
app.exec_()


