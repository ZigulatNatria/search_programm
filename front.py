# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'front.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QCompleter, QLineEdit
from back import word_auto_promstroy, word_auto_bshsu, word_auto_nova, word_auto_tozzi, word_auto_uralkal, word_auto_instrukcii


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 40, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 90, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(510, 90, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(490, 20, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(490, 40, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 240, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 170, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 190, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(510, 240, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(490, 170, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(490, 190, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(40, 390, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 320, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(20, 340, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(510, 390, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(490, 320, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(490, 340, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(250, 470, 281, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # инициирование автозаполнения
        self.promstroy()
        self.bshsu()
        self.nova()
        self.tozzi()
        self.uralkal()
        self.instrukcii()


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Карты СОУТ и Инструкции по ОТ"))
        self.label.setText(_translate("MainWindow", "АО \"Промстрой\""))
        self.pushButton.setText(_translate("MainWindow", "Поиск"))
        self.pushButton_2.setText(_translate("MainWindow", "Поиск"))
        self.label_2.setText(_translate("MainWindow", "ООО \"БШСУ\""))
        self.pushButton_3.setText(_translate("MainWindow", "Поиск"))
        self.label_3.setText(_translate("MainWindow", "ООО \"НОВА\""))
        self.pushButton_4.setText(_translate("MainWindow", "Поиск"))
        self.label_4.setText(_translate("MainWindow", "ООО \"Тоцци Восток\""))
        self.pushButton_5.setText(_translate("MainWindow", "Поиск"))
        self.label_5.setText(_translate("MainWindow", "ООО \"Урал Калий Ремонт\""))
        self.pushButton_6.setText(_translate("MainWindow", "Поиск"))
        self.label_6.setText(_translate("MainWindow", "Инструкции по ОТ"))
        self.pushButton_7.setText(_translate("MainWindow", "ВЫХОД"))

        # функция выполняющая автозаполненеие
    def promstroy(self):
        znacenie = word_auto_promstroy # Передача списка ключевых слов из back.py
        completer = QCompleter(znacenie)
        self.LineEdit = QLineEdit() #обозначение конкретной строки ввода пользователя
        self.lineEdit.setCompleter(completer)

    def bshsu(self):
        znacenie = word_auto_bshsu
        completer = QCompleter(znacenie)
        self.LineEdit_2 = QLineEdit()
        self.lineEdit_2.setCompleter(completer)

    def nova(self):
        znacenie = word_auto_nova
        completer = QCompleter(znacenie)
        self.LineEdit_3 = QLineEdit()
        self.lineEdit_3.setCompleter(completer)

    def tozzi(self):
        znacenie = word_auto_tozzi
        completer = QCompleter(znacenie)
        self.LineEdit_4 = QLineEdit()
        self.lineEdit_4.setCompleter(completer)

    def uralkal(self):
        znacenie = word_auto_uralkal
        completer = QCompleter(znacenie)
        self.LineEdit_5 = QLineEdit()
        self.lineEdit_5.setCompleter(completer)

    def instrukcii(self):
        znacenie = word_auto_instrukcii
        completer = QCompleter(znacenie)
        self.LineEdit_6 = QLineEdit()
        self.lineEdit_6.setCompleter(completer)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
