# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\SignUp.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_signUp(object):
    def setupUi(self, signUp):
        signUp.setObjectName("signUp")
        signUp.setWindowModality(QtCore.Qt.NonModal)
        signUp.resize(599, 518)
        signUp.setMinimumSize(QtCore.QSize(599, 518))
        signUp.setMaximumSize(QtCore.QSize(599, 518))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        signUp.setFont(font)
        signUp.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\system/images/qq.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        signUp.setWindowIcon(icon)
        signUp.setAutoFillBackground(False)
        signUp.setStyleSheet("/* Author : Caohaiming */\n"
"#signUp{\n"
"background-image: url(:/lay/system/images/AI.jpeg);\n"
"}")
        self.Username_label = QtWidgets.QLabel(signUp)
        self.Username_label.setGeometry(QtCore.QRect(110, 180, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.Username_label.setFont(font)
        self.Username_label.setStyleSheet("color:white;background: transparent;\n"
"font-size : 18px;")
        self.Username_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Username_label.setLineWidth(1)
        self.Username_label.setScaledContents(False)
        self.Username_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Username_label.setObjectName("Username_label")
        self.Password_Verify_label = QtWidgets.QLabel(signUp)
        self.Password_Verify_label.setGeometry(QtCore.QRect(110, 280, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.Password_Verify_label.setFont(font)
        self.Password_Verify_label.setStyleSheet("color:white;background: transparent;\n"
"font-size : 20px;")
        self.Password_Verify_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Password_Verify_label.setObjectName("Password_Verify_label")
        self.verify_lineEdit = QtWidgets.QLineEdit(signUp)
        self.verify_lineEdit.setGeometry(QtCore.QRect(210, 280, 270, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.verify_lineEdit.setFont(font)
        self.verify_lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.verify_lineEdit.setAutoFillBackground(False)
        self.verify_lineEdit.setStyleSheet("QLineEdit{\n"
"        /*border-radius: 4px;*/\n"
"        height: 30px;\n"
"        /*font-size: 18px;*/\n"
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
"/*QLineEdit:enabled:hover, QLineEdit:enabled:focus {\n"
"        color: rgb(80, 80, 80);\n"
"        border: 1px solid rgb(111, 156, 207);\n"
"        background : transparent;\n"
"        border-radius: 4px;\n"
"}*/\n"
"QLineEdit:!enabled {\n"
"        color: rgb(80, 80, 80);\n"
"}")
        self.verify_lineEdit.setText("")
        self.verify_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.verify_lineEdit.setObjectName("verify_lineEdit")
        self.SignUp_Button = QtWidgets.QPushButton(signUp)
        self.SignUp_Button.setGeometry(QtCore.QRect(110, 340, 180, 50))
        self.SignUp_Button.setStyleSheet("QPushButton{\n"
"    background: transparent;\n"
"    height:30px;\n"
"    color: white;\n"
"    border: 2px solid #FFFFFF;\n"
"    border-radius: 6px;\n"
"    font-size : 18px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #0000FF;\n"
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
"}")
        self.SignUp_Button.setObjectName("SignUp_Button")
        self.menu = QtWidgets.QFrame(signUp)
        self.menu.setGeometry(QtCore.QRect(0, 0, 600, 30))
        self.menu.setMinimumSize(QtCore.QSize(600, 30))
        self.menu.setMaximumSize(QtCore.QSize(600, 30))
        self.menu.setStyleSheet("QFrame{\n"
"    /*background: transparent;*/\n"
"    border-color:white;\n"
"    color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(0, 0, 0), stop:0.25 rgb(0, 0, 60),stop:0.50 rgb(0, 0, 120),stop:0.75 rgb(0, 0, 180),stop:1 rgb(0, 0, 255));\n"
"}")
        self.menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu.setObjectName("menu")
        self.closeButton = QtWidgets.QPushButton(self.menu)
        self.closeButton.setGeometry(QtCore.QRect(558, 0, 41, 29))
        self.closeButton.setMinimumSize(QtCore.QSize(29, 29))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.closeButton.setFont(font)
        self.closeButton.setStyleSheet("QPushButton{\n"
"    color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(0, 0, 0), stop:1 rgb(255, 255, 255));\n"
"    border: none;\n"
"    background : transparent;\n"
"    border-radius:1px;\n"
"}\n"
"/*悬停*/\n"
"QPushButton:hover {\n"
"    color: grey;\n"
"}\n"
"/*鼠标按下不放*/\n"
"QPushButton:pressed {\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}")
        self.closeButton.setCheckable(False)
        self.closeButton.setAutoDefault(False)
        self.closeButton.setDefault(False)
        self.closeButton.setFlat(False)
        self.closeButton.setObjectName("closeButton")
        self.minButton = QtWidgets.QPushButton(self.menu)
        self.minButton.setGeometry(QtCore.QRect(520, -10, 41, 29))
        self.minButton.setMinimumSize(QtCore.QSize(29, 29))
        font = QtGui.QFont()
        font.setFamily("Webdings")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.minButton.setFont(font)
        self.minButton.setStyleSheet("QPushButton{\n"
"    color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(0, 0, 0), stop:1 rgb(255, 255, 255));\n"
"    border: none;\n"
"    background : transparent;\n"
"}\n"
"/*悬停*/\n"
"QPushButton:hover {\n"
"    color: grey;\n"
"}\n"
"/*鼠标按下不放*/\n"
"QPushButton:pressed {\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}")
        self.minButton.setCheckable(False)
        self.minButton.setAutoDefault(False)
        self.minButton.setDefault(False)
        self.minButton.setFlat(False)
        self.minButton.setObjectName("minButton")
        self.return_Button = QtWidgets.QPushButton(signUp)
        self.return_Button.setGeometry(QtCore.QRect(300, 340, 180, 50))
        self.return_Button.setStyleSheet("QPushButton{\n"
"    background: transparent;\n"
"    height:30px;\n"
"    color: white;\n"
"    border: 2px solid #FFFFFF;\n"
"    border-radius: 6px;\n"
"    font-size : 18px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #0000FF;\n"
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
"}")
        self.return_Button.setObjectName("return_Button")
        self.Password_lineEdit = QtWidgets.QLineEdit(signUp)
        self.Password_lineEdit.setGeometry(QtCore.QRect(210, 230, 270, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.Password_lineEdit.setFont(font)
        self.Password_lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Password_lineEdit.setAutoFillBackground(False)
        self.Password_lineEdit.setStyleSheet("QLineEdit{\n"
"        /*border-radius: 4px;*/\n"
"        height: 30px;\n"
"        /*font-size: 18px;*/\n"
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
"/*QLineEdit:enabled:hover, QLineEdit:enabled:focus {\n"
"        color: rgb(80, 80, 80);\n"
"        border: 1px solid rgb(111, 156, 207);\n"
"        background : transparent;\n"
"        border-radius: 4px;\n"
"}*/\n"
"QLineEdit:!enabled {\n"
"        color: rgb(80, 80, 80);\n"
"}")
        self.Password_lineEdit.setText("")
        self.Password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password_lineEdit.setObjectName("Password_lineEdit")
        self.Password_label = QtWidgets.QLabel(signUp)
        self.Password_label.setGeometry(QtCore.QRect(110, 230, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.Password_label.setFont(font)
        self.Password_label.setStyleSheet("color:white;background: transparent;\n"
"font-size : 20px;")
        self.Password_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Password_label.setObjectName("Password_label")
        self.Username = QtWidgets.QLineEdit(signUp)
        self.Username.setGeometry(QtCore.QRect(210, 180, 270, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.Username.setFont(font)
        self.Username.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Username.setAutoFillBackground(False)
        self.Username.setStyleSheet("QLineEdit{\n"
"        /*border-radius: 4px;*/\n"
"        height: 30px;\n"
"        font-size: 20px;\n"
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
"/*QLineEdit:enabled:hover, QLineEdit:enabled:focus {\n"
"        color: rgb(80, 80, 80);\n"
"        border: 1px solid rgb(111, 156, 207);\n"
"        background : transparent;\n"
"        border-radius: 4px;\n"
"}*/\n"
"QLineEdit:!enabled {\n"
"        color: rgb(80, 80, 80);\n"
"}")
        self.Username.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Username.setText("")
        self.Username.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.Username.setObjectName("Username")

        self.retranslateUi(signUp)
        self.minButton.clicked.connect(signUp.showMinimized)
        self.closeButton.clicked.connect(signUp.close)
        self.return_Button.clicked.connect(signUp.close)
        QtCore.QMetaObject.connectSlotsByName(signUp)

    def retranslateUi(self, signUp):
        _translate = QtCore.QCoreApplication.translate
        signUp.setWindowTitle(_translate("signUp", "注册页面"))
        self.Username_label.setText(_translate("signUp", "用户名"))
        self.Password_Verify_label.setText(_translate("signUp", "验证密码"))
        self.SignUp_Button.setText(_translate("signUp", "注册"))
        self.closeButton.setText(_translate("signUp", "×"))
        self.minButton.setText(_translate("signUp", "0"))
        self.return_Button.setText(_translate("signUp", "返回"))
        self.Password_label.setText(_translate("signUp", "密码"))
import icon_rc
