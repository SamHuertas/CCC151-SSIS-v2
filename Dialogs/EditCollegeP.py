from pathlib import Path
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QDialog, QLabel, QPushButton
from Dialogs.DuplicateCollegeP import DuplicateCollegePopup
from Dialogs.InputError import InputErrorPopup
from Database.Database import DatabaseConnection

class Ui_EditCollegePopup(object):
    def setupUi(self, EditCollegePopup):
        EditCollegePopup.setObjectName("EditCollegePopup")
        EditCollegePopup.setFixedSize(381, 181)
        EditCollegePopup.setStyleSheet(Path('Styles/EditPopup.qss').read_text())
        
        self.EditCollege = QtWidgets.QFrame(EditCollegePopup)
        self.EditCollege.setGeometry(QtCore.QRect(10, 10, 361, 161))
        self.EditCollege.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.EditCollege.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        
        self.UpdateCollegeButton = QtWidgets.QPushButton(self.EditCollege)
        self.UpdateCollegeButton.setGeometry(QtCore.QRect(10, 110, 341, 41))
        font = QtGui.QFont("Roboto", 14)
        self.UpdateCollegeButton.setFont(font)
        self.UpdateCollegeButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.UpdateCollegeButton.setText("Update College")
        
        self.CCodeTB = QtWidgets.QLineEdit(self.EditCollege)
        self.CCodeTB.setGeometry(QtCore.QRect(150, 40, 191, 21))
        font1 = QtGui.QFont("Roboto", 10)
        self.CCodeTB.setFont(font1)
        self.CCodeTB.setPlaceholderText("ex. CCS")
        
        self.CNameText = QtWidgets.QLabel(self.EditCollege)
        self.CNameText.setGeometry(QtCore.QRect(30, 70, 111, 21))
        font2 = QtGui.QFont("Roboto", 12)
        self.CNameText.setFont(font2)
        self.CNameText.setText("College Name")
        
        self.CNameTB = QtWidgets.QLineEdit(self.EditCollege)
        self.CNameTB.setGeometry(QtCore.QRect(150, 70, 191, 21))
        self.CNameTB.setFont(font1)
        self.CNameTB.setPlaceholderText("ex. College of Computer Studies")
        
        self.CCodeText = QtWidgets.QLabel(self.EditCollege)
        self.CCodeText.setGeometry(QtCore.QRect(30, 40, 111, 21))
        self.CCodeText.setFont(font2)
        self.CCodeText.setText("Code")
        
        self.EditCollegeText = QtWidgets.QLabel(self.EditCollege)
        self.EditCollegeText.setGeometry(QtCore.QRect(10, 10, 151, 21))
        font3 = QtGui.QFont("Roboto", 12, QtGui.QFont.Weight.Bold)
        self.EditCollegeText.setFont(font3)
        self.EditCollegeText.setText("Edit College")
        self.retranslateUi(EditCollegePopup)
        QtCore.QMetaObject.connectSlotsByName(EditCollegePopup)

    def retranslateUi(self, EditCollegeWindow):
        _translate = QtCore.QCoreApplication.translate
        EditCollegeWindow.setWindowTitle(_translate("EditCollegeWindow", "Edit College"))
        self.UpdateCollegeButton.setText(_translate("EditCollegeWindow", "Update College"))
        self.CCodeTB.setPlaceholderText(_translate("EditCollegeWindow", "ex. CCS"))
        self.CNameText.setText(_translate("EditCollegeWindow", "College Name"))
        self.CNameTB.setPlaceholderText(_translate("EditCollegeWindow", "ex. College of Computer Studies"))
        self.CCodeText.setText(_translate("EditCollegeWindow", "Code"))
        self.EditCollegeText.setText(_translate("EditCollegeWindow", "Edit College"))

# Main Window Class
class EditCollegePopup(QDialog):
    def __init__(self, main_window, selected_row):
        super().__init__()
        self.ui = Ui_EditCollegePopup()
        self.ui.setupUi(self)
        self.setWindowTitle("Edit College")
        self.setWindowIcon(QIcon('Assets/StudentIcon.png'))
        self.main_window = main_window  
        self.selected_row = selected_row
        self.ui.UpdateCollegeButton.clicked.connect(self.updateCollege)
        self.current_college_code = self.main_window.ui.CollegeTable.item(selected_row, 0).text()

    def updateCollege(self):
        new_college_code = self.ui.CCodeTB.text().strip().upper()
        new_college_name = self.ui.CNameTB.text().strip().title()

        if not new_college_code or not new_college_name :
            input_error = InputErrorPopup()
            input_error.setModal(True)
            input_error.exec()
            return

        db = DatabaseConnection()
        connection = db.get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT college_code FROM college WHERE college_code = %s AND college_code != %s ", (new_college_code, self.current_college_code))
        if cursor.fetchone() is not None:
            self.duplicate_popup = DuplicateCollegePopup()
            self.duplicate_popup.setModal(True)
            self.duplicate_popup.show()
            return

        cursor.execute("""
                UPDATE college 
                SET college_code = %s, 
                    college_name = %s 
                WHERE college_code = %s
            """, (new_college_code, new_college_name, self.current_college_code))
        connection.commit()

        self.main_window.openProgramCSV() 
        self.main_window.openCollegeCSV() 
        self.close()
