# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ruben/robocomp/tools/rcmonitor/floorDlg.ui'
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

class Ui_floorDlg(object):
    def setupUi(self, floorDlg):
        floorDlg.setObjectName(_fromUtf8("floorDlg"))
        floorDlg.resize(418, 474)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(floorDlg.sizePolicy().hasHeightForWidth())
        floorDlg.setSizePolicy(sizePolicy)
        floorDlg.setMaximumSize(QtCore.QSize(418, 474))
        self.verticalLayout = QtGui.QVBoxLayout(floorDlg)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame = QtGui.QWidget(floorDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(40)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(400, 400))
        self.frame.setMaximumSize(QtCore.QSize(400, 400))
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.labelNavigation = QtGui.QLabel(floorDlg)
        self.labelNavigation.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.labelNavigation.setAlignment(QtCore.Qt.AlignCenter)
        self.labelNavigation.setObjectName(_fromUtf8("labelNavigation"))
        self.horizontalLayout.addWidget(self.labelNavigation)
        self.buttonNavigation = QtGui.QPushButton(floorDlg)
        self.buttonNavigation.setObjectName(_fromUtf8("buttonNavigation"))
        self.horizontalLayout.addWidget(self.buttonNavigation)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.labelTilt = QtGui.QLabel(floorDlg)
        self.labelTilt.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTilt.setObjectName(_fromUtf8("labelTilt"))
        self.horizontalLayout_2.addWidget(self.labelTilt)
        self.buttonTilt = QtGui.QPushButton(floorDlg)
        self.buttonTilt.setObjectName(_fromUtf8("buttonTilt"))
        self.horizontalLayout_2.addWidget(self.buttonTilt)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.checkVisible = QtGui.QCheckBox(floorDlg)
        self.checkVisible.setObjectName(_fromUtf8("checkVisible"))
        self.horizontalLayout_3.addWidget(self.checkVisible)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(floorDlg)
        QtCore.QMetaObject.connectSlotsByName(floorDlg)

    def retranslateUi(self, floorDlg):
        floorDlg.setWindowTitle(_translate("floorDlg", "JointMotor - Monitor", None))
        self.labelNavigation.setText(_translate("floorDlg", "---", None))
        self.buttonNavigation.setText(_translate("floorDlg", "switch", None))
        self.labelTilt.setText(_translate("floorDlg", "---", None))
        self.buttonTilt.setText(_translate("floorDlg", "switch", None))
        self.checkVisible.setText(_translate("floorDlg", "Visible", None))

