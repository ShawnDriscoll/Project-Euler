
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
        
        


    def true_palindrome(self, x, y):
        digits = ''
        value = x * y
        str_value = str(value)
        for k in xrange(len(str_value), 0, -1):
            digits += str_value[k - 1]
        if str_value == digits:
            return digits
        else:
            return False
    
    def solveButton_clicked(self):
        palindromes = []
        for i in xrange(100, 1000):
            for j in xrange(100, 1000):
                is_palindrome = self.true_palindrome(i, j)
                if is_palindrome:
                    palindromes.append(int(is_palindrome))
        print palindromes
        
        unsorted = True
        while unsorted:
            unsorted = False
            for i in xrange(len(palindromes) - 1):
                if palindromes[i] > palindromes[i + 1]:
                    palindromes[i], palindromes[i + 1] = palindromes[i + 1], palindromes[i]
                    unsorted = True
        print palindromes
        self.resultDisplay.setText(str(palindromes[len(palindromes) - 1]))




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
    
    
        
        
        
        
        
        
        
        
        
        
        
        
            
            
            
            
            
                    
        
        