# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newteamname.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(303, 117)
        self.formLayout = QtWidgets.QFormLayout(Form)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.l = QtWidgets.QLineEdit(Form)
        self.l.setObjectName("l")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.l)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.label_2)
        self.btn = QtWidgets.QPushButton(Form)
        self.btn.setObjectName("btn")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.btn)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Team Name :"))
        self.btn.setText(_translate("Form", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
