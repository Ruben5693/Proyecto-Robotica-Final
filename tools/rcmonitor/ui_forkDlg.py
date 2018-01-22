# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ruben/robocomp/tools/rcmonitor/forkDlg.ui'
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

class Ui_forkDlg(object):
    def setupUi(self, forkDlg):
        forkDlg.setObjectName(_fromUtf8("forkDlg"))
        forkDlg.resize(360, 164)
        self.gridLayout_2 = QtGui.QGridLayout(forkDlg)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox_2 = QtGui.QGroupBox(forkDlg)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.sbSpeed = QtGui.QSpinBox(self.groupBox_2)
        self.sbSpeed.setMinimum(-900)
        self.sbSpeed.setMaximum(900)
        self.sbSpeed.setObjectName(_fromUtf8("sbSpeed"))
        self.verticalLayout_2.addWidget(self.sbSpeed)
        self.pbSpeed = QtGui.QPushButton(self.groupBox_2)
        self.pbSpeed.setObjectName(_fromUtf8("pbSpeed"))
        self.verticalLayout_2.addWidget(self.pbSpeed)
        self.pbStop = QtGui.QPushButton(self.groupBox_2)
        self.pbStop.setObjectName(_fromUtf8("pbStop"))
        self.verticalLayout_2.addWidget(self.pbStop)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.groupBox = QtGui.QGroupBox(forkDlg)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lcdPos = QtGui.QLCDNumber(self.groupBox)
        self.lcdPos.setObjectName(_fromUtf8("lcdPos"))
        self.verticalLayout.addWidget(self.lcdPos)
        self.sbPos = QtGui.QSpinBox(self.groupBox)
        self.sbPos.setMaximum(100)
        self.sbPos.setObjectName(_fromUtf8("sbPos"))
        self.verticalLayout.addWidget(self.sbPos)
        self.pbGoPos = QtGui.QPushButton(self.groupBox)
        self.pbGoPos.setObjectName(_fromUtf8("pbGoPos"))
        self.verticalLayout.addWidget(self.pbGoPos)
        self.horizontalLayout.addWidget(self.groupBox)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.pbSetZeroPos = QtGui.QPushButton(forkDlg)
        self.pbSetZeroPos.setObjectName(_fromUtf8("pbSetZeroPos"))
        self.verticalLayout_3.addWidget(self.pbSetZeroPos)
        self.pbGoUp = QtGui.QPushButton(forkDlg)
        self.pbGoUp.setObjectName(_fromUtf8("pbGoUp"))
        self.verticalLayout_3.addWidget(self.pbGoUp)
        self.pbGoDown = QtGui.QPushButton(forkDlg)
        self.pbGoDown.setObjectName(_fromUtf8("pbGoDown"))
        self.verticalLayout_3.addWidget(self.pbGoDown)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 1, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 1, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 2, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(1, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 2, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(1, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 1, 0, 1, 1)

        self.retranslateUi(forkDlg)
        QtCore.QMetaObject.connectSlotsByName(forkDlg)

    def retranslateUi(self, forkDlg):
        forkDlg.setWindowTitle(_translate("forkDlg", "Form", None))
        self.groupBox_2.setTitle(_translate("forkDlg", "Speed", None))
        self.pbSpeed.setText(_translate("forkDlg", "setSpeed", None))
        self.pbStop.setText(_translate("forkDlg", "stop", None))
        self.groupBox.setTitle(_translate("forkDlg", "Position", None))
        self.pbGoPos.setText(_translate("forkDlg", "goPos", None))
        self.pbSetZeroPos.setText(_translate("forkDlg", "setUpPos", None))
        self.pbGoUp.setText(_translate("forkDlg", "goUp", None))
        self.pbGoDown.setText(_translate("forkDlg", "goDown", None))

