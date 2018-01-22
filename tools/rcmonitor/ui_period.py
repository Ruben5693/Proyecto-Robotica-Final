# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ruben/robocomp/tools/rcmonitor/period.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Period(object):
    def setupUi(self, Period):
        Period.setObjectName(_fromUtf8("Period"))
        Period.resize(282, 148)
        self.buttonBox = QtGui.QDialogButtonBox(Period)
        self.buttonBox.setGeometry(QtCore.QRect(90, 110, 160, 25))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.hzBox = QtGui.QDoubleSpinBox(Period)
        self.hzBox.setGeometry(QtCore.QRect(151, 70, 101, 22))
        self.hzBox.setDecimals(7)
        self.hzBox.setMinimum(0.016666)
        self.hzBox.setMaximum(1000.0)
        self.hzBox.setProperty("value", 5.0)
        self.hzBox.setObjectName(_fromUtf8("hzBox"))
        self.msBox = QtGui.QSpinBox(Period)
        self.msBox.setGeometry(QtCore.QRect(149, 30, 101, 22))
        self.msBox.setMinimum(1)
        self.msBox.setMaximum(60000)
        self.msBox.setProperty("value", 200)
        self.msBox.setObjectName(_fromUtf8("msBox"))
        self.label = QtGui.QLabel(Period)
        self.label.setGeometry(QtCore.QRect(30, 30, 81, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Period)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 81, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(Period)
        QtCore.QMetaObject.connectSlotsByName(Period)

    def retranslateUi(self, Period):
        Period.setWindowTitle(_translate("Period", "Set period", None))
        self.label.setText(_translate("Period", "Milliseconds", None))
        self.label_2.setText(_translate("Period", "Hz", None))

