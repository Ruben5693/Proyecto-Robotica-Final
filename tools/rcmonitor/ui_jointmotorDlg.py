# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ruben/robocomp/tools/rcmonitor/jointmotorDlg.ui'
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

class Ui_JointMotorDlg(object):
    def setupUi(self, JointMotorDlg):
        JointMotorDlg.setObjectName(_fromUtf8("JointMotorDlg"))
        JointMotorDlg.resize(496, 200)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(JointMotorDlg.sizePolicy().hasHeightForWidth())
        JointMotorDlg.setSizePolicy(sizePolicy)
        JointMotorDlg.setMaximumSize(QtCore.QSize(500, 200))
        self.verticalLayout = QtGui.QVBoxLayout(JointMotorDlg)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_3 = QtGui.QLabel(JointMotorDlg)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.sbLeftPan = QtGui.QDoubleSpinBox(JointMotorDlg)
        self.sbLeftPan.setMinimum(-3.0)
        self.sbLeftPan.setMaximum(3.0)
        self.sbLeftPan.setSingleStep(0.05)
        self.sbLeftPan.setObjectName(_fromUtf8("sbLeftPan"))
        self.horizontalLayout.addWidget(self.sbLeftPan)
        self.label_5 = QtGui.QLabel(JointMotorDlg)
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout.addWidget(self.label_5)
        self.lcdLeftPan = QtGui.QLCDNumber(JointMotorDlg)
        self.lcdLeftPan.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdLeftPan.setObjectName(_fromUtf8("lcdLeftPan"))
        self.horizontalLayout.addWidget(self.lcdLeftPan)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_4 = QtGui.QLabel(JointMotorDlg)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.sbRightPan = QtGui.QDoubleSpinBox(JointMotorDlg)
        self.sbRightPan.setMinimum(-3.0)
        self.sbRightPan.setMaximum(3.0)
        self.sbRightPan.setSingleStep(0.05)
        self.sbRightPan.setObjectName(_fromUtf8("sbRightPan"))
        self.horizontalLayout_2.addWidget(self.sbRightPan)
        self.lcdRightPan = QtGui.QLCDNumber(JointMotorDlg)
        self.lcdRightPan.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdRightPan.setObjectName(_fromUtf8("lcdRightPan"))
        self.horizontalLayout_2.addWidget(self.lcdRightPan)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem = QtGui.QSpacerItem(40, 28, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.dbTilt = QtGui.QLabel(JointMotorDlg)
        self.dbTilt.setObjectName(_fromUtf8("dbTilt"))
        self.horizontalLayout_3.addWidget(self.dbTilt)
        self.sbTilt = QtGui.QDoubleSpinBox(JointMotorDlg)
        self.sbTilt.setMinimum(-3.0)
        self.sbTilt.setMaximum(3.0)
        self.sbTilt.setSingleStep(0.05)
        self.sbTilt.setObjectName(_fromUtf8("sbTilt"))
        self.horizontalLayout_3.addWidget(self.sbTilt)
        self.lcdTilt = QtGui.QLCDNumber(JointMotorDlg)
        self.lcdTilt.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdTilt.setObjectName(_fromUtf8("lcdTilt"))
        self.horizontalLayout_3.addWidget(self.lcdTilt)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_3)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_6, 1, 0, 1, 2)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.dbNeck = QtGui.QLabel(JointMotorDlg)
        self.dbNeck.setObjectName(_fromUtf8("dbNeck"))
        self.horizontalLayout_4.addWidget(self.dbNeck)
        self.sbNeck = QtGui.QDoubleSpinBox(JointMotorDlg)
        self.sbNeck.setMinimum(-3.0)
        self.sbNeck.setMaximum(3.0)
        self.sbNeck.setSingleStep(0.05)
        self.sbNeck.setObjectName(_fromUtf8("sbNeck"))
        self.horizontalLayout_4.addWidget(self.sbNeck)
        self.lcdNeck = QtGui.QLCDNumber(JointMotorDlg)
        self.lcdNeck.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdNeck.setObjectName(_fromUtf8("lcdNeck"))
        self.horizontalLayout_4.addWidget(self.lcdNeck)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout_5, 2, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(JointMotorDlg)
        QtCore.QMetaObject.connectSlotsByName(JointMotorDlg)

    def retranslateUi(self, JointMotorDlg):
        JointMotorDlg.setWindowTitle(_translate("JointMotorDlg", "JointMotor - Monitor", None))
        self.label_3.setText(_translate("JointMotorDlg", "Left Pan", None))
        self.label_4.setText(_translate("JointMotorDlg", "Right Pan", None))
        self.dbTilt.setText(_translate("JointMotorDlg", "Tilt   ", None))
        self.dbNeck.setText(_translate("JointMotorDlg", "Neck", None))

