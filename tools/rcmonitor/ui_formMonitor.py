# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ruben/robocomp/tools/rcmonitor/formMonitor.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(800, 600)
        self.centralwidget = QtGui.QWidget(Form)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.mdiArea = QtGui.QMdiArea(self.centralwidget)
        self.mdiArea.setObjectName(_fromUtf8("mdiArea"))
        self.verticalLayout.addWidget(self.mdiArea)
        Form.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Form)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuConnection = QtGui.QMenu(self.menubar)
        self.menuConnection.setObjectName(_fromUtf8("menuConnection"))
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        self.menuTemplates = QtGui.QMenu(self.menubar)
        self.menuTemplates.setObjectName(_fromUtf8("menuTemplates"))
        Form.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Form)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Form.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(Form)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionClose = QtGui.QAction(Form)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionExit = QtGui.QAction(Form)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionPeriod = QtGui.QAction(Form)
        self.actionPeriod.setObjectName(_fromUtf8("actionPeriod"))
        self.actionBase_pose = QtGui.QAction(Form)
        self.actionBase_pose.setObjectName(_fromUtf8("actionBase_pose"))
        self.actionCamera_RGB_Image = QtGui.QAction(Form)
        self.actionCamera_RGB_Image.setObjectName(_fromUtf8("actionCamera_RGB_Image"))
        self.actionCamera_Grey_Image = QtGui.QAction(Form)
        self.actionCamera_Grey_Image.setObjectName(_fromUtf8("actionCamera_Grey_Image"))
        self.actionCustom = QtGui.QAction(Form)
        self.actionCustom.setObjectName(_fromUtf8("actionCustom"))
        self.actionSignal = QtGui.QAction(Form)
        self.actionSignal.setObjectName(_fromUtf8("actionSignal"))
        self.actionLaser = QtGui.QAction(Form)
        self.actionLaser.setObjectName(_fromUtf8("actionLaser"))
        self.menuConnection.addAction(self.actionOpen)
        self.menuConnection.addAction(self.actionClose)
        self.menuConnection.addSeparator()
        self.menuConnection.addAction(self.actionExit)
        self.menuSettings.addAction(self.actionPeriod)
        self.menuTemplates.addAction(self.actionBase_pose)
        self.menuTemplates.addAction(self.actionCamera_RGB_Image)
        self.menuTemplates.addAction(self.actionCamera_Grey_Image)
        self.menuTemplates.addAction(self.actionSignal)
        self.menuTemplates.addAction(self.actionCustom)
        self.menuTemplates.addSeparator()
        self.menuTemplates.addAction(self.actionLaser)
        self.menubar.addAction(self.menuConnection.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuTemplates.menuAction())

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Monitor - RoboComp", None))
        self.menuConnection.setTitle(_translate("Form", "&Connection", None))
        self.menuSettings.setTitle(_translate("Form", "&Settings", None))
        self.menuTemplates.setTitle(_translate("Form", "&Templates", None))
        self.actionOpen.setText(_translate("Form", "&Open", None))
        self.actionClose.setText(_translate("Form", "&Close", None))
        self.actionExit.setText(_translate("Form", "E&xit", None))
        self.actionPeriod.setText(_translate("Form", "&Period", None))
        self.actionBase_pose.setText(_translate("Form", "Base pose", None))
        self.actionCamera_RGB_Image.setText(_translate("Form", "Camera RGB Image", None))
        self.actionCamera_Grey_Image.setText(_translate("Form", "Camera Grey Image", None))
        self.actionCustom.setText(_translate("Form", "Custom output", None))
        self.actionSignal.setText(_translate("Form", "Signal", None))
        self.actionLaser.setText(_translate("Form", "Laser", None))

