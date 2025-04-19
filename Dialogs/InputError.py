from pathlib import Path
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QDialog, QLabel, QPushButton

class Ui_InputError(object):
    def setupUi(self, InputError):
        InputError.setObjectName("InputError")
        InputError.setFixedSize(251, 101)
        InputError.setStyleSheet(Path('Styles/EditPopup.qss').read_text())

        self.Confirmation_2 = QtWidgets.QLabel(parent=InputError)
        self.Confirmation_2.setObjectName("Confirmation_2")
        self.Confirmation_2.setGeometry(QtCore.QRect(10, 0, 231, 51))
        font = QtGui.QFont("Roboto", 11)
        self.Confirmation_2.setFont(font)
        self.Confirmation_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Confirmation_2.setWordWrap(True)
        
        self.ConfirmButton = QtWidgets.QPushButton(parent=InputError)
        self.ConfirmButton.setObjectName("ConfirmButton")
        self.ConfirmButton.setGeometry(QtCore.QRect(30, 60, 191, 31))
        font1 = QtGui.QFont("Roboto", 14)
        self.ConfirmButton.setFont(font1)
        self.ConfirmButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))

        self.retranslateUi(InputError)
        QtCore.QMetaObject.connectSlotsByName(InputError)

    def retranslateUi(self, InputError):
        InputError.setWindowTitle("Input Error")
        self.Confirmation_2.setText("All text fields must be filled out.")
        self.ConfirmButton.setText("Confirm")

class InputErrorPopup(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_InputError()
        self.ui.setupUi(self)
        self.setWindowTitle("Input Error")
        self.setWindowIcon(QIcon('Assets/StudentIcon.png'))
        self.ui.ConfirmButton.clicked.connect(self.close)
