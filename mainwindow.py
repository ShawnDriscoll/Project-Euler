# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Fri Aug 19 22:35:49 2016
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(308, 228)
        MainWindow.setMinimumSize(QtCore.QSize(308, 228))
        MainWindow.setMaximumSize(QtCore.QSize(308, 228))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("leuler.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.resultDisplay = QtGui.QLabel(self.centralwidget)
        self.resultDisplay.setGeometry(QtCore.QRect(80, 80, 161, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Code Bold"))
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.resultDisplay.setFont(font)
        self.resultDisplay.setFrameShape(QtGui.QFrame.Box)
        self.resultDisplay.setFrameShadow(QtGui.QFrame.Sunken)
        self.resultDisplay.setText(_fromUtf8(""))
        self.resultDisplay.setAlignment(QtCore.Qt.AlignCenter)
        self.resultDisplay.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.resultDisplay.setObjectName(_fromUtf8("resultDisplay"))
        self.resultLabel = QtGui.QLabel(self.centralwidget)
        self.resultLabel.setGeometry(QtCore.QRect(130, 50, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.resultLabel.setFont(font)
        self.resultLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.resultLabel.setObjectName(_fromUtf8("resultLabel"))
        self.solveButton = QtGui.QPushButton(self.centralwidget)
        self.solveButton.setGeometry(QtCore.QRect(40, 120, 75, 23))
        self.solveButton.setObjectName(_fromUtf8("solveButton"))
        self.clearButton = QtGui.QPushButton(self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(120, 120, 75, 23))
        self.clearButton.setObjectName(_fromUtf8("clearButton"))
        self.quitButton = QtGui.QPushButton(self.centralwidget)
        self.quitButton.setGeometry(QtCore.QRect(200, 120, 75, 23))
        self.quitButton.setObjectName(_fromUtf8("quitButton"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 308, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setObjectName(_fromUtf8("menuMenu"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setSizeGripEnabled(False)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionSolve_Problem = QtGui.QAction(MainWindow)
        self.actionSolve_Problem.setObjectName(_fromUtf8("actionSolve_Problem"))
        self.actionClear = QtGui.QAction(MainWindow)
        self.actionClear.setObjectName(_fromUtf8("actionClear"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionAbout_Project_Euler = QtGui.QAction(MainWindow)
        self.actionAbout_Project_Euler.setObjectName(_fromUtf8("actionAbout_Project_Euler"))
        self.menuMenu.addAction(self.actionSolve_Problem)
        self.menuMenu.addAction(self.actionClear)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout_Project_Euler)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.solveButton, self.clearButton)
        MainWindow.setTabOrder(self.clearButton, self.quitButton)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Project Euler", None, QtGui.QApplication.UnicodeUTF8))
        self.resultDisplay.setToolTip(QtGui.QApplication.translate("MainWindow", "Result display", None, QtGui.QApplication.UnicodeUTF8))
        self.resultLabel.setText(QtGui.QApplication.translate("MainWindow", "Result", None, QtGui.QApplication.UnicodeUTF8))
        self.solveButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Solve the problem", None, QtGui.QApplication.UnicodeUTF8))
        self.solveButton.setText(QtGui.QApplication.translate("MainWindow", "Solve", None, QtGui.QApplication.UnicodeUTF8))
        self.clearButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Clear field", None, QtGui.QApplication.UnicodeUTF8))
        self.clearButton.setText(QtGui.QApplication.translate("MainWindow", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.quitButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Quit this program", None, QtGui.QApplication.UnicodeUTF8))
        self.quitButton.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMenu.setTitle(QtGui.QApplication.translate("MainWindow", "Menu", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSolve_Problem.setText(QtGui.QApplication.translate("MainWindow", "Solve Problem", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSolve_Problem.setStatusTip(QtGui.QApplication.translate("MainWindow", "Solve the problem", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClear.setText(QtGui.QApplication.translate("MainWindow", "Clear Field", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClear.setStatusTip(QtGui.QApplication.translate("MainWindow", "Clear field", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setStatusTip(QtGui.QApplication.translate("MainWindow", "Quit this program", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_Project_Euler.setText(QtGui.QApplication.translate("MainWindow", "About Project Euler", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_Project_Euler.setStatusTip(QtGui.QApplication.translate("MainWindow", "About Project Euler", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

