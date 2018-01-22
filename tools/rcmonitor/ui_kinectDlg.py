# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ruben/robocomp/tools/rcmonitor/kinectDlg.ui'
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

class Ui_KinectDlg(object):
    def setupUi(self, KinectDlg):
        KinectDlg.setObjectName(_fromUtf8("KinectDlg"))
        KinectDlg.resize(1326, 708)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(KinectDlg.sizePolicy().hasHeightForWidth())
        KinectDlg.setSizePolicy(sizePolicy)
        KinectDlg.setMaximumSize(QtCore.QSize(4800, 44444))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(KinectDlg)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem = QtGui.QSpacerItem(1, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(20, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.frameRGB = QtGui.QFrame(KinectDlg)
        self.frameRGB.setMinimumSize(QtCore.QSize(640, 480))
        self.frameRGB.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameRGB.setFrameShadow(QtGui.QFrame.Raised)
        self.frameRGB.setObjectName(_fromUtf8("frameRGB"))
        self.horizontalLayout_3.addWidget(self.frameRGB)
        self.frame = QtGui.QFrame(KinectDlg)
        self.frame.setMinimumSize(QtCore.QSize(640, 480))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout_3.addWidget(self.frame)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.nameRGBD = QtGui.QLabel(KinectDlg)
        self.nameRGBD.setObjectName(_fromUtf8("nameRGBD"))
        self.horizontalLayout.addWidget(self.nameRGBD)
        self.label_3 = QtGui.QLabel(KinectDlg)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.sbTilt = QtGui.QDoubleSpinBox(KinectDlg)
        self.sbTilt.setDecimals(0)
        self.sbTilt.setMinimum(-31.0)
        self.sbTilt.setMaximum(31.0)
        self.sbTilt.setSingleStep(1.0)
        self.sbTilt.setObjectName(_fromUtf8("sbTilt"))
        self.horizontalLayout.addWidget(self.sbTilt)
        self.lcdTilt = QtGui.QLCDNumber(KinectDlg)
        self.lcdTilt.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdTilt.setObjectName(_fromUtf8("lcdTilt"))
        self.horizontalLayout.addWidget(self.lcdTilt)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pbSetLed = QtGui.QPushButton(KinectDlg)
        self.pbSetLed.setObjectName(_fromUtf8("pbSetLed"))
        self.horizontalLayout_2.addWidget(self.pbSetLed)
        self.label_4 = QtGui.QLabel(KinectDlg)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.cbLedOpt = QtGui.QComboBox(KinectDlg)
        self.cbLedOpt.setObjectName(_fromUtf8("cbLedOpt"))
        self.horizontalLayout_2.addWidget(self.cbLedOpt)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem4 = QtGui.QSpacerItem(20, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem5 = QtGui.QSpacerItem(1, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)

        self.retranslateUi(KinectDlg)
        QtCore.QMetaObject.connectSlotsByName(KinectDlg)

    def retranslateUi(self, KinectDlg):
        KinectDlg.setWindowTitle(_translate("KinectDlg", "Kinect Controller", None))
        self.nameRGBD.setText(_translate("KinectDlg", "RGBD ", None))
        self.label_3.setText(_translate("KinectDlg", "Tilt", None))
        self.pbSetLed.setText(_translate("KinectDlg", "Set LED", None))
        self.label_4.setText(_translate("KinectDlg", "S2", None))

