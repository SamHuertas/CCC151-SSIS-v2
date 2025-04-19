from pathlib import Path
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QDialog, QLabel, QPushButton, QApplication


class Ui_DuplicateProgramPopup(object):
    def setupUi(self, DuplicateProgramPopup):
        DuplicateProgramPopup.setObjectName("DuplicateProgramPopup")
        DuplicateProgramPopup.setFixedSize(371, 201)
        DuplicateProgramPopup.setStyleSheet(Path('Styles/DuplicatePopup.qss').read_text())

        self.Text = QLabel(DuplicateProgramPopup)
        self.Text.setObjectName("Text")
        self.Text.setGeometry(QtCore.QRect(50, 20, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Text.setFont(font)
        self.Text.setAutoFillBackground(False)
        self.Text.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.Text.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Text.setWordWrap(True)

        self.Text_2 = QLabel(DuplicateProgramPopup)
        self.Text_2.setObjectName("Text_2")
        self.Text_2.setGeometry(QtCore.QRect(30, 70, 311, 51))
        font1 = QtGui.QFont()
        font1.setFamily("Roboto")
        font1.setPointSize(11)
        self.Text_2.setFont(font1)
        self.Text_2.setAutoFillBackground(False)
        self.Text_2.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.Text_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Text_2.setWordWrap(True)

        self.CloseButton = QPushButton(DuplicateProgramPopup)
        self.CloseButton.setObjectName("CloseButton")
        self.CloseButton.setGeometry(QtCore.QRect(40, 130, 291, 41))
        font2 = QtGui.QFont()
        font2.setFamily("Roboto")
        font2.setPointSize(11)
        font2.setBold(False)
        font2.setWeight(50)
        self.CloseButton.setFont(font2)

        self.retranslateUi(DuplicateProgramPopup)
        QtCore.QMetaObject.connectSlotsByName(DuplicateProgramPopup)

    def retranslateUi(self, DuplicateProgramPopup):
        _translate = QtCore.QCoreApplication.translate
        DuplicateProgramPopup.setWindowTitle(_translate("DuplicateProgramPopup", "Dialog"))
        self.Text.setText(_translate("DuplicateProgramPopup", "Program already Exists"))
        self.Text_2.setText(_translate("DuplicateProgramPopup", "The program code you are trying to add is already in the database."))
        self.CloseButton.setText(_translate("DuplicateProgramPopup", "Close"))

class DuplicateProgramPopup(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DuplicateProgramPopup()
        self.ui.setupUi(self)
        self.setWindowTitle('Program Exists')
        self.setWindowIcon(QIcon('Assets/StudentIcon.png'))

        self.ui.CloseButton.clicked.connect(self.close)

