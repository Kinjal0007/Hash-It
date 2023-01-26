import os
import sys
from ui_main import *
from Custom_Widgets.Widgets import *
from PySide2.QtWidgets import QTableWidgetItem
settings = QSettings()

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui, jsonFiles = {
        "style2.json"
        })
        self.show() 
        QAppSettings.updateAppSettings(self)
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) 
