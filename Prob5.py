
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from mainwindow import Ui_MainWindow
from aboutdialog import Ui_aboutDialog
import sys

class aboutDialog(QDialog, Ui_aboutDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        flags = Qt.Drawer | Qt.WindowStaysOnTopHint
        self.setWindowFlags(flags)
        self.setupUi(self)
        self.aboutOKButton.clicked.connect(self.acceptOKButtonClicked)
        
    def acceptOKButtonClicked(self):
        self.close()

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        
        self.solveButton.clicked.connect(self.solveButton_clicked)
        self.actionSolve_Problem.triggered.connect(self.solveButton_clicked)
        
        self.clearButton.clicked.connect(self.clearButton_clicked)
        self.actionClear.triggered.connect(self.clearButton_clicked)
        
        self.actionAbout_Project_Euler.triggered.connect(self.actionAbout_triggered)
        self.popAboutDialog=aboutDialog()
        
        self.quitButton.clicked.connect(self.quitButton_clicked)
        self.actionQuit.triggered.connect(self.quitButton_clicked)
        
        


    
    def solveButton_clicked(self):
        n = 0
        searching = True
        while searching:
            n += 1
            the_one = True
            for i in xrange(20):
                if n % (i + 1) <> 0:
                    the_one = False
            if the_one:
                searching = False
        self.resultDisplay.setText(str(n))
            




    def clearButton_clicked(self):
        self.resultDisplay.setText('')
        
    def actionAbout_triggered(self):
        self.popAboutDialog.show()
    
    def quitButton_clicked(self):
        self.close()
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainApp = MainWindow()
    MainApp.show()
    sys.exit(app.exec_())
    
    
        
        
        
        
        
        
        
        
        
        
        
        
            
            
            
            
            
                    
        
        