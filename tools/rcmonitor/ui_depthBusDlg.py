# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ruben/robocomp/tools/rcmonitor/depthBusDlg.ui'
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

class Ui_DepthBusDlg(object):
    def setupUi(self, DepthBusDlg):
        DepthBusDlg.setObjectName(_fromUtf8("DepthBusDlg"))
        DepthBusDlg.resize(1470, 934)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DepthBusDlg.sizePolicy().hasHeightForWidth())
        DepthBusDlg.setSizePolicy(sizePolicy)
        DepthBusDlg.setMaximumSize(QtCore.QSize(4800, 44444))
        self.frame0 = QtGui.QFrame(DepthBusDlg)
        self.frame0.setEnabled(True)
        self.frame0.setGeometry(QtCore.QRect(100, 0, 640, 480))
        self.frame0.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame0.setFrameShadow(QtGui.QFrame.Raised)
        self.frame0.setObjectName(_fromUtf8("frame0"))
        self.frame1 = QtGui.QFrame(DepthBusDlg)
        self.frame1.setEnabled(True)
        self.frame1.setGeometry(QtCore.QRect(740, 0, 640, 480))
        self.frame1.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame1.setFrameShadow(QtGui.QFrame.Raised)
        self.frame1.setObjectName(_fromUtf8("frame1"))
        self.frame2 = QtGui.QFrame(DepthBusDlg)
        self.frame2.setEnabled(True)
        self.frame2.setGeometry(QtCore.QRect(100, 480, 640, 480))
        self.frame2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame2.setObjectName(_fromUtf8("frame2"))
        self.frame4 = QtGui.QFrame(DepthBusDlg)
        self.frame4.setEnabled(True)
        self.frame4.setGeometry(QtCore.QRect(740, 480, 640, 480))
        self.frame4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame4.setObjectName(_fromUtf8("frame4"))
        self.nameDepth0 = QtGui.QLabel(DepthBusDlg)
        self.nameDepth0.setGeometry(QtCore.QRect(0, 10, 91, 81))
        self.nameDepth0.setTextFormat(QtCore.Qt.AutoText)
        self.nameDepth0.setScaledContents(False)
        self.nameDepth0.setObjectName(_fromUtf8("nameDepth0"))
        self.nameDepth2 = QtGui.QLabel(DepthBusDlg)
        self.nameDepth2.setGeometry(QtCore.QRect(0, 490, 91, 81))
        self.nameDepth2.setScaledContents(False)
        self.nameDepth2.setObjectName(_fromUtf8("nameDepth2"))
        self.nameDepth1 = QtGui.QLabel(DepthBusDlg)
        self.nameDepth1.setGeometry(QtCore.QRect(1380, 0, 91, 81))
        self.nameDepth1.setScaledContents(False)
        self.nameDepth1.setObjectName(_fromUtf8("nameDepth1"))
        self.nameDepth3 = QtGui.QLabel(DepthBusDlg)
        self.nameDepth3.setGeometry(QtCore.QRect(1380, 490, 91, 81))
        self.nameDepth3.setScaledContents(False)
        self.nameDepth3.setObjectName(_fromUtf8("nameDepth3"))

        self.retranslateUi(DepthBusDlg)
        QtCore.QMetaObject.connectSlotsByName(DepthBusDlg)

    def retranslateUi(self, DepthBusDlg):
        DepthBusDlg.setWindowTitle(_translate("DepthBusDlg", "depth bus", None))
        self.nameDepth0.setText(_translate("DepthBusDlg", "TextLabel", None))
        self.nameDepth2.setText(_translate("DepthBusDlg", "TextLabel", None))
        self.nameDepth1.setText(_translate("DepthBusDlg", "TextLabel", None))
        self.nameDepth3.setText(_translate("DepthBusDlg", "TextLabel", None))

