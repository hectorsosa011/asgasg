from qgis.PyQt.QtWidgets import *
from .tabla_impactos_dialog import Ui_dlg_Impactos

class DlgTabla(QDialog, Ui_dlg_Impactos):
    def __init__(self):
        super(DlgTabla, self).__init__()
        self.setupUi(self)
        
        self.Tbw_Impactos.setColumnWidth(1, 200)

