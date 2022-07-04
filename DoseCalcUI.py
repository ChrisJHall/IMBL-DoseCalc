# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DoseCalcUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(481, 320)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.IClabel = QtWidgets.QLabel(self.centralwidget)
        self.IClabel.setGeometry(QtCore.QRect(170, 130, 141, 21))
        self.IClabel.setObjectName("IClabel")
        self.Flux_label = QtWidgets.QLabel(self.centralwidget)
        self.Flux_label.setGeometry(QtCore.QRect(350, 180, 81, 21))
        self.Flux_label.setObjectName("Flux_label")
        self.KERMA_label = QtWidgets.QLabel(self.centralwidget)
        self.KERMA_label.setGeometry(QtCore.QRect(50, 180, 71, 21))
        self.KERMA_label.setObjectName("KERMA_label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(390, 280, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_Current = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Current.setGeometry(QtCore.QRect(180, 160, 113, 20))
        self.lineEdit_Current.setObjectName("lineEdit_Current")
        self.lineEdit_Flux = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Flux.setGeometry(QtCore.QRect(320, 210, 113, 20))
        self.lineEdit_Flux.setObjectName("lineEdit_Flux")
        self.lineEdit_KERMA = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_KERMA.setGeometry(QtCore.QRect(30, 210, 113, 20))
        self.lineEdit_KERMA.setObjectName("lineEdit_KERMA")
        self.label_I = QtWidgets.QLabel(self.centralwidget)
        self.label_I.setGeometry(QtCore.QRect(210, 180, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_I.setFont(font)
        self.label_I.setAlignment(QtCore.Qt.AlignCenter)
        self.label_I.setObjectName("label_I")
        self.label_F = QtWidgets.QLabel(self.centralwidget)
        self.label_F.setGeometry(QtCore.QRect(330, 230, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_F.setFont(font)
        self.label_F.setAlignment(QtCore.Qt.AlignCenter)
        self.label_F.setObjectName("label_F")
        self.label_D = QtWidgets.QLabel(self.centralwidget)
        self.label_D.setGeometry(QtCore.QRect(30, 230, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_D.setFont(font)
        self.label_D.setAlignment(QtCore.Qt.AlignCenter)
        self.label_D.setObjectName("label_D")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(30, 20, 131, 31))
        self.label1.setObjectName("label1")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(250, 20, 131, 31))
        self.label2.setObjectName("label2")
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(30, 60, 211, 31))
        self.label3.setObjectName("label3")
        self.label_Area = QtWidgets.QLabel(self.centralwidget)
        self.label_Area.setGeometry(QtCore.QRect(170, 20, 47, 21))
        self.label_Area.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Area.setObjectName("label_Area")
        self.label_Energy = QtWidgets.QLabel(self.centralwidget)
        self.label_Energy.setGeometry(QtCore.QRect(390, 20, 47, 21))
        self.label_Energy.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Energy.setObjectName("label_Energy")
        self.label_Ke = QtWidgets.QLabel(self.centralwidget)
        self.label_Ke.setGeometry(QtCore.QRect(250, 60, 47, 21))
        self.label_Ke.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Ke.setObjectName("label_Ke")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.close)
        self.lineEdit_Current.returnPressed.connect(MainWindow.slot_Current)
        self.lineEdit_Flux.returnPressed.connect(MainWindow.slot_Flux)
        self.lineEdit_KERMA.returnPressed.connect(MainWindow.slot_KERMA)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.IClabel.setText(_translate("MainWindow", "Ionisation Chamber Current"))
        self.Flux_label.setText(_translate("MainWindow", "Flux Density"))
        self.KERMA_label.setText(_translate("MainWindow", "air KERMA"))
        self.pushButton.setText(_translate("MainWindow", "Close"))
        self.label_I.setText(_translate("MainWindow", "uA"))
        self.label_F.setText(_translate("MainWindow", "ph/mm^2/sec"))
        self.label_D.setText(_translate("MainWindow", "Gy/sec"))
        self.label1.setText(_translate("MainWindow", "Beam area set to (mm^2):"))
        self.label2.setText(_translate("MainWindow", "Beam energy set to (keV):"))
        self.label3.setText(_translate("MainWindow", "Ionisation chamber energy loss correction:"))
        self.label_Area.setText(_translate("MainWindow", "Area"))
        self.label_Energy.setText(_translate("MainWindow", "Energy"))
        self.label_Ke.setText(_translate("MainWindow", "Ke"))
