
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
        
        


    def fib(self, n):
        terms = [1, 2]
        value = terms[1]
        pointer = 0
        while value < n:
            value = terms[pointer] + terms[pointer + 1]
            terms.append(value)
            pointer += 1
        return terms
    
    def sum_even(self, terms):
        even_terms = []
        for value in xrange(len(terms)):
            if terms[value] % 2 == 0:
                even_terms.append(terms[value])
        print even_terms
        return even_terms

    
    def solveButton_clicked(self):
        n = 4000000
        the_naturals = self.fib(n)
        print the_naturals[0:len(the_naturals) - 1]
        result = sum(self.sum_even(the_naturals[0:len(the_naturals) - 1]))
        print result
        self.resultDisplay.setText(str(result))
        
        #print self.resultDisplay.text()
        
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
    
    
        
        
        
        
        
        
        
        
        
        
        
        
            
            
            
            
            
                    
        
        