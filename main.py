import sys
sys.dont_write_bytecode = True
from Database.Database import DatabaseConnection
from Dialogs.EditStudentP import EditStudentPopup
from Dialogs.EditProgramP import EditProgramPopup
from Dialogs.EditCollegeP import EditCollegePopup
from Dialogs.DuplicateStudentP import DuplicateStudentPopup
from Dialogs.DuplicateProgramP import DuplicateProgramPopup
from Dialogs.DuplicateCollegeP import DuplicateCollegePopup
from Dialogs.DeleteStudentP import DeleteStudentPopup
from Dialogs.DeleteProgramP import DeleteProgramPopup
from Dialogs.DeleteCollegeP import DeleteCollegePopup
from pathlib import Path
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon, QColor, QRegularExpressionValidator, QFont, QFontDatabase, QPalette
from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect, QHeaderView
from PyQt6.QtCore import QRegularExpression
import mysql.connector


class Ui_MainPage(object):
    def setupUi(self, MainPage):
        MainPage.setObjectName("MainPage")
        MainPage.setFixedSize(1491, 751)
        font = QtGui.QFont()
        font.setPointSize(8)
        MainPage.setFont(font)
        MainPage.setStyleSheet(Path('Styles/MainStyle.qss').read_text())     

        ##-------------------------------------START OF ADD STUDENT PANEL-------------------------------------
        self.AddStudent = QtWidgets.QFrame(parent=MainPage)
        self.AddStudent.setGeometry(QtCore.QRect(1050, 70, 411, 271))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.AddStudent.setFont(font)
        self.AddStudent.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.AddStudent.setObjectName("AddStudent")
        self.AddStudent.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=15, color=QColor("#96b2c9")))       
        self.AddStudentText = QtWidgets.QLabel(parent=self.AddStudent)
        self.AddStudentText.setGeometry(QtCore.QRect(10, 10, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.AddStudentText.setFont(font)
        self.AddStudentText.setObjectName("AddStudentText")
        self.IDText = QtWidgets.QLabel(parent=self.AddStudent)
        self.IDText.setGeometry(QtCore.QRect(30, 40, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.IDText.setFont(font)
        self.IDText.setObjectName("IDText")
        self.FNameText = QtWidgets.QLabel(parent=self.AddStudent)
        self.FNameText.setGeometry(QtCore.QRect(30, 70, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.FNameText.setFont(font)
        self.FNameText.setObjectName("FNameText")
        self.LNameText = QtWidgets.QLabel(parent=self.AddStudent)
        self.LNameText.setGeometry(QtCore.QRect(30, 100, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.LNameText.setFont(font)
        self.LNameText.setObjectName("LNameText")
        self.YLevelText = QtWidgets.QLabel(parent=self.AddStudent)
        self.YLevelText.setGeometry(QtCore.QRect(30, 160, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.YLevelText.setFont(font)
        self.YLevelText.setObjectName("YLevelText")
        self.IDTB = QtWidgets.QLineEdit(parent=self.AddStudent)
        self.IDTB.setGeometry(QtCore.QRect(150, 40, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.IDTB.setFont(font)
        self.IDTB.setObjectName("IDTB")
        self.GenderDD = QtWidgets.QComboBox(parent=self.AddStudent)
        self.GenderDD.setGeometry(QtCore.QRect(150, 130, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.GenderDD.setFont(font)
        self.GenderDD.setObjectName("GenderDD")
        self.GenderDD.addItems(["","Male", "Female"])
        self.GenderText = QtWidgets.QLabel(parent=self.AddStudent)
        self.GenderText.setGeometry(QtCore.QRect(30, 130, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.GenderText.setFont(font)
        self.GenderText.setObjectName("GenderText")
        self.YLevelDD = QtWidgets.QComboBox(parent=self.AddStudent)
        self.YLevelDD.setGeometry(QtCore.QRect(150, 160, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.YLevelDD.setFont(font)
        self.YLevelDD.setObjectName("YLevelDD")
        self.YLevelDD.addItems(["","1", "2", "3", "4"])
        self.FNameTB = QtWidgets.QLineEdit(parent=self.AddStudent)
        self.FNameTB.setGeometry(QtCore.QRect(150, 70, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.FNameTB.setFont(font)
        self.FNameTB.setPlaceholderText("")
        self.FNameTB.setObjectName("FNameTB")
        self.LNameTB = QtWidgets.QLineEdit(parent=self.AddStudent)
        self.LNameTB.setGeometry(QtCore.QRect(150, 100, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.LNameTB.setFont(font)
        self.LNameTB.setPlaceholderText("")
        self.LNameTB.setObjectName("LNameTB")
        self.PCodeText = QtWidgets.QLabel(parent=self.AddStudent)
        self.PCodeText.setGeometry(QtCore.QRect(30, 190, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.PCodeText.setFont(font)
        self.PCodeText.setObjectName("PCodeText")
        self.PCodeDD = QtWidgets.QComboBox(parent=self.AddStudent)
        self.PCodeDD.setGeometry(QtCore.QRect(150, 190, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.PCodeDD.setFont(font)
        self.PCodeDD.setObjectName("PCodeDD")
        self.PCodeDD.addItem("")
        self.AddStudentButton = QtWidgets.QPushButton(parent=self.AddStudent)
        self.AddStudentButton.setGeometry(QtCore.QRect(280, 230, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.AddStudentButton.setFont(font)
        self.AddStudentButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.AddStudentButton.setDisabled(True)
        self.AddStudentButton.setObjectName("AddStudentButton")
        ##-------------------------------------END OF ADD STUDENT PANEL-------------------------------------

        ##-------------------------------------START OF ADD PROGRAM PANEL-------------------------------------
        self.AddProgram = QtWidgets.QFrame(parent=MainPage)
        self.AddProgram.setGeometry(QtCore.QRect(1050, 540, 411, 181))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.AddProgram.setFont(font)
        self.AddProgram.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.AddProgram.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.AddProgram.setObjectName("AddProgram")
        self.AddProgram.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=15, color=QColor("#96b2c9")))  
        self.AddProgramText = QtWidgets.QLabel(parent=self.AddProgram)
        self.AddProgramText.setGeometry(QtCore.QRect(10, 10, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.AddProgramText.setFont(font)
        self.AddProgramText.setObjectName("AddProgramText")
        self.PCodeText2 = QtWidgets.QLabel(parent=self.AddProgram)
        self.PCodeText2.setGeometry(QtCore.QRect(30, 40, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.PCodeText2.setFont(font)
        self.PCodeText2.setObjectName("PCodeText2")
        self.PCodeTB = QtWidgets.QLineEdit(parent=self.AddProgram)
        self.PCodeTB.setGeometry(QtCore.QRect(150, 40, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.PCodeTB.setFont(font)
        self.PCodeTB.setObjectName("PCodeTB")
        self.PNameText = QtWidgets.QLabel(parent=self.AddProgram)
        self.PNameText.setGeometry(QtCore.QRect(30, 70, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.PNameText.setFont(font)
        self.PNameText.setObjectName("PNameText")
        self.PCollCodeText = QtWidgets.QLabel(parent=self.AddProgram)
        self.PCollCodeText.setGeometry(QtCore.QRect(30, 100, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.PCollCodeText.setFont(font)
        self.PCollCodeText.setObjectName("PCollCodeText")
        self.PNameTB = QtWidgets.QLineEdit(parent=self.AddProgram)
        self.PNameTB.setGeometry(QtCore.QRect(150, 70, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.PNameTB.setFont(font)
        self.PNameTB.setText("")
        self.PNameTB.setObjectName("PNameTB")
        self.AddProgramButton = QtWidgets.QPushButton(parent=self.AddProgram)
        self.AddProgramButton.setGeometry(QtCore.QRect(280, 140, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.AddProgramButton.setFont(font)
        self.AddProgramButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.AddProgramButton.setDisabled(True)
        self.AddProgramButton.setObjectName("AddProgramButton")
        self.PCollCodeDD = QtWidgets.QComboBox(parent=self.AddProgram)
        self.PCollCodeDD.setGeometry(QtCore.QRect(150, 100, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.PCollCodeDD.setFont(font)
        self.PCollCodeDD.setObjectName("PCollCodeDD")
        self.PCollCodeDD.addItem("")
        ##-------------------------------------END OF ADD PROGRAM PANEL-------------------------------------

        ##-------------------------------------START OF ADD COLLEGE PANEL-------------------------------------
        self.AddCollege = QtWidgets.QFrame(parent=MainPage)
        self.AddCollege.setGeometry(QtCore.QRect(1050, 360, 411, 161))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.AddCollege.setFont(font)
        self.AddCollege.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.AddCollege.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.AddCollege.setObjectName("AddCollege")
        self.AddCollege.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=15, color=QColor("#96b2c9")))  
        self.AddCollegeText = QtWidgets.QLabel(parent=self.AddCollege)
        self.AddCollegeText.setGeometry(QtCore.QRect(10, 10, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.AddCollegeText.setFont(font)
        self.AddCollegeText.setObjectName("AddCollegeText")
        self.CCodeText = QtWidgets.QLabel(parent=self.AddCollege)
        self.CCodeText.setGeometry(QtCore.QRect(30, 40, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.CCodeText.setFont(font)
        self.CCodeText.setObjectName("CCodeText")
        self.CCodeTB = QtWidgets.QLineEdit(parent=self.AddCollege)
        self.CCodeTB.setGeometry(QtCore.QRect(150, 40, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.CCodeTB.setFont(font)
        self.CCodeTB.setText("")
        self.CCodeTB.setObjectName("CCodeTB")
        self.CNameText = QtWidgets.QLabel(parent=self.AddCollege)
        self.CNameText.setGeometry(QtCore.QRect(30, 70, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.CNameText.setFont(font)
        self.CNameText.setObjectName("CNameText")
        self.CNameTB = QtWidgets.QLineEdit(parent=self.AddCollege)
        self.CNameTB.setGeometry(QtCore.QRect(150, 70, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.CNameTB.setFont(font)
        self.CNameTB.setText("")
        self.CNameTB.setObjectName("CNameTB")
        self.AddCollegeButton = QtWidgets.QPushButton(parent=self.AddCollege)
        self.AddCollegeButton.setGeometry(QtCore.QRect(280, 120, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.AddCollegeButton.setFont(font)
        self.AddCollegeButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.AddCollegeButton.setObjectName("AddCollegeButton")
        ##-------------------------------------END OF ADD COLLEGE PANEL-------------------------------------

        ##-------------------------------------START OF DATABASE PANEL-------------------------------------
        self.Database = QtWidgets.QFrame(parent=MainPage)
        self.Database.setGeometry(QtCore.QRect(30, 70, 1001, 651))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.Database.setFont(font)
        self.Database.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.Database.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Database.setObjectName("Database")
        self.Database.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=15, color=QColor("#96b2c9")))  
        self.ListData = QtWidgets.QTabWidget(parent=self.Database)
        self.ListData.setGeometry(QtCore.QRect(20, 10, 961, 631))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.ListData.setFont(font)
        self.ListData.setTabPosition(QtWidgets.QTabWidget.TabPosition.North)
        self.ListData.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.ListData.setElideMode(QtCore.Qt.TextElideMode.ElideNone)
        self.ListData.setObjectName("ListData")

        ##-------------------------------START OF STUDENT TAB-------------------------------
        self.StudentDatabase = QtWidgets.QWidget()
        self.StudentDatabase.setObjectName("StudentDatabase")
        self.StudentTable = QtWidgets.QTableWidget(parent=self.StudentDatabase)
        self.StudentTable.setGeometry(QtCore.QRect(0, 60, 961, 501))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.StudentTable.setFont(font)
        self.StudentTable.setObjectName("StudentTable")

        self.StudentSearchText = QtWidgets.QLabel(parent=self.StudentDatabase)
        self.StudentSearchText.setGeometry(QtCore.QRect(0, 20, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.StudentSearchText.setFont(font)
        self.StudentSearchText.setObjectName("StudentSearchText")
        self.StudentSearchDD = QtWidgets.QComboBox(parent=self.StudentDatabase)
        self.StudentSearchDD.setGeometry(QtCore.QRect(80, 20, 111, 22))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.StudentSearchDD.setFont(font)
        self.StudentSearchDD.setObjectName("StudentSearchDD")
        self.StudentSearchDD.addItems(["", "ID #", "First Name", "Last Name", "Year Level", "Gender", "Program Code"])
        self.StudentSearchTB = QtWidgets.QLineEdit(parent=self.StudentDatabase)
        self.StudentSearchTB.setGeometry(QtCore.QRect(200, 20, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.StudentSearchTB.setFont(font)
        self.StudentSearchTB.setPlaceholderText("")
        self.StudentSearchTB.setObjectName("StudentSearchTB")
        self.StudentSearchButton = QtWidgets.QPushButton(parent=self.StudentDatabase)
        self.StudentSearchButton.setGeometry(QtCore.QRect(420, 20, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.StudentSearchButton.setFont(font)
        self.StudentSearchButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.StudentSearchButton.setStyleSheet(Path('Styles/SearchButton.qss').read_text())
        self.StudentSearchButton.setObjectName("StudentSearchButton")
        self.StudentSortText = QtWidgets.QLabel(parent=self.StudentDatabase)
        self.StudentSortText.setGeometry(QtCore.QRect(790, 20, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.StudentSortText.setFont(font)
        self.StudentSortText.setObjectName("StudentSortText")
        self.StudentSortDD = QtWidgets.QComboBox(parent=self.StudentDatabase)
        self.StudentSortDD.setGeometry(QtCore.QRect(850, 20, 111, 22))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.StudentSortDD.setFont(font)
        self.StudentSortDD.setObjectName("StudentSortDD")
        self.StudentSortDD.addItems(["", "ID #", "First Name", "Last Name", "Year Level", "Gender", "Program Code"])
        self.EditStudentButton = QtWidgets.QPushButton(parent=self.StudentDatabase)
        self.EditStudentButton.setEnabled(True)
        self.EditStudentButton.setGeometry(QtCore.QRect(0, 570, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.EditStudentButton.setFont(font)
        self.EditStudentButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.EditStudentButton.setObjectName("EditStudentButton")
        self.EditStudentButton.setDisabled(True)
        self.DeleteStudentButton = QtWidgets.QPushButton(parent=self.StudentDatabase)
        self.DeleteStudentButton.setEnabled(True)
        self.DeleteStudentButton.setGeometry(QtCore.QRect(130, 570, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.DeleteStudentButton.setFont(font)
        self.DeleteStudentButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.DeleteStudentButton.setObjectName("DeleteStudentButton")
        self.DeleteStudentButton.setDisabled(True)
        self.ListData.addTab(self.StudentDatabase, "")
        ##-------------------------------END OF STUDENT TAB-------------------------------

        ##-------------------------------START OF PROGRAM TAB-------------------------------
        self.ProgramDatabase = QtWidgets.QWidget()
        self.ProgramDatabase.setObjectName("ProgramDatabase")
        self.ProgramSearchText = QtWidgets.QLabel(parent=self.ProgramDatabase)
        self.ProgramSearchText.setGeometry(QtCore.QRect(0, 20, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.ProgramSearchText.setFont(font)
        self.ProgramSearchText.setObjectName("ProgramSearchText")
        self.ProgramSearchDD = QtWidgets.QComboBox(parent=self.ProgramDatabase)
        self.ProgramSearchDD.setGeometry(QtCore.QRect(80, 20, 111, 22))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.ProgramSearchDD.setFont(font)
        self.ProgramSearchDD.setObjectName("ProgramSearchDD")
        self.ProgramSearchDD.addItems(["", "Program Code", "Program Name", "College Code"])
        self.ProgramSearchTB = QtWidgets.QLineEdit(parent=self.ProgramDatabase)
        self.ProgramSearchTB.setGeometry(QtCore.QRect(200, 20, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.ProgramSearchTB.setFont(font)
        self.ProgramSearchTB.setPlaceholderText("")
        self.ProgramSearchTB.setObjectName("ProgramSearchTB")
        self.ProgramSearchButton = QtWidgets.QPushButton(parent=self.ProgramDatabase)
        self.ProgramSearchButton.setGeometry(QtCore.QRect(420, 20, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.ProgramSearchButton.setFont(font)
        self.ProgramSearchButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.ProgramSearchButton.setStyleSheet(Path('Styles/SearchButton.qss').read_text())
        self.ProgramSearchButton.setObjectName("ProgramSearchButton")
        self.ProgramSortText = QtWidgets.QLabel(parent=self.ProgramDatabase)
        self.ProgramSortText.setGeometry(QtCore.QRect(790, 20, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.ProgramSortText.setFont(font)
        self.ProgramSortText.setObjectName("ProgramSortText")
        self.ProgramSortDD = QtWidgets.QComboBox(parent=self.ProgramDatabase)
        self.ProgramSortDD.setGeometry(QtCore.QRect(850, 20, 111, 22))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.ProgramSortDD.setFont(font)
        self.ProgramSortDD.setObjectName("ProgramSortDD")
        self.ProgramSortDD.addItems(["", "Program Code", "Program Name", "College Code"])

        self.EditProgramButton = QtWidgets.QPushButton(parent=self.ProgramDatabase)
        self.EditProgramButton.setEnabled(True)
        self.EditProgramButton.setGeometry(QtCore.QRect(0, 570, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.EditProgramButton.setFont(font)
        self.EditProgramButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.EditProgramButton.setObjectName("EditProgramButton")
        self.EditProgramButton.setDisabled(True)
        self.DeleteProgramButton = QtWidgets.QPushButton(parent=self.ProgramDatabase)
        self.DeleteProgramButton.setEnabled(True)
        self.DeleteProgramButton.setGeometry(QtCore.QRect(130, 570, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.DeleteProgramButton.setFont(font)
        self.DeleteProgramButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.DeleteProgramButton.setObjectName("DeleteProgramButton")
        self.DeleteProgramButton.setDisabled(True)
        self.ProgramTable = QtWidgets.QTableWidget(parent=self.ProgramDatabase)
        self.ProgramTable.setGeometry(QtCore.QRect(0, 60, 961, 501))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.ProgramTable.setFont(font)
        self.ProgramTable.setObjectName("ProgramTable")
        self.ProgramTable.setColumnCount(2)
        self.ProgramTable.setRowCount(0)
        self.ListData.addTab(self.ProgramDatabase, "")
        ##-------------------------------END OF PROGRAM TAB-------------------------------

        ##-------------------------------START OF COLLEGE TAB-------------------------------
        self.CollegeDatabase = QtWidgets.QWidget()
        self.CollegeDatabase.setObjectName("CollegeDatabase")
        self.CollegeTable = QtWidgets.QTableWidget(parent=self.CollegeDatabase)
        self.CollegeTable.setGeometry(QtCore.QRect(0, 60, 961, 501))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.CollegeTable.setFont(font)
        self.CollegeTable.setObjectName("CollegeTable")

        self.CollegeSearchText = QtWidgets.QLabel(parent=self.CollegeDatabase)
        self.CollegeSearchText.setGeometry(QtCore.QRect(0, 20, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.CollegeSearchText.setFont(font)
        self.CollegeSearchText.setObjectName("CollegeSearchText")
        self.CollegeSearchDD = QtWidgets.QComboBox(parent=self.CollegeDatabase)
        self.CollegeSearchDD.setGeometry(QtCore.QRect(80, 20, 111, 22))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.CollegeSearchDD.setFont(font)
        self.CollegeSearchDD.setObjectName("CollegeSearchDD")
        self.CollegeSearchDD.addItems(["","College Code", "College Name"])
        self.CollegeSearchTB = QtWidgets.QLineEdit(parent=self.CollegeDatabase)
        self.CollegeSearchTB.setGeometry(QtCore.QRect(200, 20, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.CollegeSearchTB.setFont(font)
        self.CollegeSearchTB.setPlaceholderText("")
        self.CollegeSearchTB.setObjectName("CollegeSearchTB")
        self.CollegeSearchButton = QtWidgets.QPushButton(parent=self.CollegeDatabase)
        self.CollegeSearchButton.setGeometry(QtCore.QRect(420, 20, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.CollegeSearchButton.setFont(font)
        self.CollegeSearchButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.CollegeSearchButton.setStyleSheet(Path('Styles/SearchButton.qss').read_text())
        self.CollegeSearchButton.setObjectName("CollegeSearchButton")
        self.CollegeSortText = QtWidgets.QLabel(parent=self.CollegeDatabase)
        self.CollegeSortText.setGeometry(QtCore.QRect(790, 20, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.CollegeSortText.setFont(font)
        self.CollegeSortText.setObjectName("CollegeSortText")
        self.CollegeSortDD = QtWidgets.QComboBox(parent=self.CollegeDatabase)
        self.CollegeSortDD.setGeometry(QtCore.QRect(850, 20, 111, 22))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.CollegeSortDD.setFont(font)
        self.CollegeSortDD.setObjectName("CollegeSortDD")
        self.CollegeSortDD.addItems(["","College Code", "College Name"])

        self.EditCollegeButton = QtWidgets.QPushButton(parent=self.CollegeDatabase)
        self.EditCollegeButton.setEnabled(True)
        self.EditCollegeButton.setGeometry(QtCore.QRect(0, 570, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.EditCollegeButton.setFont(font)
        self.EditCollegeButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.EditCollegeButton.setObjectName("EditCollegeButton")
        self.EditCollegeButton.setDisabled(True)
        self.DeleteCollegeButton = QtWidgets.QPushButton(parent=self.CollegeDatabase)
        self.DeleteCollegeButton.setEnabled(True)
        self.DeleteCollegeButton.setGeometry(QtCore.QRect(130, 570, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.DeleteCollegeButton.setFont(font)
        self.DeleteCollegeButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.DeleteCollegeButton.setObjectName("DeleteCollegeButton")
        self.DeleteCollegeButton.setDisabled(True)
        self.ListData.addTab(self.CollegeDatabase, "")
        ##-------------------------------END OF COLLEGE TAB-------------------------------

        MainPage.setTabOrder(self.IDTB, self.FNameTB)
        MainPage.setTabOrder(self.FNameTB, self.LNameTB)
        MainPage.setTabOrder(self.LNameTB, self.GenderDD)
        MainPage.setTabOrder(self.GenderDD, self.YLevelDD)
        MainPage.setTabOrder(self.YLevelDD, self.PCodeDD)
        MainPage.setTabOrder(self.PCodeDD, self.AddStudentButton)
        MainPage.setTabOrder(self.AddStudentButton, self.CCodeTB)
        MainPage.setTabOrder(self.CCodeTB, self.CNameTB)
        MainPage.setTabOrder(self.CNameTB, self.AddCollegeButton)
        MainPage.setTabOrder(self.AddCollegeButton, self.PCodeTB)
        MainPage.setTabOrder(self.PCodeTB, self.PNameTB)
        MainPage.setTabOrder(self.PNameTB, self.PCollCodeDD)
        MainPage.setTabOrder(self.PCollCodeDD, self.AddProgramButton)

        ##-------------------------------------END OF DATABASE PANEL-------------------------------------

        self.Heading = QtWidgets.QFrame(parent=MainPage)
        self.Heading.setGeometry(QtCore.QRect(0, 0, 1491, 51))
        self.Heading.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.Heading.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Heading.setObjectName("Heading")
        self.HeadingTitle = QtWidgets.QLabel(parent=self.Heading)
        self.HeadingTitle.setGeometry(QtCore.QRect(40, 10, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.HeadingTitle.setFont(font)
        self.HeadingTitle.setObjectName("HeadingTitle")

        self.retranslateUi(MainPage)
        QtCore.QMetaObject.connectSlotsByName(MainPage)

    def retranslateUi(self, MainPage):
        _translate = QtCore.QCoreApplication.translate
        MainPage.setWindowTitle(_translate("MainPage", "Dialog"))
        self.AddStudentText.setText(_translate("MainPage", "Add Student"))
        self.IDText.setText(_translate("MainPage", "ID #"))
        self.FNameText.setText(_translate("MainPage", "First Name"))
        self.LNameText.setText(_translate("MainPage", "Last Name"))
        self.YLevelText.setText(_translate("MainPage", "Year Level"))
        self.GenderText.setText(_translate("MainPage", "Gender"))
        self.PCodeText.setText(_translate("MainPage", "Program Code"))
        self.AddStudentButton.setText(_translate("MainPage", "Add Student"))
        self.AddProgramText.setText(_translate("MainPage", "Add Program"))
        self.PCodeText2.setText(_translate("MainPage", "Code"))
        self.PCodeTB.setPlaceholderText(_translate("MainPage", "ex. BSCS"))
        self.PNameText.setText(_translate("MainPage", "Program Name"))
        self.PCollCodeText.setText(_translate("MainPage", "College Code"))
        self.PNameTB.setPlaceholderText(_translate("MainPage", "ex. Bachelor of Science in Computer Science"))
        self.AddProgramButton.setText(_translate("MainPage", "Add Program"))
        self.AddCollegeText.setText(_translate("MainPage", "Add College"))
        self.CCodeText.setText(_translate("MainPage", "Code"))
        self.CCodeTB.setPlaceholderText(_translate("MainPage", "ex. CCS"))
        self.CNameText.setText(_translate("MainPage", "College Name"))
        self.CNameTB.setPlaceholderText(_translate("MainPage", "ex. College of Computer Studies"))
        self.AddCollegeButton.setText(_translate("MainPage", "Add College"))

        self.StudentSearchText.setText(_translate("MainPage", "Search by:"))
        self.StudentSearchButton.setText(_translate("MainPage", "Search"))
        self.StudentSortText.setText(_translate("MainPage", "Sort by:"))
        self.ProgramSearchText.setText(_translate("MainPage", "Search by:"))
        self.ProgramSearchButton.setText(_translate("MainPage", "Search"))
        self.ProgramSortText.setText(_translate("MainPage", "Sort by:"))
        self.CollegeSearchText.setText(_translate("MainPage", "Search by:"))
        self.CollegeSearchButton.setText(_translate("MainPage", "Search"))
        self.CollegeSortText.setText(_translate("MainPage", "Sort by:"))

        self.EditStudentButton.setText(_translate("MainPage", "Edit Student"))
        self.DeleteStudentButton.setText(_translate("MainPage", "Delete Student"))
        self.ListData.setTabText(self.ListData.indexOf(self.StudentDatabase), _translate("MainPage", "Student Database"))
        self.EditProgramButton.setText(_translate("MainPage", "Edit Program"))
        self.DeleteProgramButton.setText(_translate("MainPage", "Delete Program"))
        self.ListData.setTabText(self.ListData.indexOf(self.ProgramDatabase), _translate("MainPage", "Program Database"))
        self.EditCollegeButton.setText(_translate("MainPage", "Edit College"))
        self.DeleteCollegeButton.setText(_translate("MainPage", "Delete College"))
        self.ListData.setTabText(self.ListData.indexOf(self.CollegeDatabase), _translate("MainPage", "College Database"))

        self.HeadingTitle.setText(_translate("MainPage", "Student Information System"))


# Main Window Class
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainPage()
        self.ui.setupUi(self)
        self.setWindowTitle('Simple Student Information System')
        self.setWindowIcon(QIcon('Assets/StudentIcon.png'))

        self.setupValidators()
        self.openStudentCSV()
        self.openProgramCSV()
        self.openCollegeCSV()
        self.TableFormat()
        self.AddStudentButtonState()
        self.AddCollegeButtonState()
        self.AddProgramButtonState()
        self.setupConnections()
        self.PopulateCollegeCode()
        self.PopulateProgramCode()
        self.setFocus()

    def clearTableSelection(self):
        self.ui.StudentTable.clearSelection()
        self.ui.ProgramTable.clearSelection()
        self.ui.CollegeTable.clearSelection()

    def mousePressEvent(self, event):
        self.setFocus() 
        super().mousePressEvent(event)

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.Type.MouseButtonPress:
            if not isinstance(self.focusWidget(), QtWidgets.QLineEdit):  
                self.setFocus()  

            if not self.ui.StudentTable.underMouse() and not self.ui.ProgramTable.underMouse() and not self.ui.CollegeTable.underMouse():
                self.clearTableSelection()
                self.updateDeleteButtonState() 
        return super().eventFilter(obj, event)

    def setupConnections(self):
        self.ui.AddStudentButton.clicked.connect(self.AddStudentUpdateTable)
        self.ui.AddCollegeButton.clicked.connect(self.AddCollegeUpdateTable)
        self.ui.AddProgramButton.clicked.connect(self.AddProgramUpdateTable)

        self.ui.IDTB.textChanged.connect(self.AddStudentButtonState)
        self.ui.FNameTB.textChanged.connect(self.AddStudentButtonState)
        self.ui.LNameTB.textChanged.connect(self.AddStudentButtonState)
        self.ui.GenderDD.currentTextChanged.connect(self.AddStudentButtonState)
        self.ui.YLevelDD.currentTextChanged.connect(self.AddStudentButtonState)
        self.ui.PCodeDD.currentTextChanged.connect(self.AddStudentButtonState)

        self.ui.CCodeTB.textChanged.connect(self.AddCollegeButtonState)
        self.ui.CNameTB.textChanged.connect(self.AddCollegeButtonState)
        
        self.ui.PCodeTB.textChanged.connect(self.AddProgramButtonState)
        self.ui.PNameTB.textChanged.connect(self.AddProgramButtonState)
        self.ui.PCollCodeDD.currentTextChanged.connect(self.AddProgramButtonState)

        self.ui.StudentSortDD.currentTextChanged.connect(self.sort_student_table)
        self.ui.ProgramSortDD.currentTextChanged.connect(self.sort_program_table)
        self.ui.CollegeSortDD.currentTextChanged.connect(self.sort_college_table)

        self.ui.StudentTable.itemSelectionChanged.connect(self.updateDeleteButtonState)
        self.ui.ProgramTable.itemSelectionChanged.connect(self.updateDeleteButtonState)
        self.ui.CollegeTable.itemSelectionChanged.connect(self.updateDeleteButtonState)

        self.ui.DeleteStudentButton.clicked.connect(self.openDeleteStudentPopup)
        self.ui.DeleteProgramButton.clicked.connect(self.openDeleteProgramPopup)
        self.ui.DeleteCollegeButton.clicked.connect(self.openDeleteCollegePopup)

        self.ui.EditStudentButton.clicked.connect(self.openEditStudentPopup)
        self.ui.EditProgramButton.clicked.connect(self.openEditProgramPopup)
        self.ui.EditCollegeButton.clicked.connect(self.openEditCollegePopup)

        self.ui.StudentSearchButton.clicked.connect(self.search_student)
        self.ui.ProgramSearchButton.clicked.connect(self.search_program)
        self.ui.CollegeSearchButton.clicked.connect(self.search_college)


        self.ui.ListData.currentChanged.connect(self.clearTableSelection)
        self.installEventFilter(self)

    def updateDeleteButtonState(self):
        student_selected = len(self.ui.StudentTable.selectedItems()) > 0
        program_selected = len(self.ui.ProgramTable.selectedItems()) > 0
        college_selected = len(self.ui.CollegeTable.selectedItems()) > 0

        self.ui.DeleteStudentButton.setDisabled(not student_selected)
        self.ui.EditStudentButton.setDisabled(not student_selected)
        self.ui.DeleteProgramButton.setDisabled(not program_selected)
        self.ui.EditProgramButton.setDisabled(not program_selected)
        self.ui.DeleteCollegeButton.setDisabled(not college_selected)
        self.ui. EditCollegeButton.setDisabled(not college_selected)

    def openStudentCSV(self):
        db = DatabaseConnection()
        connection = db.get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM student")
        students = cursor.fetchall()

        if students:       
            self.ui.StudentTable.setRowCount(len(students))
            self.ui.StudentTable.setColumnCount(len(students[0]))
            self.ui.StudentTable.setHorizontalHeaderLabels(["ID#","First Name","Last Name","Year Level","Gender","Program Code"])
            
            for row_idx, student in enumerate(students):
                for col_idx, cell in enumerate(student):
                    item = QtWidgets.QTableWidgetItem(str(cell))
                    if cell is None:
                        item.setForeground(QColor("red"))
                        item.setText("NULL")
                    self.ui.StudentTable.setItem(row_idx, col_idx, item)
        cursor.close()
        db.close_connection()           

    def openProgramCSV(self):
        db = DatabaseConnection()
        connection = db.get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM program")
        programs = cursor.fetchall()

        if programs:
            self.ui.ProgramTable.setRowCount(len(programs))
            self.ui.ProgramTable.setColumnCount(len(programs[0]))
            self.ui.ProgramTable.setHorizontalHeaderLabels(["Program Code","Program Name","College Code"])

            for row_idx, program in enumerate(programs):
                for col_idx, cell in enumerate(program):
                    item = QtWidgets.QTableWidgetItem(cell)
                    if cell is None:
                        item.setForeground(QColor("red"))
                        item.setText("NULL")
                    self.ui.ProgramTable.setItem(row_idx, col_idx, item)
        cursor.close()
        db.close_connection()    
        
    def openCollegeCSV(self):
        db = DatabaseConnection()
        connection = db.get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM college")
        colleges = cursor.fetchall()

        if colleges:
            self.ui.CollegeTable.setRowCount(len(colleges))
            self.ui.CollegeTable.setColumnCount(len(colleges[0]))
            self.ui.CollegeTable.setHorizontalHeaderLabels(["College Code","College Name"])

            for row_idx, college in enumerate(colleges):
                for col_idx, cell in enumerate(college):
                    item = QtWidgets.QTableWidgetItem(cell)
                    self.ui.CollegeTable.setItem(row_idx, col_idx, item)
        
    def TableFormat(self):
        self.ui.StudentTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.ui.StudentTable.horizontalHeader().setHighlightSections(False)
        self.ui.StudentTable.verticalHeader().setHighlightSections(False)
        self.ui.StudentTable.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.ui.StudentTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.ui.StudentTable.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.ui.StudentTable.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ui.StudentTable.setAlternatingRowColors(True)

        self.ui.ProgramTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.ui.ProgramTable.horizontalHeader().setHighlightSections(False)
        self.ui.ProgramTable.verticalHeader().setHighlightSections(False)
        self.ui.ProgramTable.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.ui.ProgramTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.ui.ProgramTable.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.ui.ProgramTable.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ui.ProgramTable.setAlternatingRowColors(True)

        self.ui.CollegeTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.ui.CollegeTable.horizontalHeader().setHighlightSections(False)
        self.ui.CollegeTable.verticalHeader().setHighlightSections(False)
        self.ui.CollegeTable.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.ui.CollegeTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.ui.CollegeTable.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.ui.CollegeTable.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ui.CollegeTable.setAlternatingRowColors(True)

    def AddStudentButtonState(self):
        student_id = self.ui.IDTB.text()
        first_name = self.ui.FNameTB.text()
        last_name = self.ui.LNameTB.text()
        gender = self.ui.GenderDD.currentText()
        year_level = self.ui.YLevelDD.currentText()
        program_code = self.ui.PCodeDD.currentText()

        if student_id and first_name and last_name and gender and year_level and program_code:
            self.ui.AddStudentButton.setDisabled(False)
        else:
            self.ui.AddStudentButton.setDisabled(True)
    
    def AddCollegeButtonState(self):
        college_code = self.ui.CCodeTB.text()
        college_name = self.ui.CNameTB.text()

        if college_code and college_name:
            self.ui.AddCollegeButton.setDisabled(False)
        else:
            self.ui.AddCollegeButton.setDisabled(True)
    
    def AddProgramButtonState(self):
        program_code = self.ui.PCodeTB.text()
        program_name = self.ui.PNameTB.text()
        pcollege_code = self.ui.PCollCodeDD.currentText()

        if program_code and program_name and pcollege_code:
            self.ui.AddProgramButton.setDisabled(False)
        else:
            self.ui.AddProgramButton.setDisabled(True)
              
    def AddStudentUpdateTable(self):
        db = DatabaseConnection()
        connection = db.get_connection()
        cursor = connection.cursor()

        student_id = self.ui.IDTB.text().strip()

        cursor.execute("SELECT COUNT(*) FROM student WHERE student_id = %s", (student_id,))
        if cursor.fetchone()[0] > 0:
            self.duplicate_popup = DuplicateStudentPopup()
            self.duplicate_popup.setModal(True)
            self.duplicate_popup.show()
            return

        student_data = (
            self.ui.IDTB.text(),
            self.ui.FNameTB.text().title(),
            self.ui.LNameTB.text().title(),
            int(self.ui.YLevelDD.currentText()),
            self.ui.GenderDD.currentText(),
            self.ui.PCodeDD.currentText()
        )
        cursor.execute("INSERT INTO student VALUES (%s, %s, %s, %s, %s, %s)", student_data)
        connection.commit()
    
        self.ui.IDTB.clear()
        self.ui.FNameTB.clear()
        self.ui.LNameTB.clear()
        self.ui.GenderDD.setCurrentIndex(0)
        self.ui.YLevelDD.setCurrentIndex(0)
        self.ui.PCodeDD.setCurrentIndex(0)
        self.ui.AddStudentButton.setDisabled(True)

        self.openStudentCSV()
        self.sort_student_table()
        self.setFocus()
        cursor.close()
        db.close_connection()  

    def AddCollegeUpdateTable(self):
        db = DatabaseConnection()
        connection = db.get_connection()
        cursor = connection.cursor()

        ccode = self.ui.CCodeTB.text().strip().upper()

        cursor.execute("SELECT COUNT(*) FROM college WHERE college_code = %s", (ccode,))
        if cursor.fetchone()[0] > 0:
            self.duplicate_popup = DuplicateCollegePopup()
            self.duplicate_popup.setModal(True)
            self.duplicate_popup.show()
            return
        
        college_data = (
            self.ui.CCodeTB.text().upper(),
            self.ui.CNameTB.text().title()
        )

        cursor.execute("INSERT INTO college VALUES (%s, %s)", college_data)
        connection.commit()

        self.ui.CCodeTB.clear()
        self.ui.CNameTB.clear()
        self.ui.AddCollegeButton.setDisabled(True)

        self.openCollegeCSV()
        self.sort_college_table()
        self.PopulateCollegeCode()   
        self.setFocus()
        cursor.close()
        db.close_connection() 

    def AddProgramUpdateTable(self):
        db = DatabaseConnection()
        connection = db.get_connection()
        cursor = connection.cursor()

        pcode = self.ui.PCodeTB.text().strip().upper()

        cursor.execute("SELECT COUNT(*) FROM program WHERE program_code = %s", (pcode,))
        if cursor.fetchone()[0] > 0:
            self.duplicate_popup = DuplicateProgramPopup()
            self.duplicate_popup.setModal(True)
            self.duplicate_popup.show()
            return

        program_data = (
            self.ui.PCodeTB.text().upper(),
            self.ui.PNameTB.text().title(),
            self.ui.PCollCodeDD.currentText())

        cursor.execute("INSERT INTO program VALUES (%s, %s, %s)", program_data)
        connection.commit()
    
        self.ui.PCodeTB.clear()
        self.ui.PNameTB.clear()
        self.ui.PCollCodeDD.setCurrentIndex(0)
        self.ui.AddProgramButton.setDisabled(True)

        self.openProgramCSV()
        self.sort_program_table()
        self.PopulateProgramCode()
        self.setFocus()
        cursor.close()
        db.close_connection() 

    def PopulateCollegeCode(self):
        db = DatabaseConnection()
        connection = db.get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT college_code FROM college ORDER BY college_code")
        colleges = cursor.fetchall()
        college_codes = [college[0] for college in colleges]

        self.ui.PCollCodeDD.clear()
        self.ui.PCollCodeDD.addItem("")
        self.ui.PCollCodeDD.addItems(college_codes)

    def PopulateProgramCode(self):
        db = DatabaseConnection()
        connection = db.get_connection()
        cursor = connection.cursor() 

        cursor.execute("SELECT program_code FROM program ORDER BY program_code")
        programs = cursor.fetchall()
        program_codes = [program[0] for program in programs]

        self.ui.PCodeDD.clear()
        self.ui.PCodeDD.addItem("")
        self.ui.PCodeDD.addItems(program_codes)

    def sort_student_table(self):
        sort_columns = {
            "ID #": 0,
            "First Name": 1,
            "Last Name": 2,
            "Year Level": 3,
            "Gender": 4,
            "Program Code": 5
        }

        sort_option = self.ui.StudentSortDD.currentText()
        if not sort_option:  
            self.ui.StudentTable.sortItems(0)
            return

        col = sort_columns.get(sort_option, 0)
        self.ui.StudentTable.sortItems(col)

        for row in range(self.ui.StudentTable.rowCount()):
            item = self.ui.StudentTable.item(row, col)
            if item and item.text().strip().upper() == "NULL":
                item.setForeground(QColor("red"))

    def sort_program_table(self):
        sort_columns = {
            "Program Code": 0,
            "Program Name": 1,
            "College Code": 2,
        }   

        sort_option = self.ui.ProgramSortDD.currentText()
        if not sort_option:  
            self.ui.ProgramTable.sortItems(0)
            return

        col = sort_columns.get(sort_option, 0)
        self.ui.ProgramTable.sortItems(col)

        for row in range(self.ui.ProgramTable.rowCount()):
            item = self.ui.ProgramTable.item(row, col)
            if item and item.text().strip().upper() == "NULL":
                item.setForeground(QColor("red"))

    def sort_college_table(self):
        sort_columns = {
            "College Code": 0,
            "College Name": 1,
        } 

        sort_option = self.ui.CollegeSortDD.currentText()
        if not sort_option:  
            self.ui.CollegeTable.sortItems(0)
            return

        col = sort_columns.get(sort_option, 0)
        self.ui.CollegeTable.sortItems(col)

        for row in range(self.ui.CollegeTable.rowCount()):
            item = self.ui.CollegeTable.item(row, col)

    def openDeleteStudentPopup(self):
        selected_row = self.ui.StudentTable.currentRow()
        if selected_row != -1:  
            student_id = self.ui.StudentTable.item(selected_row, 0).text()  
            self.delete_popup = DeleteStudentPopup(student_id, self)
            self.delete_popup.setModal(True)
            self.delete_popup.show()

    def openEditStudentPopup(self):
        db = DatabaseConnection()
        connection = db.get_connection()
        cursor = connection.cursor()

        selected_row = self.ui.StudentTable.currentRow()
        if selected_row != -1:
            student_data_id = self.ui.StudentTable.item(selected_row, 0).text()

            cursor.execute("SELECT * FROM student WHERE student_id = %s", (student_data_id,))
            student_data = cursor.fetchone() 
            
            if student_data: 
                self.edit_popup = EditStudentPopup(self, selected_row)

                self.edit_popup.ui.PCodeDD.clear()
                current_program = student_data[5]

                cursor.execute("SELECT program_code FROM program ORDER BY program_code")
                programs = cursor.fetchall()
                program_codes = [program[0] for program in programs]

                if current_program == None:
                    program_codes.append("NULL")

                self.edit_popup.ui.PCodeDD.addItems(sorted(program_codes)) 

                if current_program is None:
                    self.edit_popup.ui.PCodeDD.setCurrentText("NULL")

                self.edit_popup.ui.IDTB.setText(str(student_data[0]))
                self.edit_popup.ui.FNameTB.setText(str(student_data[1]))
                self.edit_popup.ui.LNameTB.setText(str(student_data[2]))
                self.edit_popup.ui.YLevelDD.setCurrentText(str(student_data[3]))
                self.edit_popup.ui.GenderDD.setCurrentText(str(student_data[4]))
                self.edit_popup.ui.PCodeDD.setCurrentText(str(student_data[5]))

                self.edit_popup.setModal(True)
                self.edit_popup.show()

    def openDeleteProgramPopup(self):
        selected_row = self.ui.ProgramTable.currentRow()
        if selected_row != -1:
            program_code = self.ui.ProgramTable.item(selected_row, 0).text()
            self.delete_popup = DeleteProgramPopup(program_code, self)
            self.delete_popup.setModal(True)
            self.delete_popup.show()

    def openEditProgramPopup(self):
        db = DatabaseConnection()
        connection = db.get_connection()
        cursor = connection.cursor()

        selected_row = self.ui.ProgramTable.currentRow()
        if selected_row != -1:
            program_data_id = self.ui.ProgramTable.item(selected_row, 0).text()

            cursor.execute("SELECT * FROM program WHERE program_code = %s", (program_data_id,))
            program_data = cursor.fetchone() 

            if program_data:
                self.edit_popup = EditProgramPopup(self, selected_row)

                self.edit_popup.ui.PCollCodeDD.clear()
                current_college = program_data[2]

                cursor.execute("SELECT college_code FROM college ORDER BY college_code")
                colleges = cursor.fetchall()
                college_codes = [college[0] for college in colleges]

                if current_college == None:
                    college_codes.append("NULL")

                self.edit_popup.ui.PCollCodeDD.addItems(sorted(college_codes)) 

                if current_college is None:
                    self.edit_popup.ui.PCollCodeDD.setCurrentText("NULL")

                self.edit_popup.ui.PCodeTB.setText(program_data[0])
                self.edit_popup.ui.PNameTB.setText(program_data[1])
                self.edit_popup.ui.PCollCodeDD.setCurrentText(program_data[2])
                self.edit_popup.setModal(True)
                self.edit_popup.show()

    def openDeleteCollegePopup(self):
        selected_row = self.ui.CollegeTable.currentRow()
        if selected_row != -1:
            program_code = self.ui.CollegeTable.item(selected_row, 0). text()
            self.delete_popup = DeleteCollegePopup(program_code, self)
            self.delete_popup.setModal(True)
            self.delete_popup.show()

    def openEditCollegePopup(self):
        db = DatabaseConnection()
        connection = db.get_connection()
        cursor = connection.cursor()

        selected_row = self.ui.CollegeTable.currentRow()
        if selected_row !=-1:
            college_data_id = self.ui.CollegeTable.item(selected_row, 0).text()
            cursor.execute("SELECT * FROM college WHERE college_code = %s", (college_data_id,))
            college_data = cursor.fetchone() 

            if college_data:
                self.edit_popup = EditCollegePopup(self, selected_row)

                self.edit_popup.ui.CCodeTB.setText(college_data[0])
                self.edit_popup.ui.CNameTB.setText(college_data[1])
                self.edit_popup.setModal(True)
                self.edit_popup.show()

    def search_student(self):
        search_by = self.ui.StudentSearchDD.currentText()
        search_text = self.ui.StudentSearchTB.text().strip().lower()

        if not search_by:
            self.openStudentCSV()
            return

        if not search_text:
            self.openStudentCSV()
            return

        search_options = {
            "ID #": "student_id", 
            "First Name": "first_name",
            "Last Name": "last_name",
            "Year Level": "year_level",
            "Gender": "gender",
            "Program Code": "program_code"
        }

        column_index = search_options.get(search_by, 0)

        db = DatabaseConnection()
        connection = db.get_connection()
        cursor = connection.cursor()

        if search_by == "Gender":
            query = "SELECT * FROM student WHERE {} = %s".format(column_index)
            cursor.execute(query, (search_text,))
        else:
            query = "SELECT * FROM student WHERE {} LIKE %s".format(column_index)
            param = "%" + search_text + "%"
            cursor.execute(query, (param,))
                
        results = cursor.fetchall()
        print(f"Found {len(results)} matching records")
        self.ui.StudentTable.setRowCount(0)

        for row_data in results:
            row_position = self.ui.StudentTable.rowCount()
            self.ui.StudentTable.insertRow(row_position)
            for col, data in enumerate(row_data):
                data_str = str(data) if data is not None else "NULL"
                item = QtWidgets.QTableWidgetItem(data_str)
                if data_str.strip().upper() == "NULL":
                    item.setForeground(QColor("red"))
                else:
                    item.setForeground(QColor("black"))
                self.ui.StudentTable.setItem(row_position, col, item)
        
        cursor.close()
        connection.close()

    def search_program(self):
        search_by = self.ui.ProgramSearchDD.currentText()
        search_text = self.ui.ProgramSearchTB.text().strip().lower()

        if not search_by:
            self.openProgramCSV()
            return

        if not search_text:
            self.openProgramCSV()
            return

        search_options = {
            "Program Code": "program_code",
            "Program Name": "program_name",
            "College Code": "college_code"
        }

        column_index = search_options.get(search_by, 0)

        db = DatabaseConnection()
        connection = db.get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM program WHERE {} LIKE %s".format(column_index)
        param = "%" + search_text + "%"
        cursor.execute(query, (param,))

        results = cursor.fetchall()
        print(f"Found {len(results)} matching records")
        self.ui.ProgramTable.setRowCount(0)

        for row_data in results:
            row_position = self.ui.ProgramTable.rowCount()
            self.ui.ProgramTable.insertRow(row_position)
            for col, data in enumerate(row_data):
                data_str = str(data) if data is not None else "NULL"
                item = QtWidgets.QTableWidgetItem(data_str)
                if data_str.strip().upper() == "NULL":
                    item.setForeground(QColor("red"))
                else:
                    item.setForeground(QColor("black"))
                self.ui.ProgramTable.setItem(row_position, col, item)

    def search_college(self):
        search_by = self.ui.CollegeSearchDD.currentText()
        search_text = self.ui.CollegeSearchTB.text().strip().lower()

        if not search_by:
            self.openCollegeCSV()
            return

        if not search_text:
            self.openCollegeCSV()
            return

        search_options = {
            "College Code": "college_code",
            "College Name": "college_name"
        }

        column_index = search_options.get(search_by, 0)

        db = DatabaseConnection()
        connection = db.get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM college WHERE {} LIKE %s".format(column_index)
        param = "%" + search_text + "%"
        cursor.execute(query, (param,))

        results = cursor.fetchall()
        print(f"Found {len(results)} matching records")
        self.ui.CollegeTable.setRowCount(0)

        for row_data in results:
            row_position = self.ui.CollegeTable.rowCount()
            self.ui.CollegeTable.insertRow(row_position)
            for col, data in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(data)
                self.ui.CollegeTable.setItem(row_position, col, item)

    def setupValidators(self):
        code_validator = QRegularExpressionValidator(QRegularExpression("[A-Za-z]+"))
        self.ui.CCodeTB.setValidator(code_validator)
        id_validator = QRegularExpressionValidator(QRegularExpression("^\\d{4}-\\d{4}$"))
        self.ui.IDTB.setValidator(id_validator)
        name_validator = QRegularExpressionValidator(QRegularExpression("[A-Za-z ]+"))
        self.ui.FNameTB.setValidator(name_validator)
        self.ui.LNameTB.setValidator(name_validator)
    
# Main Function to Run the Application
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


# Entry Point
if __name__ == "__main__":
    main()