from pathlib import Path
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QDialog, QLabel, QPushButton, QApplication


class Ui_DuplicateCollegePopup(object):
    def setupUi(self, DuplicateCollegePopup):
        DuplicateCollegePopup.setObjectName("DuplicateCollegePopup")
        DuplicateCollegePopup.setFixedSize(371, 201)
        DuplicateCollegePopup.setStyleSheet(Path('Styles/DuplicatePopup.qss').read_text())

        self.Text = QLabel(DuplicateCollegePopup)
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

        self.Text_2 = QLabel(DuplicateCollegePopup)
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

        self.CloseButton = QPushButton(DuplicateCollegePopup)
        self.CloseButton.setObjectName("CloseButton")
        self.CloseButton.setGeometry(QtCore.QRect(40, 130, 291, 41))
        font2 = QtGui.QFont()
        font2.setFamily("Roboto")
        font2.setPointSize(11)
        font2.setBold(False)
        font2.setWeight(50)
        self.CloseButton.setFont(font2)

        self.retranslateUi(DuplicateCollegePopup)
        QtCore.QMetaObject.connectSlotsByName(DuplicateCollegePopup)

    def retranslateUi(self, DuplicateCollegePopup):
        _translate = QtCore.QCoreApplication.translate
        DuplicateCollegePopup.setWindowTitle(_translate("DuplicateCollegePopup", "Dialog"))
        self.Text.setText(_translate("DuplicateCollegePopup", "College already Exists"))
        self.Text_2.setText(_translate("DuplicateCollegePopup", "The college code you are trying add is already in the database."))
        self.CloseButton.setText(_translate("DuplicateCollegePopup", "Close"))

class DuplicateCollegePopup(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DuplicateCollegePopup()
        self.ui.setupUi(self)
        self.setWindowTitle('College Exists')
        self.setWindowIcon(QIcon('Assets/StudentIcon.png'))

        self.ui.CloseButton.clicked.connect(self.close)

