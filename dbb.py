# just looked up the code to create a popup window pretty easy
# you have to fetch aand import the UI file of the window into the current window
# and then create an object of that class
# then use that class wit the below code
#
#
# self.window=QtWidgets.QMainWindow() # try using QDialog
# self.ui=other_Window_clas_name()
# self.ui.setupUI(self.window)
# self.window.show()
#
#
# implement a functionnality to write and delete questions from database
# write menu option to export the file
# from preload_voice import preload_questions
# the above import will produce an infinite import error hence find a way around it
# there has too be a way
# also mmaybbe you need to read up on organising a project properly
# god this project work is very hard
from preload_voice import preload_questions
from preload_voice import preload_resume_questions
from playsound import playsound
from chat_bot import chatgui
from gtts import gTTS
from pygame import mixer
import DetectVoice as dtV
import voicetotextsenitment as vot
from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5
import threading
from PyQt5.QtCore import pyqtSlot
from voicetotextsenitment import *
# from voicetotextsenitment import busy
from faceemotions import *
from faceemotions import result_of_face_emotion as rsfe
from voicetotextsenitment import result_of_sentiment_analysis as rsvs
from DetectVoice import result_of_DetectVoice as rsdt
from DetectVoice import *
from dbmsconnect import *
import time
from tkinter import filedialog as fd
from PyQt5 import QtCore, QtGui, QtWidgets




from PyQt5 import QtCore, QtGui, QtWidgets


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'projectUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


