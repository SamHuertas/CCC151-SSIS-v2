from pathlib import Path
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QDialog, QLabel, QPushButton, QApplication


class Ui_DuplicateStudentPopup(object):
    def setupUi(self, DuplicateStudentPopup):
        DuplicateStudentPopup.setObjectName("DuplicateStudentPopup")
        DuplicateStudentPopup.setFixedSize(371, 201)
        DuplicateStudentPopup.setStyleSheet(Path('Styles/DuplicatePopup.qss').read_text())

        self.Text = QLabel(DuplicateStudentPopup)
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

        self.Text_2 = QLabel(DuplicateStudentPopup)
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

        self.CloseButton = QPushButton(DuplicateStudentPopup)
        self.CloseButton.setObjectName("CloseButton")
        self.CloseButton.setGeometry(QtCore.QRect(40, 130, 291, 41))
        font2 = QtGui.QFont()
        font2.setFamily("Roboto")
        font2.setPointSize(11)
        font2.setBold(False)
        font2.setWeight(50)
        self.CloseButton.setFont(font2)

        self.retranslateUi(DuplicateStudentPopup)
        QtCore.QMetaObject.connectSlotsByName(DuplicateStudentPopup)

    def retranslateUi(self, DuplicateStudentPopup):
        _translate = QtCore.QCoreApplication.translate
        DuplicateStudentPopup.setWindowTitle(_translate("DuplicateStudentPopup", "Dialog"))
        self.Text.setText(_translate("DuplicateStudentPopup", "Student already Exists"))
        self.Text_2.setText(_translate("DuplicateStudentPopup", "The students' ID number you are trying add is already in the database."))
        self.CloseButton.setText(_translate("DuplicateStudentPopup", "Close"))

class DuplicateStudentPopup(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DuplicateStudentPopup()
        self.ui.setupUi(self)
        self.setWindowTitle('Student Exists')
        self.setWindowIcon(QIcon('Assets/StudentIcon.png'))

        self.ui.CloseButton.clicked.connect(self.close)

