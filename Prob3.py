
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from mainwindow import Ui_MainWindow
from aboutdialog import Ui_aboutDialog
import sys
from math import sqrt

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
        
        


    def fac(self, number):
        factors = []
        for i in xrange(2, int(sqrt(number)) + 1):
            if number % i == 0:
                factors.append(i)
        return factors
    
    def find_prime_num(self, fac_list):
        primes = []
        for i in xrange(len(fac_list)):
            if self.fac(fac_list[i]) == []:
                primes.append(fac_list[i])
        return primes
    
    def solveButton_clicked(self):
        number = 600851475143
        fac_list = self.fac(number)
        print fac_list
        prime_list = self.find_prime_num(fac_list)
        print prime_list
        self.resultDisplay.setText(str(prime_list[len(prime_list) - 1]))




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
    
    
        
        
        
        
        
        
        
        
        
        
        
        
            
            
            
            
            
                    
        
        