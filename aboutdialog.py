# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutdialog.ui'
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

class Ui_aboutDialog(object):
    def setupUi(self, aboutDialog):
        aboutDialog.setObjectName(_fromUtf8("aboutDialog"))
        aboutDialog.resize(285, 239)
        aboutDialog.setMinimumSize(QtCore.QSize(285, 239))
        aboutDialog.setMaximumSize(QtCore.QSize(285, 239))
        self.aboutOKButton = QtGui.QPushButton(aboutDialog)
        self.aboutOKButton.setGeometry(QtCore.QRect(110, 190, 75, 23))
        self.aboutOKButton.setObjectName(_fromUtf8("aboutOKButton"))
        self.textLabel = QtGui.QLabel(aboutDialog)
        self.textLabel.setGeometry(QtCore.QRect(50, 50, 191, 111))
        self.textLabel.setTextFormat(QtCore.Qt.RichText)
        self.textLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.textLabel.setWordWrap(True)
        self.textLabel.setObjectName(_fromUtf8("textLabel"))

        self.retranslateUi(aboutDialog)
        QtCore.QMetaObject.connectSlotsByName(aboutDialog)

    def retranslateUi(self, aboutDialog):
        aboutDialog.setWindowTitle(QtGui.QApplication.translate("aboutDialog", "About Project Euler", None, QtGui.QApplication.UnicodeUTF8))
        self.aboutOKButton.setText(QtGui.QApplication.translate("aboutDialog", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel.setText(QtGui.QApplication.translate("aboutDialog", "<html><head/><body><p align=\"center\"><br/><span style=\" font-size:10pt;\">Project Euler program</span></p><p align=\"center\"><span style=\" font-size:10pt;\">by </span></p><p align=\"center\"><span style=\" font-size:10pt;\">Shawn Driscoll</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    aboutDialog = QtGui.QDialog()
    ui = Ui_aboutDialog()
    ui.setupUi(aboutDialog)
    aboutDialog.show()
    sys.exit(app.exec_())

