# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pomodoro.ui'
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

class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName(_fromUtf8("main_window"))
        main_window.setWindowModality(QtCore.Qt.NonModal)
        main_window.resize(693, 588)
        main_window.setLayoutDirection(QtCore.Qt.LeftToRight)
        main_window.setAutoFillBackground(False)
        self.horizontalLayout = QtGui.QHBoxLayout(main_window)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tabWidget = QtGui.QTabWidget(main_window)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_hours = QtGui.QLabel(self.tab_2)
        self.label_hours.setObjectName(_fromUtf8("label_hours"))
        self.horizontalLayout_5.addWidget(self.label_hours)
        self.spinBox_hours = QtGui.QSpinBox(self.tab_2)
        self.spinBox_hours.setObjectName(_fromUtf8("spinBox_hours"))
        self.horizontalLayout_5.addWidget(self.spinBox_hours)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.pushButton_1 = QtGui.QPushButton(self.tab_2)
        self.pushButton_1.setObjectName(_fromUtf8("pushButton_1"))
        self.verticalLayout_3.addWidget(self.pushButton_1)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_minutes = QtGui.QLabel(self.tab_2)
        self.label_minutes.setObjectName(_fromUtf8("label_minutes"))
        self.horizontalLayout_7.addWidget(self.label_minutes)
        self.spinBox_minutes = QtGui.QSpinBox(self.tab_2)
        self.spinBox_minutes.setObjectName(_fromUtf8("spinBox_minutes"))
        self.horizontalLayout_7.addWidget(self.spinBox_minutes)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.pushButton_2 = QtGui.QPushButton(self.tab_2)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout_4.addWidget(self.pushButton_2)
        self.horizontalLayout_6.addLayout(self.verticalLayout_4)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_6)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_seconds = QtGui.QLabel(self.tab_2)
        self.label_seconds.setObjectName(_fromUtf8("label_seconds"))
        self.horizontalLayout_9.addWidget(self.label_seconds)
        self.spinBox_seconds = QtGui.QSpinBox(self.tab_2)
        self.spinBox_seconds.setObjectName(_fromUtf8("spinBox_seconds"))
        self.horizontalLayout_9.addWidget(self.spinBox_seconds)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.pushButton_3 = QtGui.QPushButton(self.tab_2)
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.verticalLayout_5.addWidget(self.pushButton_3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.lcdNumber = QtGui.QLCDNumber(self.tab_2)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.verticalLayout.addWidget(self.lcdNumber)
        self.verticalLayout_6.addLayout(self.verticalLayout)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.tabWidget)

        self.retranslateUi(main_window)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(_translate("main_window", "Countdown Timer", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("main_window", "Pomodoro", None))
        self.label_hours.setText(_translate("main_window", "Hours:", None))
        self.pushButton_1.setText(_translate("main_window", "Start", None))
        self.label_minutes.setText(_translate("main_window", "Minutes:", None))
        self.pushButton_2.setText(_translate("main_window", "Pause", None))
        self.label_seconds.setText(_translate("main_window", "Seconds:", None))
        self.pushButton_3.setText(_translate("main_window", "Stop", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("main_window", "Countdown", None))

