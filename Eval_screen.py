# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Eval_screen.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Evaluate_Window(object):
    def setupUi(self, Evaluate_Window):
        Evaluate_Window.setObjectName("Evaluate_Window")
        Evaluate_Window.resize(794, 589)
        self.centralwidget = QtWidgets.QWidget(Evaluate_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cb1 = QtWidgets.QComboBox(self.centralwidget)
        self.cb1.setObjectName("cb1")
        self.horizontalLayout.addWidget(self.cb1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cb_2 = QtWidgets.QComboBox(self.centralwidget)
        self.cb_2.setObjectName("cb_2")
        self.horizontalLayout.addWidget(self.cb_2)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 4)

        self.cb1.addItem("")
        self.cb_2.addItem("")
        self.cb1.addItem("")
        self.cb_2.addItem("")
        self.cb_2.addItem("")
        
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setObjectName("listWidget_2")
        self.gridLayout.addWidget(self.listWidget_2, 2, 3, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 2, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 3, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 5, 1, 1, 3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 2)
        Evaluate_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Evaluate_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 794, 26))
        self.menubar.setObjectName("menubar")
        Evaluate_Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Evaluate_Window)
        self.statusbar.setObjectName("statusbar")
        Evaluate_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Evaluate_Window)
        QtCore.QMetaObject.connectSlotsByName(Evaluate_Window)

    def retranslateUi(self, Evaluate_Window):
        _translate = QtCore.QCoreApplication.translate
        Evaluate_Window.setWindowTitle(_translate("Evaluate_Window", "MainWindow"))
        self.label.setText(_translate("Evaluate_Window", "Total Score :"))
        self.pushButton.setText(_translate("Evaluate_Window", "OK"))
        self.label_4.setText(_translate("Evaluate_Window", "Score :"))
        self.label_3.setText(_translate("Evaluate_Window", "Players :"))
        self.cb1.setItemText(1, _translate("Evaluate_Window", "Match 1"))
        self.cb_2.setItemText(1, _translate("Evaluate_Window", "Python11"))
        self.cb_2.setItemText(2, _translate("Evaluate_Window", "Sql11"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Evaluate_Window = QtWidgets.QMainWindow()
    ui = Ui_Evaluate_Window()
    ui.setupUi(Evaluate_Window)
    Evaluate_Window.show()
    sys.exit(app.exec_())