# class Ui_Dialog(object):
#     def setupUi(self, Dialog):
#         Dialog.setObjectName("Dialog")
#         Dialog.resize(1799, 819)
#         Dialog.setStyleSheet("background-color: rgb(34, 63, 116);")
#         self.FaceFrame = QtWidgets.QFrame(Dialog)
#         self.FaceFrame.setGeometry(QtCore.QRect(30, 130, 311, 371))
#         self.FaceFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.FaceFrame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.FaceFrame.setObjectName("FaceFrame")
#         self.textEdit = QtWidgets.QTextEdit(self.FaceFrame)
#         self.textEdit.setGeometry(QtCore.QRect(10, 70, 291, 251))
#         self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
#         self.textEdit.setObjectName("textEdit")
#         self.label = QtWidgets.QLabel(self.FaceFrame)
#         self.label.setGeometry(QtCore.QRect(10, 20, 231, 41))
#         font = QtGui.QFont()
#         font.setPointSize(15)
#         self.label.setFont(font)
#         self.label.setStyleSheet("color: rgb(172, 196, 252);")
#         self.label.setObjectName("label")
#         self.facelaunch = QtWidgets.QPushButton(self.FaceFrame)
#         self.facelaunch.setGeometry(QtCore.QRect(170, 330, 131, 28))
#         self.facelaunch.setStyleSheet("background-color: rgb(189, 192, 234);")
#         self.facelaunch.setObjectName("facelaunch")
#         self.VoiceFrame = QtWidgets.QFrame(Dialog)
#         self.VoiceFrame.setGeometry(QtCore.QRect(380, 130, 331, 371))
#         self.VoiceFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.VoiceFrame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.VoiceFrame.setObjectName("VoiceFrame")
#         self.textEdit_2 = QtWidgets.QTextEdit(self.VoiceFrame)
#         self.textEdit_2.setGeometry(QtCore.QRect(20, 70, 291, 251))
#         self.textEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
#         self.textEdit_2.setObjectName("textEdit_2")
#         self.voicetonelaunch = QtWidgets.QPushButton(self.VoiceFrame)
#         self.voicetonelaunch.setGeometry(QtCore.QRect(182, 330, 131, 28))
#         self.voicetonelaunch.setStyleSheet("background-color: rgb(189, 192, 234);")
#         self.voicetonelaunch.setObjectName("voicetonelaunch")
#         self.radioButton = QtWidgets.QRadioButton(self.VoiceFrame)
#         self.radioButton.setGeometry(QtCore.QRect(20, 330, 95, 20))
#         self.radioButton.setStyleSheet("color: rgb(172, 196, 252);")
#         self.radioButton.setObjectName("radioButton")
#         self.label_2 = QtWidgets.QLabel(self.VoiceFrame)
#         self.label_2.setGeometry(QtCore.QRect(20, 20, 241, 41))
#         font = QtGui.QFont()
#         font.setPointSize(15)
#         self.label_2.setFont(font)
#         self.label_2.setStyleSheet("color: rgb(172, 196, 252);")
#         self.label_2.setObjectName("label_2")
#         self.SentiFrame = QtWidgets.QFrame(Dialog)
#         self.SentiFrame.setGeometry(QtCore.QRect(750, 130, 311, 371))
#         self.SentiFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.SentiFrame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.SentiFrame.setObjectName("SentiFrame")
#         self.textEdit_3 = QtWidgets.QTextEdit(self.SentiFrame)
#         self.textEdit_3.setGeometry(QtCore.QRect(10, 70, 291, 251))
#         self.textEdit_3.setAutoFillBackground(False)
#         self.textEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
#         self.textEdit_3.setFrameShadow(QtWidgets.QFrame.Sunken)
#         self.textEdit_3.setLineWidth(5)
#         self.textEdit_3.setObjectName("textEdit_3")
#         self.linguisticlaunch = QtWidgets.QPushButton(self.SentiFrame)
#         self.linguisticlaunch.setGeometry(QtCore.QRect(172, 330, 131, 28))
#         self.linguisticlaunch.setStyleSheet("background-color: rgb(189, 192, 234);")
#         self.linguisticlaunch.setObjectName("linguisticlaunch")
#         self.radioButton_2 = QtWidgets.QRadioButton(self.SentiFrame)
#         self.radioButton_2.setGeometry(QtCore.QRect(10, 330, 95, 20))
#         self.radioButton_2.setStyleSheet("color: rgb(172, 196, 252);")
#         self.radioButton_2.setObjectName("radioButton_2")
#         self.label_3 = QtWidgets.QLabel(self.SentiFrame)
#         self.label_3.setGeometry(QtCore.QRect(10, 20, 211, 41))
#         font = QtGui.QFont()
#         font.setPointSize(15)
#         self.label_3.setFont(font)
#         self.label_3.setStyleSheet("color: rgb(172, 196, 252);")
#         self.label_3.setObjectName("label_3")
#         self.tableframe = QtWidgets.QFrame(Dialog)
#         self.tableframe.setGeometry(QtCore.QRect(30, 570, 651, 231))
#         self.tableframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.tableframe.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.tableframe.setLineWidth(5)
#         self.tableframe.setObjectName("tableframe")
#         self.label_4 = QtWidgets.QLabel(Dialog)
#         self.label_4.setGeometry(QtCore.QRect(20, 10, 231, 41))
#         font = QtGui.QFont()
#         font.setPointSize(15)
#         self.label_4.setFont(font)
#         self.label_4.setStyleSheet("color: rgb(172, 196, 252);")
#         self.label_4.setObjectName("label_4")
#         self.label_5 = QtWidgets.QLabel(Dialog)
#         self.label_5.setGeometry(QtCore.QRect(20, 60, 231, 41))
#         font = QtGui.QFont()
#         font.setPointSize(15)
#         self.label_5.setFont(font)
#         self.label_5.setStyleSheet("color: rgb(172, 196, 252);")
#         self.label_5.setObjectName("label_5")
#         self.candiname = QtWidgets.QLineEdit(Dialog)
#         self.candiname.setGeometry(QtCore.QRect(220, 21, 551, 31))
#         self.candiname.setStyleSheet("background-color: rgb(255, 255, 255);")
#         self.candiname.setObjectName("candiname")
#         self.candiid = QtWidgets.QLineEdit(Dialog)
#         self.candiid.setGeometry(QtCore.QRect(220, 70, 551, 31))
#         self.candiid.setStyleSheet("background-color: rgb(255, 255, 255);")
#         self.candiid.setObjectName("candiid")
#         self.startbutton = QtWidgets.QPushButton(Dialog)
#         self.startbutton.setGeometry(QtCore.QRect(840, 20, 93, 28))
#         self.startbutton.setStyleSheet("background-color: rgb(189, 192, 234);")
#         self.startbutton.setObjectName("startbutton")
#         self.reportbutton = QtWidgets.QPushButton(Dialog)
#         self.reportbutton.setGeometry(QtCore.QRect(840, 70, 93, 28))
#         self.reportbutton.setStyleSheet("background-color: rgb(189, 192, 234);")
#         self.reportbutton.setObjectName("reportbutton")
#         self.label_6 = QtWidgets.QLabel(Dialog)
#         self.label_6.setGeometry(QtCore.QRect(30, 520, 371, 41))
#         font = QtGui.QFont()
#         font.setPointSize(15)
#         self.label_6.setFont(font)
#         self.label_6.setStyleSheet("color: rgb(172, 196, 252);")
#         self.label_6.setObjectName("label_6")
#         self.label_7 = QtWidgets.QLabel(Dialog)
#         self.label_7.setGeometry(QtCore.QRect(710, 520, 371, 41))
#         font = QtGui.QFont()
#         font.setPointSize(15)
#         self.label_7.setFont(font)
#         self.label_7.setStyleSheet("color: rgb(172, 196, 252);")
#         self.label_7.setObjectName("label_7")
#         self.currentscoreframe = QtWidgets.QFrame(Dialog)
#         self.currentscoreframe.setGeometry(QtCore.QRect(710, 570, 371, 231))
#         font = QtGui.QFont()
#         font.setPointSize(8)
#         self.currentscoreframe.setFont(font)
#         self.currentscoreframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.currentscoreframe.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.currentscoreframe.setObjectName("currentscoreframe")
#         self.curscore = QtWidgets.QLabel(self.currentscoreframe)
#         self.curscore.setGeometry(QtCore.QRect(40, 60, 301, 101))
#         font = QtGui.QFont()
#         font.setPointSize(50)
#         self.curscore.setFont(font)
#         self.curscore.setStyleSheet("color: rgb(31, 226, 194);")
#         self.curscore.setObjectName("curscore")
#         self.resetdb = QtWidgets.QPushButton(Dialog)
#         self.resetdb.setGeometry(QtCore.QRect(960, 20, 101, 28))
#         self.resetdb.setStyleSheet("background-color: rgb(189, 192, 234);")
#         self.resetdb.setObjectName("resetdb")
#         self.savereport = QtWidgets.QPushButton(Dialog)
#         self.savereport.setGeometry(QtCore.QRect(960, 70, 101, 28))
#         self.savereport.setStyleSheet("background-color: rgb(189, 192, 234);")
#         self.savereport.setObjectName("savereport")
#         self.label_8 = QtWidgets.QLabel(Dialog)
#         self.label_8.setGeometry(QtCore.QRect(1110, 150, 211, 41))
#         font = QtGui.QFont()
#         font.setPointSize(15)
#         self.label_8.setFont(font)
#         self.label_8.setStyleSheet("color: rgb(172, 196, 252);")
#         self.label_8.setObjectName("label_8")
#         self.qbox = QtWidgets.QTextEdit(Dialog)
#         self.qbox.setGeometry(QtCore.QRect(1110, 200, 671, 171))
#         font = QtGui.QFont()
#         font.setPointSize(24)
#         self.qbox.setFont(font)
#         self.qbox.setAutoFillBackground(False)
#         self.qbox.setStyleSheet("background-color: rgb(255, 255, 255);")
#         self.qbox.setFrameShadow(QtWidgets.QFrame.Sunken)
#         self.qbox.setLineWidth(5)
#         self.qbox.setObjectName("qbox")
#         self.label_9 = QtWidgets.QLabel(Dialog)
#         self.label_9.setGeometry(QtCore.QRect(1110, 390, 211, 41))
#         font = QtGui.QFont()
#         font.setPointSize(15)
#         self.label_9.setFont(font)
#         self.label_9.setStyleSheet("color: rgb(172, 196, 252);")
#         self.label_9.setObjectName("label_9")
#         self.rbox = QtWidgets.QTextEdit(Dialog)
#         self.rbox.setGeometry(QtCore.QRect(1110, 440, 671, 171))
#         font = QtGui.QFont()
#         font.setPointSize(24)
#         self.rbox.setFont(font)
#         self.rbox.setAutoFillBackground(False)
#         self.rbox.setStyleSheet("background-color: rgb(255, 255, 255);")
#         self.rbox.setFrameShadow(QtWidgets.QFrame.Sunken)
#         self.rbox.setLineWidth(5)
#         self.rbox.setObjectName("rbox")
#         self.label_10 = QtWidgets.QLabel(Dialog)
#         self.label_10.setGeometry(QtCore.QRect(1340, 40, 261, 51))
#         font = QtGui.QFont()
#         font.setPointSize(26)
#         self.label_10.setFont(font)
#         self.label_10.setStyleSheet("color: rgb(172, 196, 252);")
#         self.label_10.setObjectName("label_10")
#         self.label_11 = QtWidgets.QLabel(Dialog)
#         self.label_11.setGeometry(QtCore.QRect(1110, 630, 371, 41))
#         font = QtGui.QFont()
#         font.setPointSize(15)
#         self.label_11.setFont(font)
#         self.label_11.setStyleSheet("color: rgb(172, 196, 252);")
#         self.label_11.setObjectName("label_11")
#         self.resumeselect = QtWidgets.QPushButton(Dialog)
#         self.resumeselect.setGeometry(QtCore.QRect(1280, 700, 301, 91))
#         font = QtGui.QFont()
#         font.setPointSize(15)
#         self.resumeselect.setFont(font)
#         self.resumeselect.setStyleSheet("background-color: rgb(189, 192, 234);")
#         self.resumeselect.setObjectName("resumeselect")
#         self.table=QtWidgets.QTableWidget(self.tableframe)
#         self.table.setFixedWidth(650)
#         self.table.setFixedHeight(300)
#         self.table.setAlternatingRowColors(True)
#
#         self.retranslateUi(Dialog)
#         QtCore.QMetaObject.connectSlotsByName(Dialog)
#
#     def retranslateUi(self, Dialog):
#         _translate = QtCore.QCoreApplication.translate
#         Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
#         self.label.setText(_translate("Dialog", "Face Analysis Status:"))
#         self.facelaunch.setText(_translate("Dialog", "launch seprately"))
#         self.voicetonelaunch.setText(_translate("Dialog", "launch seprately"))
#         self.radioButton.setText(_translate("Dialog", "selected"))
#         self.label_2.setText(_translate("Dialog", "Voice Tone Analysis:"))
#         self.linguisticlaunch.setText(_translate("Dialog", "launch seperately"))
#         self.radioButton_2.setText(_translate("Dialog", "selected"))
#         self.label_3.setText(_translate("Dialog", "Linguistic Analysis:"))
#         self.label_4.setText(_translate("Dialog", "Candidate name:"))
#         self.label_5.setText(_translate("Dialog", "Candidate ID:"))
#         self.startbutton.setText(_translate("Dialog", "Start Session"))
#         self.reportbutton.setText(_translate("Dialog", "Get Report"))
#         self.label_6.setText(_translate("Dialog", "Previous Candidates Score Table:"))
#         self.label_7.setText(_translate("Dialog", "Current Candidate Score:"))
#         self.curscore.setText(_translate("Dialog", "0.00%"))
#         self.resetdb.setText(_translate("Dialog", "Reset Database"))
#         self.savereport.setText(_translate("Dialog", "Save Report"))
#         self.label_8.setText(_translate("Dialog", "Question:"))
#         self.label_9.setText(_translate("Dialog", "Response:"))
#         self.label_10.setText(_translate("Dialog", "Questionaire"))
#         self.label_11.setText(_translate("Dialog", "Upload Candidate Resume:"))
#         self.resumeselect.setText(_translate("Dialog", "Select  Resume file"))
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1803, 848)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".designer/backup/Downloads/1076441.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color: rgb(34, 63, 116);")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1811, 851))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.mainview = QtWidgets.QWidget()
        self.mainview.setObjectName("mainview")
        self.reportbutton = QtWidgets.QPushButton(self.mainview)
        self.reportbutton.setGeometry(QtCore.QRect(830, 69, 93, 28))
        self.reportbutton.setStyleSheet("background-color: rgb(189, 192, 234);")
        self.reportbutton.setObjectName("reportbutton")
        self.label_7 = QtWidgets.QLabel(self.mainview)
        self.label_7.setGeometry(QtCore.QRect(700, 519, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(172, 196, 252);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.mainview)
        self.label_8.setGeometry(QtCore.QRect(1100, 149, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(172, 196, 252);")
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(self.mainview)
        self.label_10.setGeometry(QtCore.QRect(1330, 39, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(172, 196, 252);")
        self.label_10.setObjectName("label_10")
        self.label_6 = QtWidgets.QLabel(self.mainview)
        self.label_6.setGeometry(QtCore.QRect(20, 519, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(172, 196, 252);")
        self.label_6.setObjectName("label_6")
        self.label_11 = QtWidgets.QLabel(self.mainview)
        self.label_11.setGeometry(QtCore.QRect(1100, 629, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(172, 196, 252);")
        self.label_11.setObjectName("label_11")
        self.resetdb = QtWidgets.QPushButton(self.mainview)
        self.resetdb.setGeometry(QtCore.QRect(950, 19, 101, 28))
        self.resetdb.setStyleSheet("background-color: rgb(189, 192, 234);")
        self.resetdb.setObjectName("resetdb")
        self.candiid = QtWidgets.QLineEdit(self.mainview)
        self.candiid.setGeometry(QtCore.QRect(210, 69, 551, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.candiid.setFont(font)
        self.candiid.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.candiid.setObjectName("candiid")
        self.label_5 = QtWidgets.QLabel(self.mainview)
        self.label_5.setGeometry(QtCore.QRect(10, 59, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(172, 196, 252);")
        self.label_5.setObjectName("label_5")
        self.FaceFrame = QtWidgets.QFrame(self.mainview)
        self.FaceFrame.setGeometry(QtCore.QRect(20, 129, 311, 371))
        self.FaceFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FaceFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FaceFrame.setObjectName("FaceFrame")
        self.textEdit_4 = QtWidgets.QTextEdit(self.FaceFrame)
        self.textEdit_4.setGeometry(QtCore.QRect(10, 70, 291, 251))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_4.setFont(font)
        self.textEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_4.setObjectName("textEdit_4")
        self.label_4 = QtWidgets.QLabel(self.FaceFrame)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(172, 196, 252);")
        self.label_4.setObjectName("label_4")
        self.facelaunch = QtWidgets.QPushButton(self.FaceFrame)
        self.facelaunch.setGeometry(QtCore.QRect(170, 330, 131, 28))
        self.facelaunch.setStyleSheet("background-color: rgb(189, 192, 234);")
        self.facelaunch.setObjectName("facelaunch_2")
        self.rbox = QtWidgets.QTextEdit(self.mainview)
        self.rbox.setGeometry(QtCore.QRect(1100, 439, 671, 171))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.rbox.setFont(font)
        self.rbox.setAutoFillBackground(False)
        self.rbox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.rbox.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.rbox.setLineWidth(5)
        self.rbox.setObjectName("rbox")
        self.label_9 = QtWidgets.QLabel(self.mainview)
        self.label_9.setGeometry(QtCore.QRect(1100, 389, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(172, 196, 252);")
        self.label_9.setObjectName("label_9")
        self.savereport = QtWidgets.QPushButton(self.mainview)
        self.savereport.setGeometry(QtCore.QRect(950, 69, 101, 28))
        self.savereport.setStyleSheet("background-color: rgb(189, 192, 234);")
        self.savereport.setObjectName("savereport")
        self.resumeselect = QtWidgets.QPushButton(self.mainview)
        self.resumeselect.setGeometry(QtCore.QRect(1270, 699, 301, 91))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.resumeselect.setFont(font)
        self.resumeselect.setStyleSheet("background-color: rgb(189, 192, 234);")
        self.resumeselect.setObjectName("resumeselect")
        self.currentscoreframe = QtWidgets.QFrame(self.mainview)
        self.currentscoreframe.setGeometry(QtCore.QRect(700, 569, 371, 231))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.currentscoreframe.setFont(font)
        self.currentscoreframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.currentscoreframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.currentscoreframe.setObjectName("currentscoreframe")
        self.curscore = QtWidgets.QLabel(self.currentscoreframe)
        self.curscore.setGeometry(QtCore.QRect(40, 60, 301, 101))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.curscore.setFont(font)
        self.curscore.setStyleSheet("color: rgb(31, 226, 194);")
        self.curscore.setObjectName("curscore_2")
        self.VoiceFrame = QtWidgets.QFrame(self.mainview)
        self.VoiceFrame.setGeometry(QtCore.QRect(370, 129, 331, 371))
        self.VoiceFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.VoiceFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.VoiceFrame.setObjectName("VoiceFrame")
        self.textEdit_5 = QtWidgets.QTextEdit(self.VoiceFrame)
        self.textEdit_5.setGeometry(QtCore.QRect(20, 70, 291, 251))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_5.setFont(font)
        self.textEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_5.setObjectName("textEdit_5")
        self.voicetonelaunch = QtWidgets.QPushButton(self.VoiceFrame)
        self.voicetonelaunch.setGeometry(QtCore.QRect(182, 330, 131, 28))
        self.voicetonelaunch.setStyleSheet("background-color: rgb(189, 192, 234);")
        self.voicetonelaunch.setObjectName("voicetonelaunch_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.VoiceFrame)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 330, 95, 20))
        self.radioButton_3.setStyleSheet("color: rgb(172, 196, 252);")
        self.radioButton_3.setObjectName("radioButton_3")
        self.label_12 = QtWidgets.QLabel(self.VoiceFrame)
        self.label_12.setGeometry(QtCore.QRect(20, 20, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(172, 196, 252);")
        self.label_12.setObjectName("label_12")
        self.SentiFrame = QtWidgets.QFrame(self.mainview)
        self.SentiFrame.setGeometry(QtCore.QRect(740, 129, 311, 371))
        self.SentiFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SentiFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SentiFrame.setObjectName("SentiFrame")
        self.textEdit_6 = QtWidgets.QTextEdit(self.SentiFrame)
        self.textEdit_6.setGeometry(QtCore.QRect(10, 70, 291, 251))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_6.setFont(font)
        self.textEdit_6.setAutoFillBackground(False)
        self.textEdit_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textEdit_6.setLineWidth(5)
        self.textEdit_6.setObjectName("textEdit_6")
        self.linguisticlaunch_2 = QtWidgets.QPushButton(self.SentiFrame)
        self.linguisticlaunch_2.setGeometry(QtCore.QRect(172, 330, 131, 28))
        self.linguisticlaunch_2.setStyleSheet("background-color: rgb(189, 192, 234);")
        self.linguisticlaunch_2.setObjectName("linguisticlaunch_2")
        self.radioButton_4 = QtWidgets.QRadioButton(self.SentiFrame)
        self.radioButton_4.setGeometry(QtCore.QRect(10, 330, 95, 20))
        self.radioButton_4.setStyleSheet("color: rgb(172, 196, 252);")
        self.radioButton_4.setObjectName("radioButton_4")
        self.label_13 = QtWidgets.QLabel(self.SentiFrame)
        self.label_13.setGeometry(QtCore.QRect(10, 20, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(172, 196, 252);")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.mainview)
        self.label_14.setGeometry(QtCore.QRect(10, 9, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(172, 196, 252);")
        self.label_14.setObjectName("label_14")
        self.tableframe = QtWidgets.QFrame(self.mainview)
        self.tableframe.setGeometry(QtCore.QRect(20, 569, 651, 231))
        self.tableframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tableframe.setLineWidth(5)
        self.tableframe.setObjectName("tableframe")
        self.startbutton = QtWidgets.QPushButton(self.mainview)
        self.startbutton.setGeometry(QtCore.QRect(830, 19, 93, 28))
        self.startbutton.setStyleSheet("background-color: rgb(189, 192, 234);")
        self.startbutton.setObjectName("startbutton")
        self.qbox = QtWidgets.QTextEdit(self.mainview)
        self.qbox.setGeometry(QtCore.QRect(1100, 199, 671, 171))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.qbox.setFont(font)
        self.qbox.setAutoFillBackground(False)
        self.qbox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.qbox.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.qbox.setLineWidth(5)
        self.qbox.setObjectName("qbox")
        self.candiname = QtWidgets.QLineEdit(self.mainview)
        self.candiname.setGeometry(QtCore.QRect(210, 20, 551, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.candiname.setFont(font)
        self.candiname.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.candiname.setObjectName("candiname")
        self.tabWidget.addTab(self.mainview, "")
        self.personalitytab = QtWidgets.QWidget()
        self.personalitytab.setObjectName("personalitytab")
        self.label_23 = QtWidgets.QLabel(self.personalitytab)
        self.label_23.setGeometry(QtCore.QRect(40-25, 360+232, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color: rgb(172, 196, 252);")
        self.label_23.setObjectName("label_23")
        self.label_22 = QtWidgets.QLabel(self.personalitytab)
        self.label_22.setGeometry(QtCore.QRect(40-25, 280+232, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color: rgb(172, 196, 252);")
        self.label_22.setObjectName("label_22")
        self.label_21 = QtWidgets.QLabel(self.personalitytab)
        self.label_21.setGeometry(QtCore.QRect(40, 80, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color: rgb(172, 196, 252);")
        self.label_21.setObjectName("label_21")
        self.characterlabel = QtWidgets.QLabel(self.personalitytab)
        self.characterlabel.setGeometry(QtCore.QRect(80-60, 140, 671+1100, 111+250)) # create a new dataset to be resized to this dimesions 1771x361
        font = QtGui.QFont()
        font.setPointSize(15)
        self.characterlabel.setFont(font)
        self.characterlabel.setStyleSheet("color: rgb(172, 196, 252);")
        self.characterlabel.setObjectName("characterlabel")
        # self.webviewinsert = QtWidgets.QGraphicsView(self.personalitytab)
        # self.webviewinsert.setGeometry(QtCore.QRect(860, 110, 911, 691))
        # self.webviewinsert.setObjectName("webviewinsert")
        self.label_24 = QtWidgets.QLabel(self.personalitytab)
        self.label_24.setGeometry(QtCore.QRect(1020-450, 30-20, 661, 61)) #1020
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("color: rgb(172, 196, 252);")
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.personalitytab)
        self.label_25.setGeometry(QtCore.QRect(40+850+20, 520, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("color: rgb(172, 196, 252);")
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.personalitytab)
        self.label_26.setGeometry(QtCore.QRect(40-25, 440+232, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("color: rgb(172, 196, 252);")
        self.label_26.setObjectName("label_26")
        # self.label_27 = QtWidgets.QLabel(self.personalitytab)
        # self.label_27.setGeometry(QtCore.QRect(230+850+20, 10, 450, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        # self.label_27.setFont(font)
        # self.label_27.setStyleSheet("color: rgb(172, 196, 252);")
        # self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.personalitytab)
        self.label_28.setGeometry(QtCore.QRect(40+850+20, 600, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("color: rgb(172, 196, 252);")
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.personalitytab)
        self.label_29.setGeometry(QtCore.QRect(40+850+20, 680, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("color: rgb(172, 196, 252);")
        self.label_29.setObjectName("label_29")
        self.interaction = QtWidgets.QLabel(self.personalitytab)
        self.interaction.setGeometry(QtCore.QRect(480-25, 280+232, 450, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.interaction.setFont(font)
        self.interaction.setStyleSheet("color: rgb(172, 196, 252);")
        self.interaction.setObjectName("interaction")
        self.intelligence = QtWidgets.QLabel(self.personalitytab)
        self.intelligence.setGeometry(QtCore.QRect(480-25, 360+232, 450, 31)) # 221
        font = QtGui.QFont()
        font.setPointSize(15)
        self.intelligence.setFont(font)
        self.intelligence.setStyleSheet("color: rgb(172, 196, 252);")
        self.intelligence.setObjectName("intelligence")
        self.strength = QtWidgets.QLabel(self.personalitytab)
        self.strength.setGeometry(QtCore.QRect(480-25, 440+232, 450, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.strength.setFont(font)
        self.strength.setStyleSheet("color: rgb(172, 196, 252);")
        self.strength.setObjectName("strength")
        self.weakness = QtWidgets.QLabel(self.personalitytab)
        self.weakness.setGeometry(QtCore.QRect(480+850+20, 520, 450, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.weakness.setFont(font)
        self.weakness.setStyleSheet("color: rgb(172, 196, 252);")
        self.weakness.setObjectName("weakness")
        self.career = QtWidgets.QLabel(self.personalitytab)
        self.career.setGeometry(QtCore.QRect(480+850+20, 600, 450, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.career.setFont(font)
        self.career.setStyleSheet("color: rgb(172, 196, 252);")
        self.career.setObjectName("career")
        self.famous = QtWidgets.QLabel(self.personalitytab)
        self.famous.setGeometry(QtCore.QRect(480+850+20, 680, 450, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.famous.setFont(font)
        self.famous.setStyleSheet("color: rgb(172, 196, 252);")
        self.famous.setObjectName("famous")
        self.tabWidget.addTab(self.personalitytab, "")
        self.questioneditview = QtWidgets.QWidget()
        self.questioneditview.setObjectName("questioneditview")
        self.quesprev = QtWidgets.QTableWidget(self.questioneditview) #self.quesprev = QtWidgets.QFrame(self.questioneditview)
        self.quesprev.setGeometry(QtCore.QRect(1050, 120, 711, 671))
        # self.quesprev.setStyleSheet("background-color: rgb(255, 255, 255);") 3 commmenting to try to get default style sheet
        self.quesprev.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.quesprev.setFrameShadow(QtWidgets.QFrame.Raised)
        self.quesprev.setLineWidth(5)
        self.quesprev.setObjectName("quesprev")
        self.quesprev.setAlternatingRowColors(True) # manually added
        self.label_15 = QtWidgets.QLabel(self.questioneditview)
        self.label_15.setGeometry(QtCore.QRect(1240, 40, 491, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(172, 196, 252);")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.questioneditview)
        self.label_16.setGeometry(QtCore.QRect(60, 80, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgb(172, 196, 252);")
        self.label_16.setObjectName("label_16")
        self.questionadd = QtWidgets.QLineEdit(self.questioneditview)
        self.questionadd.setGeometry(QtCore.QRect(420, 80, 551, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.questionadd.setFont(font)
        self.questionadd.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.questionadd.setObjectName("questionadd")
        self.label_17 = QtWidgets.QLabel(self.questioneditview)
        self.label_17.setGeometry(QtCore.QRect(330, 20, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(172, 196, 252);")
        self.label_17.setObjectName("label_17")
        self.desc = QtWidgets.QTextEdit(self.questioneditview)
        self.desc.setGeometry(QtCore.QRect(420, 140, 551, 111))
        self.desc.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.desc.setObjectName("desc")
        self.label_19 = QtWidgets.QLabel(self.questioneditview)
        self.label_19.setGeometry(QtCore.QRect(60, 150, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: rgb(172, 196, 252);")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.questioneditview)
        self.label_20.setGeometry(QtCore.QRect(60, 300, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: rgb(172, 196, 252);")
        self.label_20.setObjectName("label_20")
        self.comboBox = QtWidgets.QComboBox(self.questioneditview)
        self.comboBox.setGeometry(QtCore.QRect(420, 310, 111, 22))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.preloadbtn = QtWidgets.QPushButton(self.questioneditview)
        self.preloadbtn.setGeometry(QtCore.QRect(580, 300, 171, 41))
        self.preloadbtn.setStyleSheet("background-color: rgb(189, 192, 234);")
        self.preloadbtn.setObjectName("preloadbtn")
        self.tabWidget.addTab(self.questioneditview, "")
        self.settings = QtWidgets.QWidget()
        self.settings.setObjectName("settings")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.settings)
        self.plainTextEdit.setEnabled(False)
        self.plainTextEdit.setGeometry(QtCore.QRect(1000, 90, 781, 711))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet("color: rgb(172, 196, 252);")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.horizontalSlider = QtWidgets.QSlider(self.settings)
        self.horizontalSlider.setGeometry(QtCore.QRect(380, 330, 361, 21))
        self.horizontalSlider.setMinimum(1000)
        self.horizontalSlider.setMaximum(5000)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.noisethreshold = QtWidgets.QSpinBox(self.settings)
        self.noisethreshold.setGeometry(QtCore.QRect(760, 330, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.noisethreshold.setFont(font)
        self.noisethreshold.setStyleSheet("color: rgb(172, 196, 252);")
        self.noisethreshold.setMinimum(1000)
        self.noisethreshold.setMaximum(5000)
        self.noisethreshold.setObjectName("noisethreshold")
        self.label_36 = QtWidgets.QLabel(self.settings)
        self.label_36.setGeometry(QtCore.QRect(90, 320, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("color: rgb(172, 196, 252);")
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.settings)
        self.label_37.setGeometry(QtCore.QRect(410, 30, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_37.setFont(font)
        self.label_37.setStyleSheet("color: rgb(172, 196, 252);")
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.settings)
        self.label_38.setGeometry(QtCore.QRect(1000, 20, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_38.setFont(font)
        self.label_38.setStyleSheet("color: rgb(172, 196, 252);")
        self.label_38.setObjectName("label_38")
        self.testmicbtn = QtWidgets.QPushButton(self.settings)
        self.testmicbtn.setGeometry(QtCore.QRect(380, 390, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.testmicbtn.setFont(font)
        self.testmicbtn.setStyleSheet("background-color: rgb(189, 192, 234);")
        self.testmicbtn.setObjectName("pushButton")
        self.tabWidget.addTab(self.settings, "")
        self.table = QtWidgets.QTableWidget(self.tableframe)
        self.table.setFixedWidth(650)
        self.table.setFixedHeight(300)
        self.table.setAlternatingRowColors(True)
        # self.table.setHorizontalHeaderLabels("Id;Name;Fscore;Vscore;Lscore;Tscore".split(";"))
        # self.table.horizontalHeaderItem().setTextAlignment(PyQt5.QtCore.Qt.AlignHCenter) # not working
        # self.quesprev.setFixedHeight(1000)
        # self.quesprev.setFixedSize(4000,4000)
        # self.quesprev.setFixedWidth(2000)
        # none of them seem to adjustt the frame
        # im shit scared to edit the UI again
        # try to fix thee stuff in this same UI

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.noisethreshold.valueChanged['int'].connect(self.horizontalSlider.setValue)
        self.horizontalSlider.valueChanged['int'].connect(self.noisethreshold.setValue)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "AI Hiring System"))
        self.reportbutton.setText(_translate("Dialog", "Get Report"))
        self.label_7.setText(_translate("Dialog", "Current Candidate Score:"))
        self.label_8.setText(_translate("Dialog", "Question:"))
        self.label_10.setText(_translate("Dialog", "Questionaire"))
        self.label_6.setText(_translate("Dialog", "Previous Candidates Score Table:"))
        self.label_11.setText(_translate("Dialog", "Upload Candidate Resume:"))
        self.resetdb.setText(_translate("Dialog", "Reset Database"))
        self.label_5.setText(_translate("Dialog", "Candidate ID:"))
        self.label_4.setText(_translate("Dialog", "Face Analysis Status:"))
        self.facelaunch.setText(_translate("Dialog", "launch seprately"))
        self.label_9.setText(_translate("Dialog", "Response:"))
        self.savereport.setText(_translate("Dialog", "Save Report"))
        self.resumeselect.setText(_translate("Dialog", "Select  Resume file"))
        self.curscore.setText(_translate("Dialog", "0.00%"))
        self.voicetonelaunch.setText(_translate("Dialog", "launch seprately"))
        self.radioButton_3.setText(_translate("Dialog", "selected"))
        self.label_12.setText(_translate("Dialog", "Voice Tone Analysis:"))
        self.linguisticlaunch_2.setText(_translate("Dialog", "launch seperately"))
        self.radioButton_4.setText(_translate("Dialog", "selected"))
        self.label_13.setText(_translate("Dialog", "Linguistic Analysis:"))
        self.label_14.setText(_translate("Dialog", "Candidate name:"))
        self.startbutton.setText(_translate("Dialog", "Start Session"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mainview), _translate("Dialog", "Candidate testing"))
        self.label_23.setText(_translate("Dialog", "Intelligence type                       :"))
        self.label_22.setText(_translate("Dialog", "Interaction type                        :"))
        self.label_21.setText(_translate("Dialog", "Character Code:"))
        self.characterlabel.setText(_translate("Dialog", "<--------------------No Image loaded----------------->"))
        self.label_24.setText(_translate("Dialog", "Detailed Personality Insight"))
        self.label_25.setText(_translate("Dialog", "Weakness                                :"))
        self.label_26.setText(_translate("Dialog", "Strength                                  :"))
        # self.label_27.setText(_translate("Dialog", "Quick Summary of Personality"))
        self.label_28.setText(_translate("Dialog", "Ideal Careers                            :"))
        self.label_29.setText(_translate("Dialog", "Famous personalities                 :"))
        self.interaction.setText(_translate("Dialog", "None"))
        self.intelligence.setText(_translate("Dialog", "None"))
        self.strength.setText(_translate("Dialog", "None"))
        self.weakness.setText(_translate("Dialog", "None"))
        self.career.setText(_translate("Dialog", "None"))
        self.famous.setText(_translate("Dialog", "None"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.personalitytab), _translate("Dialog", "Personality Analysis"))
        self.label_15.setText(_translate("Dialog", "Question preview"))
        self.label_16.setText(_translate("Dialog", "Question to add:"))
        self.label_17.setText(_translate("Dialog", "Edit Questions In database"))
        self.label_19.setText(_translate("Dialog", "Description of Question:"))
        self.label_20.setText(_translate("Dialog", "Weightage of Question:"))
        self.comboBox.setItemText(0, _translate("Dialog", "1"))
        self.comboBox.setItemText(1, _translate("Dialog", "2"))
        self.comboBox.setItemText(2, _translate("Dialog", "3"))
        self.comboBox.setItemText(3, _translate("Dialog", "4"))
        self.comboBox.setItemText(4, _translate("Dialog", "5"))
        self.comboBox.setItemText(5, _translate("Dialog", "6"))
        self.comboBox.setItemText(6, _translate("Dialog", "7"))
        self.comboBox.setItemText(7, _translate("Dialog", "8"))
        self.comboBox.setItemText(8, _translate("Dialog", "9"))
        self.comboBox.setItemText(9, _translate("Dialog", "10"))
        self.preloadbtn.setText(_translate("Dialog", "Pre-Load Questions"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.questioneditview), _translate("Dialog", "Question edit view"))
        self.plainTextEdit.setPlainText(_translate("Dialog", "About The App:\n"
"\n"
"1) This app is developed to create a new way of hiring process\n"
"2) This application is targeted to hirers with candidate count greater than 1000\n"
"3) Bulk Filtering method is applied in this application. Bulk Filtering is a process of cutting down ineligible candidates where the postings to applicants ratio is about 0.01 to 0.1\n"
"\n"
"Procedure for Usage:\n"
"\n"
"1) The Candidate must produce a E-Resume for the interview\n"
"2) The candidate is required to sit before the computer with face facing the camera\n"
"3) As soon as the candidate uploads his/her resume the session starts\n"
"4) The Session is a series of conversation between the canndidate and the E-Intervier \n"
"5) The candidate is required to answer to the E-Interviewer\'s Questions as accurately as possibble\n"
"6) At the end of the session the caandidate may take leave and the candidate\'s result will be evaluated*\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"*->result Evaluated might be inaccurate as the software is not completely finished\n"
""))
        self.label_36.setText(_translate("Dialog", "Noise Threshold:"))
        self.label_37.setText(_translate("Dialog", "Settings"))
        self.label_38.setText(_translate("Dialog", "Instructions:"))
        self.testmicbtn.setText(_translate("Dialog", "Test Microphone"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings), _translate("Dialog", "Settings and About"))

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#new ui end
###############################################################################################################
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox as QM, QPushButton,QInputDialog,QFileDialog
# mixer.init()

# from dialog import MyDialog

class AppWindow(QDialog, QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # declaration of class variables
        self.t = threading.Thread
        self.t1 = threading.Thread
        self.t2 = threading.Thread
        self.Cname = None # candidates's name
        self.Cid1 = None  # candidate's id
        self.msg = QM() # a global message box
        self.res_file=None # a file varibale to store the resume of the candidate
        self.resume_extract={}
        self.characterExtract=[]
        self.msg.StandardButtons(QM.Ok)
        self.character_code="INTP" # saves character code of the person default is set INTP chracter code
        self.response_array=[]
        self.writedata=""
        self.scorecopy=0
        self.file_set=False # a variable to check if the file of the candidate is preset or not for querying
        self.startbutton.clicked.connect(self.launchall)
        # self.startbutton.clicked.connect(self.fake_quesser)
        self.facelaunch.clicked.connect(self.Start_Face_Detect)
        self.voicetonelaunch.clicked.connect(self.Start_Tone_Detect)
        self.linguisticlaunch_2.clicked.connect(self.Start_Ligui_Detect)
        self.reportbutton.clicked.connect(self.get_values)
        self.resetdb.clicked.connect(self.clear_database)
        self.savereport.clicked.connect(self.generate_report_file)
        self.resumeselect.clicked.connect(self.select_resume_file)
        self.preloadbtn.clicked.connect(self.add_questions_to_base)
        self.testmicbtn.clicked.connect(self.test_mic)
        self.show_question_preview()
        self.show()

    @pyqtSlot()
    # complete all the below given functions
    # be careful at every step
    # lot of work ahead of you dude
    # work hard and gt the reward
    # lot of refactoring to do !!!!!!
    def load_character_img(self,img="INTP"):
        try:
            self.characterlabel.setPixmap(QtGui.QPixmap(f"character_code_images/{img}.jpg"))
        except:
            print('error occured : '+traceback.print_exc())

    def test_mic(self):
        self.noise_threshold_adjust()
        sample_check()
        print('Checking was over and current threshold value is',dtV.THRESHOLD)

    def set_personality_analysis(self):
        guess_code=""
        chck=self.response_array[2:] # slices the response of the first question as they are causal questions and not needed
        # chck=["no","yes","no","yes","yes","no","yes","yes"] # just for checking purposes
        if chck[:2]==["yes","yes"]:
            guess_code+="I"
        else:
            guess_code+="E"
        if chck[2:4] == ["yes", "yes"]:
            guess_code += "N"
        else:
            guess_code += "S"
        if chck[4:6] == ["yes", "yes"]:
            guess_code += "T"
        else:
            guess_code += "F"
        if chck[6:8] == ["yes", "yes"]:
            guess_code += "P"
        else:
            guess_code += "J"
        # print(guess_code)  # the code is working I checked it in the terminal
        self.character_code=guess_code
        det=fetch_character_details(guess_code)
        self.intelligence.setText(det[1])
        self.interaction.setText(det[2])
        self.strength.setText(det[3])
        self.weakness.setText(det[4])
        self.career.setText(det[5])
        self.famous.setText(det[6])
        self.load_character_img(guess_code)
        # self.load_character_img("ENFJB")

    def add_questions_to_base(self):
        # writinng the questions to the base
        ques=self.questionadd.text()
        wt=int(self.comboBox.currentText())
        des=self.desc.toPlainText()
        if None in (ques,wt,des):
            self.msg.setWindowTitle("All values not filled")
            self.msg.setText("Please fill in all the values to add question to the database")
            self.msg.exec()
            return
        else:
            write_question_to_base(ques,wt,des)
            # preloading the questions
            preload_questions()
            self.msg.setWindowTitle("Write and Preload done")
            self.msg.setText("The question was written and preloading was done!")
            self.msg.exec()

    def load_web_view(self):
        pass

    def show_question_preview(self):
        self.response_array=["no","yes","yes","yes","no","no","no","no"] # the testing was a success and cool almost done for the day
        self.set_personality_analysis() # dont call this before calling the launch all function call only for test purposes
        ques=get_all_ques_values()
        self.quesprev.setColumnCount(3)
        self.quesprev.setRowCount(0)
        rowpos = self.quesprev.rowCount()
        # add the title code here
        # self.table.insertRow(rowpos)
        for x in range(len(ques)):
            self.quesprev.insertRow(rowpos)
            for y in range(len(ques[x])):
                self.quesprev.setItem(rowpos, y, QtWidgets.QTableWidgetItem(f'{ques[x][y]}'))
            rowpos += 1

    def noise_threshold_adjust(self):
        thresh=self.horizontalSlider.value()
        print(thresh)
        change_threshold(int(thresh))
        # updating the last threshold value
        try:
            f = open('last_threshold.txt', 'w')
            f.write(str(thresh))
        except:
            print('Some error occured setting threshold to 2500')
            f.write(f'{2500}')
        finally:
            f.close()

    def clear_database(self):
        clear_db()
        print('database has been reset')

    def get_resume_extract(self):
        return(self.resume_extract)

    def analyse_resume(self):
        self.res_file.readline() # omitting the title line of the resume
        for x in self.res_file.readlines(): # reading all the otheer lines in the resume
            lis1=x.split(':')                    # I think this syntax is unneccssary
            if len(lis1)==2:
                self.resume_extract[lis1[0]]=lis1[1]
            # the lis1[0] is a mapped value of strings can be like
            # reading,writing,swimming etc so write code to manage that functionality
        #preloads the resume questions audio
        print("please wait a few secs to load and analyse the given resume",f"\n{self.resume_extract}")
        # preload_resume_questions(self.resume_extract) #  expected to inpput as dicct but input is a lisyt? how uncomment this line
        print(self.resume_extract)

    def select_resume_file(self):
        file_name,j=QFileDialog.getOpenFileName(self,'Open File','/home') # a tuple is returned hence the value of j is self value which is not needed
        if file_name.endswith('txt') or file_name.endswith('docx') or file_name.endswith('doc'):
            self.file_set=True
            print('File read okay')
            self.res_file=open(file_name,'r')
            print(self.res_file.readlines())
            self.res_file.seek(0) # readlines functions places the file pointer at the end of the file so a seek operatio
            self.analyse_resume()
        else:
            self.msg.setWindowTitle('Unsupported format error')
            self.msg.setText('The file format is not supported please upload supported format')
            self.msg.exec()
            self.file_set=False

# try to tigify this funtion its looks so messy
    def quesser(self,read):
        val2=1
        chk_array=["yeah","yea","yes","yep","i do"]
        for x in read:
            self.qbox.append(x[0])
            playsound(f'sentences_folder\\sentence-{val2}.mp3')
            val2+=1
            time.sleep(2)
            fg=0
            try:
                user_reply=recog_save()
                self.rbox.append(user_reply)
                perform_analysis(user_reply) # this works
                for x in chk_array:
                    if x in user_reply:
                        self.response_array.append("yes")
                        fg=1
                        break
                if fg!=1:
                    self.response_array.append("no")
                # self.qbox.append(self.bot_reply(user_reply))
                # try to add the chat response to this area or add some random messages here sounds good?
                # fetching all question names from the resume_questions folder
                # resumeques=os.listdir("sentences_folder\\resume_questions") # this piece of shit is uneccssarry
                cnt=1
                print("reached at  top of resume ques")
                resumeques=fetch_resume_questions()
                print(resumeques)
                playsound('sentences_folder\\sentence-resume.mp3')
                self.qbox.append("Now let's take a look at your resume")
                for x in resumeques:
                    self.qbox.append(x)
                    playsound(f'sentences_folder\\resume_questions\\resume-{cnt}.mp3')
                    cnt+=1
                    time.sleep(2)
                    user_reply=recog_save()
                    self.rbox.append(user_reply)
                    perform_analysis(user_reply)
                    # check the above block of code for wokring from the resume
            except:
                self.rbox.append("---No Reply---")
        self.qbox.append("Thank you , We'll get Back to you later")
        try:
            playsound('sentences_folder\\sentence-end.mp3')
            self.set_personality_analysis()
        except:
            print('Playing sound was not succesfull')
        finally:
            self.writedata=''
            self.writedata+='\t\tConversation Log of interview \n'
            bottalk=self.qbox.toPlainText().split('\n')
            cantalk=self.rbox.toPlainText().split('\n')
            try:
                for x in range(len(bottalk)):
                    self.writedata += (f'Bot:\t{bottalk[x]}\n')
                    self.writedata += (f'Candidate({self.Cname}):\t{cantalk[x]}\n')
            except:
                print('Error while trying to write the data to file')
            finally:
                self.writedata+= '-' * 20
                print("Quesser thread has Finsihed it's work")

    def generate_report_file(self):
        self.writedata+="\n\t\tPersonality Analysis"
        for x in self.characterExtract:
            self.writedata+=(x+"\n")
        print(self.writedata+"\n\nJust before the write operation")
        write_report(self.Cname,self.writedata)
        self.msg.setText("Report Generated and saved to local drive")
        self.msg.exec()

    def bot_reply(self,instring):
        val=chatgui.chatbot_response(instring)
        return val

    def launchall(self):
        self.writedata=None
        self.Cname = self.candiname.text()
        self.Cid = self.candiid.text()
        print(f"Cname is |{self.Cname}| and Cid is |{self.Cid}|")
        if self.Cname==None or len(self.Cname)<=0 or self.Cid==None or len(self.Cid)<=0:
            self.msg.setWindowTitle("No name Error")
            self.msg.setText("Please Enter a Candidate Name and ID to Start Session")
            self.msg.exec()
            return None

        if self.file_set==False:
            self.msg.setWindowTitle("No Resume uploaded")
            self.msg.setText("Please Upload Resume to start Session")
            self.msg.exec()
            return None

        self.msg.setWindowTitle('Please Wait')
        self.msg.setText('Starting the session please wait a few seconds')
        self.msg.exec()

        print('3 second delay to get Ready') # this delay is to get the user ready for the session
        time.sleep(3) # delay time is three seconds So start and wait for three seconds for the process to begin
        t = threading.Thread(target=rsfe)
        quesset=get_all_questions() # fetching all the questions from the database into the quesset variable
        t3 =threading.Thread(target=self.quesser,args=(quesset,)) # check this line
        t.start()
        t3.start()
        # clearing Session specific variables
        self.character_code=''
        self.candiname.setText('')
        self.candiid.setText('')
        self.file_set=False
        self.resume_extract={}
        self.res_file=None
        self.set_personality_analysis()
        self.characterExtract=[]
        clear_resume_ques() # check this line too

    def Start_Tone_Detect(self):
        t = threading.Thread(target=rsdt)
        t.start()
        t.join()
        detResult = dtV.get_detected()
        self.textEdit_5.setText(f'The analysed voice Tone {detResult}')
        # self.textEdit_3.setText(f'{detectedResult}'))

    def Start_Ligui_Detect(self):
        t1 = threading.Thread(target=rsvs)
        t1.start()
        # print(chatgui.chatbot_response('hello'))
        # self.textEdit.setText(f'positive={pos} and negative={neg}')

    def Start_Face_Detect(self):
        t = threading.Thread(target=rsfe)
        t.start()

    def stop_all_threads(self):
        # i just ran into ann interesting error my pc suddenly hung and gave me a THREAD_STUCK_IN_DEVICE_DRIVER error and got restarted
        # i figured out that the thing is due to the un stopped threads i created in the program's exeution
        # so finish this function and kill all the threads after programs
        # i just looked up how to kill thread...............WE JUST CAN'T KILL THREADS IN PYTHON!!!!!!!!
        pass

    def get_values(self):
        s = sum(emote_map.values())
        if (s == 0):
            s = 1
            # sometimes faces aren't detected when candidate doesnt show his face
        for x in emote_map.keys():
            self.textEdit_4.append(f'{x}={round((emote_map[x] / s * 100),2)}%')
            # check if this works without an error

        posi, negi = vot.get_vals()
        detResult = dtV.get_detected()
        self.textEdit_5.setText(f'The analysed voice Tone {detResult}')
        self.textEdit_6.setText(f'The positve Sentences spoke are :{posi} \n the negative sentences spoke are {negi}')
        fscore = emote_map['Confident'] / s * 100
        dscore = 0
        if posi == 0 or negi == 0:
            dscore = 0
        else:
            dscore = posi / (posi + negi) * 100
        d1score = (fscore + dscore) / 0.5 # 2.5 seems like a too low vallue that y i am swithcing to .5
        tscore = (fscore + dscore + d1score) / 3
        print(f'Caluculated scores are {fscore,dscore,d1score,tscore}')
        # writing the scores to the database
        if self.Cname is not None and self.Cid is not None:
            write_to_base(fscore, dscore, d1score, tscore, self.Cname, self.Cid)
        else:
            self.msg.setText('DataBase write failed: No name and Id')
            self.msg.exec()
            return(None)
        reqdata=fetch_data_from_base()
        self.curscore.setText(f'{round(tscore,2)}%')
        # self.writedata='' # this line is not needed as it overwrites the self.writedata produced by the quesser function
        self.writedata+=f"\n\t\tAbstract Data of {self.Cname}\n"
        self.writedata+=f'The analysed voice Tone {detResult}\n'
        self.writedata+=f'The positve Sentences spoke are :{posi} \n the negative sentences spoke are {negi}\n'
        self.writedata+=f'The  confidence score of the candidate is {fscore}\n'
        self.writedata+="\n\\t\tPersonality analysis\n"
        self.writedata+=f"Intelligence : {self.intelligence.text()}\n"
        self.writedata+=f"Interaction : {self.interaction.text()}\n"
        self.writedata += f"Strength : {self.strength.text()}\n"
        self.writedata += f"Weakness : {self.weakness.text()}\n"
        self.writedata += f"Ideal Carrer  : {self.career.text()}\n"
        self.writedata += f"Famous Personalities : {self.famous.text()}\n"
        self.scorecopy=fscore
        self.SetTable(reqdata)

    def SetTable(self,rdata):
        self.table.setColumnCount(6)
        self.table.setRowCount(0)
        rowpos=self.table.rowCount()
        # add the title code here
        # self.table.insertRow(rowpos)
        for x in range(len(rdata)):
            self.table.insertRow(rowpos)
            for y in range(len(rdata[x])):
                self.table.setItem(rowpos,y,QtWidgets.QTableWidgetItem(f'{rdata[x][y]}'))
            rowpos+=1

    # this function is to test the application in the absence of the internet connection
    # some are all the featured might not work so dont panic
    def fake_quesser(self):
        self.qbox.append(chatgui.give_resp("Hello Balarubinan"))
        print("Done")


app = QApplication(sys.argv)
# app.setStyle('Fusion')
w = AppWindow()
w.show()
def gresume_extract():
    return(w.get_resume_extract())

sys.exit(app.exec_())

# most of the app's fuctionality is done
# pending tasks :
# set the title of the tables ---- Couldn't find a way to do that still! :=-(
# write the personality data to the analysis report of the candidate ----Done!!
# change all the images to original size in the project
# use the weighing system in questioning system
# define a yes and no dicctionary of sounds and map the output of the questions to the sounds and capture the appropriate
# answers from the candidate in the given sequence