# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\paraModify.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_modify(object):
    def setupUi(self, modify):
        modify.setObjectName("modify")
        modify.setWindowModality(QtCore.Qt.NonModal)
        modify.resize(600, 400)
        modify.setMinimumSize(QtCore.QSize(600, 400))
        modify.setMaximumSize(QtCore.QSize(600, 400))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        modify.setFont(font)
        modify.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\system/images/qq.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        modify.setWindowIcon(icon)
        modify.setAutoFillBackground(False)
        modify.setStyleSheet("/* Author : Caohaiming */\n"
"\n"
"#modify{\n"
"background-image: url(:/img/system/images/DataSci.png);\n"
"}")
        self.returnLogin = QtWidgets.QPushButton(modify)
        self.returnLogin.setGeometry(QtCore.QRect(350, 320, 201, 41))
        self.returnLogin.setStyleSheet("QPushButton{\n"
"    background: transparent;\n"
"    height:30px;\n"
"    color: white;\n"
"    border: 2px solid #FFFFFF;\n"
"    border-radius: 6px;\n"
"    font-size : 19px;\n"
"}\n"
"QPushButton:hover {\n"
"    /*background-color: #0000FF;*/\n"
"    \n"
"    border-radius: 6px;\n"
"    color:white;\n"
"    font-size : 20px;\n"
"}\n"
"QPushButton:pressed {\n"
"    \n"
"    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
"    padding-left:3px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:3px;\n"
"    border: 2px solid rgb(80,80,80);\n"
"}")
        self.returnLogin.setObjectName("returnLogin")
        self.setButton = QtWidgets.QPushButton(modify)
        self.setButton.setGeometry(QtCore.QRect(60, 320, 201, 41))
        self.setButton.setStyleSheet("QPushButton{\n"
"    background: transparent;\n"
"    height:30px;\n"
"    color: white;\n"
"    border: 2px solid #FFFFFF;\n"
"    border-radius: 6px;\n"
"    font-size : 19px;\n"
"}\n"
"QPushButton:hover {\n"
"    /*background-color: #0000FF;*/\n"
"    \n"
"    border-radius: 6px;\n"
"    color:white;\n"
"    font-size : 20px;\n"
"}\n"
"QPushButton:pressed {\n"
"    \n"
"    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
"    padding-left:3px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:3px;\n"
"    border: 2px solid rgb(80,80,80);\n"
"}")
        self.setButton.setObjectName("setButton")
        self.FTypeLabel = QtWidgets.QLabel(modify)
        self.FTypeLabel.setGeometry(QtCore.QRect(60, 80, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.FTypeLabel.setFont(font)
        self.FTypeLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.FTypeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.FTypeLabel.setObjectName("FTypeLabel")
        self.FtypeBox = QtWidgets.QComboBox(modify)
        self.FtypeBox.setGeometry(QtCore.QRect(260, 80, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.FtypeBox.setFont(font)
        self.FtypeBox.setStyleSheet("QComboBox{\n"
"        height: 30px;\n"
"        font-size : 30px;\n"
"       /* border-radius: 4px;*/\n"
"        background: transparent;\n"
"        border-color:#FFFFFF;\n"
"        border-style:solid;\n"
"        border-top-width:0px;\n"
"        border-right-width:0px;\n"
"        border-bottom-width:2px;\n"
"        border-left-width:0px;\n"
"}\n"
"QComboBox:enabled{\n"
"        color: white;\n"
"        font-size : 20px;\n"
"}\n"
"QComboBox:!enabled {\n"
"        color: rgb(80, 80, 80);\n"
"        font-size : 20px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"        border: 1px solid rgb(111, 156, 207);\n"
"        outline: none;\n"
"}")
        self.FtypeBox.setEditable(False)
        self.FtypeBox.setObjectName("FtypeBox")
        self.FtypeBox.addItem("")
        self.FtypeBox.addItem("")
        self.ClipLimitLabel = QtWidgets.QLabel(modify)
        self.ClipLimitLabel.setGeometry(QtCore.QRect(60, 140, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.ClipLimitLabel.setFont(font)
        self.ClipLimitLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.ClipLimitLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ClipLimitLabel.setObjectName("ClipLimitLabel")
        self.ClipLimitEdit = QtWidgets.QLineEdit(modify)
        self.ClipLimitEdit.setGeometry(QtCore.QRect(260, 140, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.ClipLimitEdit.setFont(font)
        self.ClipLimitEdit.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.ClipLimitEdit.setAutoFillBackground(False)
        self.ClipLimitEdit.setStyleSheet("QLineEdit{\n"
"        height: 30px;\n"
"        background: transparent;\n"
"}\n"
"QLineEdit:enabled {\n"
"        color:#FFFFFF;\n"
"        border-color:#FFFFFF;\n"
"        border-style:solid;\n"
"        border-top-width:0px;\n"
"        border-right-width:0px;\n"
"        border-bottom-width:2px;\n"
"        border-left-width:0px;\n"
"        color: white;\n"
"}\n"
"")
        self.ClipLimitEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.ClipLimitEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.ClipLimitEdit.setObjectName("ClipLimitEdit")
        self.GridWidthLabel = QtWidgets.QLabel(modify)
        self.GridWidthLabel.setGeometry(QtCore.QRect(60, 200, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.GridWidthLabel.setFont(font)
        self.GridWidthLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.GridWidthLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.GridWidthLabel.setObjectName("GridWidthLabel")
        self.GridWidthEdit = QtWidgets.QLineEdit(modify)
        self.GridWidthEdit.setGeometry(QtCore.QRect(260, 200, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.GridWidthEdit.setFont(font)
        self.GridWidthEdit.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.GridWidthEdit.setAutoFillBackground(False)
        self.GridWidthEdit.setStyleSheet("QLineEdit{\n"
"        height: 30px;\n"
"        background: transparent;\n"
"}\n"
"QLineEdit:enabled {\n"
"        color:#FFFFFF;\n"
"        border-color:#FFFFFF;\n"
"        border-style:solid;\n"
"        border-top-width:0px;\n"
"        border-right-width:0px;\n"
"        border-bottom-width:2px;\n"
"        border-left-width:0px;\n"
"        color: white;\n"
"}\n"
"\n"
"QLineEdit:!enabled {\n"
"        color: rgb(80, 80, 80);\n"
"}")
        self.GridWidthEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.GridWidthEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.GridWidthEdit.setObjectName("GridWidthEdit")
        self.GridHeightLabel = QtWidgets.QLabel(modify)
        self.GridHeightLabel.setGeometry(QtCore.QRect(60, 260, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.GridHeightLabel.setFont(font)
        self.GridHeightLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.GridHeightLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.GridHeightLabel.setObjectName("GridHeightLabel")
        self.GridHeightEdit = QtWidgets.QLineEdit(modify)
        self.GridHeightEdit.setGeometry(QtCore.QRect(260, 260, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.GridHeightEdit.setFont(font)
        self.GridHeightEdit.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.GridHeightEdit.setAutoFillBackground(False)
        self.GridHeightEdit.setStyleSheet("QLineEdit{\n"
"        height: 30px;\n"
"        background: transparent;\n"
"}\n"
"QLineEdit:enabled {\n"
"        color:#FFFFFF;\n"
"        border-color:#FFFFFF;\n"
"        border-style:solid;\n"
"        border-top-width:0px;\n"
"        border-right-width:0px;\n"
"        border-bottom-width:2px;\n"
"        border-left-width:0px;\n"
"        color: white;\n"
"}\n"
"\n"
"QLineEdit:!enabled {\n"
"        color: rgb(80, 80, 80);\n"
"}")
        self.GridHeightEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.GridHeightEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.GridHeightEdit.setObjectName("GridHeightEdit")
        self.TitleLabel = QtWidgets.QLabel(modify)
        self.TitleLabel.setGeometry(QtCore.QRect(70, 10, 481, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.TitleLabel.setFont(font)
        self.TitleLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.TitleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TitleLabel.setObjectName("TitleLabel")

        self.retranslateUi(modify)
        self.returnLogin.clicked.connect(modify.close)
        QtCore.QMetaObject.connectSlotsByName(modify)

    def retranslateUi(self, modify):
        _translate = QtCore.QCoreApplication.translate
        modify.setWindowTitle(_translate("modify", "作者信息"))
        self.returnLogin.setText(_translate("modify", "返回"))
        self.setButton.setText(_translate("modify", "确定"))
        self.FTypeLabel.setText(_translate("modify", "function type"))
        self.FtypeBox.setItemText(0, _translate("modify", "local"))
        self.FtypeBox.setItemText(1, _translate("modify", "global"))
        self.ClipLimitLabel.setText(_translate("modify", "clip limit"))
        self.ClipLimitEdit.setText(_translate("modify", "1.0"))
        self.ClipLimitEdit.setPlaceholderText(_translate("modify", "input a float number"))
        self.GridWidthLabel.setText(_translate("modify", "grid width"))
        self.GridWidthEdit.setText(_translate("modify", "8"))
        self.GridWidthEdit.setPlaceholderText(_translate("modify", "input a int number"))
        self.GridHeightLabel.setText(_translate("modify", "grid height"))
        self.GridHeightEdit.setText(_translate("modify", "8"))
        self.GridHeightEdit.setPlaceholderText(_translate("modify", "input a int number"))
        self.TitleLabel.setText(_translate("modify", "Edit window"))
import icon_rc
import signup_rc
