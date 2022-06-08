import sys
import subprocess as s
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QCompleter, QLineEdit
from front import Ui_MainWindow
from back import baza_promstroy, baza_bshsu, baza_nova, baza_tozzi, baza_uralkal, baza_instrukcii

#путь к ПДФ ридеру
rider = ("C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe")

#Запуск графической части
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

#функции вызывающие запуск поиска
def promstroy():
    vvod = ui.lineEdit.text()
    promstroy = s.call([rider, baza_promstroy[vvod]])

def bshsu():
    vvod = ui.lineEdit_2.text()
    bshesu = s.call([rider, baza_bshsu[vvod]])

def nova():
    vvod = ui.lineEdit_3.text()
    nova = s.call([rider, baza_nova[vvod]])

def tozzi():
    vvod = ui.lineEdit_4.text()
    tozzi = s.call([rider, baza_tozzi[vvod]])

def uralkal():
    vvod = ui.lineEdit_5.text()
    uralkal = s.call([rider, baza_uralkal[vvod]])

def instrukcii():
    vvod = ui.lineEdit_6.text()
    instrukcii = s.call([rider, baza_instrukcii[vvod]])

#Кнопки запускающие функции
ui.pushButton.clicked.connect(promstroy)
ui.pushButton_2.clicked.connect(bshsu)
ui.pushButton_3.clicked.connect(nova)
ui.pushButton_4.clicked.connect(tozzi)
ui.pushButton_5.clicked.connect(uralkal)
ui.pushButton_6.clicked.connect(instrukcii)
ui.pushButton_7.clicked.connect(sys.exit)

sys.exit(app.exec_())
