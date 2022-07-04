# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 15:29:05 2022

@author: hallc
"""
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow)
from PyQt5.uic import loadUi
from DoseCalcUI import Ui_MainWindow

class Window(QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.d_e=2.1128e11 # Constant 1e-9 ev/C
        self.qe=1.602176e-19 # Coulombs
        self.G=570 # Geometric IC factor?
        
        loadUi("DoseCalcUI.ui", self)
        self.setupUi(self)
        # Display the default parameters
        self.label_Area.setStyleSheet("background-color: lightgreen")
        self.label_Area.setText("15.0")
        self.label_Energy.setStyleSheet("background-color: lightgreen")
        self.label_Energy.setText("40.0")
        self.label_Ke.setStyleSheet("background-color: lightgreen")
        self.label_Ke.setText("1.52")

    def FluxFromCurrent(self):
    # Calculates the flux given the IC current.
        A=15*15 # Beam area mm^2
        E=40 # KeV
        Ke=1.52
        ICabs=0.00041 # Absorption of the IC volume
        I=float(self.lineEdit_Current.text()) # micro-Amps
        F=(I*Ke*self.d_e)/(ICabs*A*E)
        # print('Flux =',F)
        sFlux="{:.4e}".format(F)
        self.lineEdit_Flux.setText(sFlux) # Display the result
        
    def DoseFromFlux(self):
        # Calculates the air KERMA given the flux.
        E=40 # KeV
        Ep=E*1000*self.qe # Joules per photon
        F=float(self.lineEdit_Flux.text())*100.0 # Flux density (cm^2)
        EF=Ep*F # Joules/sec
        MuEn=0.0683 # cm^2/g
        KERMA=EF*MuEn*1000 # J/kg
        sKERMA="{:.4e}".format(KERMA)
        self.lineEdit_KERMA.setText(sKERMA) # Display the result
        
    def CurrentFromDose(self):
    # Calculates the IC current given the air KERMA
        Ke=1.52
        A=15*15 # mm^2
        KERMA=float(self.lineEdit_KERMA.text())
        I=(KERMA*A)/(self.G*Ke)
        # print('Current =',I)
        sCurrent="{:.4e}".format(I)
        self.lineEdit_Current.setText(sCurrent) # Display the result
       
    def slot_KERMA(self):
        # print('Slot KERMA')
        self.CurrentFromDose()
        # Now current has been recalculated...
        self.FluxFromCurrent()
        
    def slot_Current(self):
        # print('Slot_Current')
        self.FluxFromCurrent()
        # Now flux has been recalculated...
        self.DoseFromFlux()
        
    def slot_Flux(self):
        # print('Slot Flux')
        self.DoseFromFlux()
        # Now dose has been recalculated
        self.CurrentFromDose()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
    