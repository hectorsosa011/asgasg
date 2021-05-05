# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tabla_impactos.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dlg_Impactos(object):
    def setupUi(self, dlg_Impactos):
        dlg_Impactos.setObjectName("dlg_Impactos")
        dlg_Impactos.resize(461, 300)
        self.Tbw_Impactos = QtWidgets.QTableWidget(dlg_Impactos)
        self.Tbw_Impactos.setGeometry(QtCore.QRect(10, 10, 441, 281))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.Tbw_Impactos.setFont(font)
        self.Tbw_Impactos.setAlternatingRowColors(True)
        self.Tbw_Impactos.setObjectName("Tbw_Impactos")
        self.Tbw_Impactos.setColumnCount(3)
        self.Tbw_Impactos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.Tbw_Impactos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tbw_Impactos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tbw_Impactos.setHorizontalHeaderItem(2, item)

        self.retranslateUi(dlg_Impactos)
        QtCore.QMetaObject.connectSlotsByName(dlg_Impactos)

    def retranslateUi(self, dlg_Impactos):
        _translate = QtCore.QCoreApplication.translate
        dlg_Impactos.setWindowTitle(_translate("dlg_Impactos", "Tabla de impactos"))
        item = self.Tbw_Impactos.horizontalHeaderItem(0)
        item.setText(_translate("dlg_Impactos", "Proyecto"))
        item = self.Tbw_Impactos.horizontalHeaderItem(1)
        item.setText(_translate("dlg_Impactos", "Tipo"))
        item = self.Tbw_Impactos.horizontalHeaderItem(2)
        item.setText(_translate("dlg_Impactos", "Distancia"))

