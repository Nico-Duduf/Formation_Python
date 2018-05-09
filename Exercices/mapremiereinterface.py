# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\n.dufresne\Desktop\Exercices\mapremiereinterface.ui'
#
# Created: Tue Apr 17 19:18:31 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(514, 457)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.premierBouton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.premierBouton.sizePolicy().hasHeightForWidth())
        self.premierBouton.setSizePolicy(sizePolicy)
        self.premierBouton.setObjectName("premierBouton")
        self.horizontalLayout_2.addWidget(self.premierBouton)
        self.verticalSlider = QtGui.QSlider(self.centralwidget)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.horizontalLayout_2.addWidget(self.verticalSlider)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.premiereBox = QtGui.QCheckBox(self.centralwidget)
        self.premiereBox.setObjectName("premiereBox")
        self.horizontalLayout.addWidget(self.premiereBox)
        self.spinBox = QtGui.QSpinBox(self.centralwidget)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 514, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

    def maFonction(self, truc):
        fais un truc

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.premierBouton, QtCore.SIGNAL("clicked()"), self.maFonction)
        QtCore.QObject.connect(self.verticalSlider, QtCore.SIGNAL("sliderMoved(int)"), self.spinBox.setValue)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.premierBouton.setText(QtGui.QApplication.translate("MainWindow", "mon premier bouton", None, QtGui.QApplication.UnicodeUTF8))
        self.premiereBox.setText(QtGui.QApplication.translate("MainWindow", "macheckbox 1", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

