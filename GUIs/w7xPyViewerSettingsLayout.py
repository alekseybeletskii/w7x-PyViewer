# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'w7xPyViewerSettingsLayout.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_w7xPyViewerSettingsWidget(object):
    def setupUi(self, w7xPyViewerSettingsWidget):
        w7xPyViewerSettingsWidget.setObjectName("w7xPyViewerSettingsWidget")
        w7xPyViewerSettingsWidget.resize(660, 260)
        w7xPyViewerSettingsWidget.setMinimumSize(QtCore.QSize(660, 260))
        w7xPyViewerSettingsWidget.setMaximumSize(QtCore.QSize(660, 260))
        w7xPyViewerSettingsWidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Germany))
        self.widget = QtWidgets.QWidget(w7xPyViewerSettingsWidget)
        self.widget.setGeometry(QtCore.QRect(0, 10, 648, 242))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_19 = QtWidgets.QLabel(self.widget)
        self.label_19.setMinimumSize(QtCore.QSize(90, 0))
        self.label_19.setMaximumSize(QtCore.QSize(90, 15))
        self.label_19.setSizeIncrement(QtCore.QSize(0, 0))
        self.label_19.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 0, 0, 1, 1, QtCore.Qt.AlignRight)
        self.dataSource_ui = QtWidgets.QComboBox(self.widget)
        self.dataSource_ui.setObjectName("dataSource_ui")
        self.dataSource_ui.addItem("")
        self.dataSource_ui.addItem("")
        self.dataSource_ui.addItem("")
        self.gridLayout.addWidget(self.dataSource_ui, 0, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.widget)
        self.label_21.setMinimumSize(QtCore.QSize(180, 20))
        self.label_21.setMaximumSize(QtCore.QSize(180, 20))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 1, 2, 1, 2, QtCore.Qt.AlignHCenter)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setMinimumSize(QtCore.QSize(50, 15))
        self.label_2.setMaximumSize(QtCore.QSize(50, 15))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1, QtCore.Qt.AlignRight)
        self.shotNum_ui = QtWidgets.QLineEdit(self.widget)
        self.shotNum_ui.setMinimumSize(QtCore.QSize(80, 20))
        self.shotNum_ui.setMaximumSize(QtCore.QSize(80, 20))
        self.shotNum_ui.setAutoFillBackground(False)
        self.shotNum_ui.setFrame(True)
        self.shotNum_ui.setObjectName("shotNum_ui")
        self.gridLayout.addWidget(self.shotNum_ui, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMinimumSize(QtCore.QSize(150, 15))
        self.label.setMaximumSize(QtCore.QSize(120, 100))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 2, 1, 1, QtCore.Qt.AlignRight)
        self.treeName_ui = QtWidgets.QLineEdit(self.widget)
        self.treeName_ui.setMinimumSize(QtCore.QSize(60, 20))
        self.treeName_ui.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.treeName_ui.setFont(font)
        self.treeName_ui.setPlaceholderText("")
        self.treeName_ui.setObjectName("treeName_ui")
        self.gridLayout.addWidget(self.treeName_ui, 2, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setMinimumSize(QtCore.QSize(50, 15))
        self.label_4.setMaximumSize(QtCore.QSize(50, 15))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1, QtCore.Qt.AlignRight)
        self.startMdsplusTime_ui = QtWidgets.QLineEdit(self.widget)
        self.startMdsplusTime_ui.setMinimumSize(QtCore.QSize(80, 20))
        self.startMdsplusTime_ui.setMaximumSize(QtCore.QSize(80, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.startMdsplusTime_ui.setFont(font)
        self.startMdsplusTime_ui.setPlaceholderText("")
        self.startMdsplusTime_ui.setObjectName("startMdsplusTime_ui")
        self.gridLayout.addWidget(self.startMdsplusTime_ui, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setMinimumSize(QtCore.QSize(50, 15))
        self.label_5.setMaximumSize(QtCore.QSize(50, 15))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 2, 1, 1, QtCore.Qt.AlignRight)
        self.endMdsplusTime_ui = QtWidgets.QLineEdit(self.widget)
        self.endMdsplusTime_ui.setMinimumSize(QtCore.QSize(60, 20))
        self.endMdsplusTime_ui.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.endMdsplusTime_ui.setFont(font)
        self.endMdsplusTime_ui.setPlaceholderText("")
        self.endMdsplusTime_ui.setObjectName("endMdsplusTime_ui")
        self.gridLayout.addWidget(self.endMdsplusTime_ui, 3, 3, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.widget)
        self.label_22.setMinimumSize(QtCore.QSize(60, 15))
        self.label_22.setMaximumSize(QtCore.QSize(60, 15))
        self.label_22.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 3, 4, 1, 1, QtCore.Qt.AlignRight)
        self.deltaMdsplusTime_ui = QtWidgets.QLineEdit(self.widget)
        self.deltaMdsplusTime_ui.setMinimumSize(QtCore.QSize(80, 20))
        self.deltaMdsplusTime_ui.setMaximumSize(QtCore.QSize(80, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.deltaMdsplusTime_ui.setFont(font)
        self.deltaMdsplusTime_ui.setPlaceholderText("")
        self.deltaMdsplusTime_ui.setObjectName("deltaMdsplusTime_ui")
        self.gridLayout.addWidget(self.deltaMdsplusTime_ui, 3, 5, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.widget)
        self.label_23.setMinimumSize(QtCore.QSize(150, 20))
        self.label_23.setMaximumSize(QtCore.QSize(150, 20))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_23.setFont(font)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 4, 2, 1, 2, QtCore.Qt.AlignHCenter)
        self.label_15 = QtWidgets.QLabel(self.widget)
        self.label_15.setMinimumSize(QtCore.QSize(130, 15))
        self.label_15.setMaximumSize(QtCore.QSize(130, 15))
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 5, 0, 1, 1, QtCore.Qt.AlignRight)
        self.applyDownsampling_ui = QtWidgets.QCheckBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(60)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.applyDownsampling_ui.sizePolicy().hasHeightForWidth())
        self.applyDownsampling_ui.setSizePolicy(sizePolicy)
        self.applyDownsampling_ui.setMinimumSize(QtCore.QSize(60, 20))
        self.applyDownsampling_ui.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.applyDownsampling_ui.setText("")
        self.applyDownsampling_ui.setTristate(False)
        self.applyDownsampling_ui.setObjectName("applyDownsampling_ui")
        self.gridLayout.addWidget(self.applyDownsampling_ui, 5, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.widget)
        self.label_14.setMinimumSize(QtCore.QSize(100, 0))
        self.label_14.setMaximumSize(QtCore.QSize(60, 15))
        self.label_14.setSizeIncrement(QtCore.QSize(0, 0))
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 5, 2, 1, 1, QtCore.Qt.AlignRight)
        self.targetFrq_kHz_ui = QtWidgets.QLineEdit(self.widget)
        self.targetFrq_kHz_ui.setMinimumSize(QtCore.QSize(60, 20))
        self.targetFrq_kHz_ui.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.targetFrq_kHz_ui.setFont(font)
        self.targetFrq_kHz_ui.setPlaceholderText("")
        self.targetFrq_kHz_ui.setObjectName("targetFrq_kHz_ui")
        self.gridLayout.addWidget(self.targetFrq_kHz_ui, 5, 3, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.widget)
        self.label_24.setMinimumSize(QtCore.QSize(175, 20))
        self.label_24.setMaximumSize(QtCore.QSize(175, 20))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_24.setFont(font)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 6, 2, 1, 2, QtCore.Qt.AlignHCenter)
        self.label_17 = QtWidgets.QLabel(self.widget)
        self.label_17.setMinimumSize(QtCore.QSize(80, 0))
        self.label_17.setMaximumSize(QtCore.QSize(80, 15))
        self.label_17.setSizeIncrement(QtCore.QSize(0, 0))
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 7, 0, 1, 1, QtCore.Qt.AlignRight)
        self.sgFilterWindow_ui = QtWidgets.QLineEdit(self.widget)
        self.sgFilterWindow_ui.setMinimumSize(QtCore.QSize(80, 20))
        self.sgFilterWindow_ui.setMaximumSize(QtCore.QSize(80, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.sgFilterWindow_ui.setFont(font)
        self.sgFilterWindow_ui.setPlaceholderText("")
        self.sgFilterWindow_ui.setObjectName("sgFilterWindow_ui")
        self.gridLayout.addWidget(self.sgFilterWindow_ui, 7, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.widget)
        self.label_18.setMinimumSize(QtCore.QSize(90, 0))
        self.label_18.setMaximumSize(QtCore.QSize(90, 15))
        self.label_18.setSizeIncrement(QtCore.QSize(0, 0))
        self.label_18.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 7, 2, 1, 1, QtCore.Qt.AlignRight)
        self.sgFilterPolyOrder_ui = QtWidgets.QLineEdit(self.widget)
        self.sgFilterPolyOrder_ui.setMinimumSize(QtCore.QSize(60, 20))
        self.sgFilterPolyOrder_ui.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.sgFilterPolyOrder_ui.setFont(font)
        self.sgFilterPolyOrder_ui.setPlaceholderText("")
        self.sgFilterPolyOrder_ui.setObjectName("sgFilterPolyOrder_ui")
        self.gridLayout.addWidget(self.sgFilterPolyOrder_ui, 7, 3, 1, 1)
        self.line_7 = QtWidgets.QFrame(self.widget)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout.addWidget(self.line_7, 8, 0, 1, 7)
        self.getFromUiApplyAndClose_btn = QtWidgets.QPushButton(self.widget)
        self.getFromUiApplyAndClose_btn.setMinimumSize(QtCore.QSize(50, 20))
        self.getFromUiApplyAndClose_btn.setMaximumSize(QtCore.QSize(50, 20))
        self.getFromUiApplyAndClose_btn.setObjectName("getFromUiApplyAndClose_btn")
        self.gridLayout.addWidget(self.getFromUiApplyAndClose_btn, 9, 4, 1, 1)
        self.saveSettings_btn = QtWidgets.QPushButton(self.widget)
        self.saveSettings_btn.setMinimumSize(QtCore.QSize(80, 20))
        self.saveSettings_btn.setMaximumSize(QtCore.QSize(80, 20))
        self.saveSettings_btn.setObjectName("saveSettings_btn")
        self.gridLayout.addWidget(self.saveSettings_btn, 9, 5, 1, 1)
        self.resetSetings_btn = QtWidgets.QPushButton(self.widget)
        self.resetSetings_btn.setMinimumSize(QtCore.QSize(50, 20))
        self.resetSetings_btn.setMaximumSize(QtCore.QSize(50, 20))
        self.resetSetings_btn.setObjectName("resetSetings_btn")
        self.gridLayout.addWidget(self.resetSetings_btn, 9, 6, 1, 1)

        self.retranslateUi(w7xPyViewerSettingsWidget)
        QtCore.QMetaObject.connectSlotsByName(w7xPyViewerSettingsWidget)

    def retranslateUi(self, w7xPyViewerSettingsWidget):
        _translate = QtCore.QCoreApplication.translate
        w7xPyViewerSettingsWidget.setWindowTitle(_translate("w7xPyViewerSettingsWidget", "w7xPyViewerSettings"))
        self.label_19.setText(_translate("w7xPyViewerSettingsWidget", "data source"))
        self.dataSource_ui.setItemText(0, _translate("w7xPyViewerSettingsWidget", "csv_txt"))
        self.dataSource_ui.setItemText(1, _translate("w7xPyViewerSettingsWidget", "MDSPlus"))
        self.dataSource_ui.setItemText(2, _translate("w7xPyViewerSettingsWidget", "LGraph2"))
        self.label_21.setText(_translate("w7xPyViewerSettingsWidget", "MDSPlus configuration"))
        self.label_2.setText(_translate("w7xPyViewerSettingsWidget", "shot#"))
        self.shotNum_ui.setText(_translate("w7xPyViewerSettingsWidget", "180906039"))
        self.label.setText(_translate("w7xPyViewerSettingsWidget", "tree(qoc, qxt1, qsr02)"))
        self.treeName_ui.setText(_translate("w7xPyViewerSettingsWidget", "qoc"))
        self.label_4.setText(_translate("w7xPyViewerSettingsWidget", "start, s"))
        self.startMdsplusTime_ui.setText(_translate("w7xPyViewerSettingsWidget", "*"))
        self.label_5.setText(_translate("w7xPyViewerSettingsWidget", "end, s"))
        self.endMdsplusTime_ui.setText(_translate("w7xPyViewerSettingsWidget", "*"))
        self.label_22.setText(_translate("w7xPyViewerSettingsWidget", "delta, cnt"))
        self.deltaMdsplusTime_ui.setText(_translate("w7xPyViewerSettingsWidget", "*"))
        self.label_23.setText(_translate("w7xPyViewerSettingsWidget", "Resampling"))
        self.label_15.setText(_translate("w7xPyViewerSettingsWidget", "apply downsampling"))
        self.label_14.setText(_translate("w7xPyViewerSettingsWidget", "target frq, kHz"))
        self.targetFrq_kHz_ui.setText(_translate("w7xPyViewerSettingsWidget", "500"))
        self.label_24.setText(_translate("w7xPyViewerSettingsWidget", "SGFilter configuration"))
        self.label_17.setText(_translate("w7xPyViewerSettingsWidget", "window, cnt"))
        self.sgFilterWindow_ui.setToolTip(_translate("w7xPyViewerSettingsWidget", "*SxxMax"))
        self.sgFilterWindow_ui.setText(_translate("w7xPyViewerSettingsWidget", "101"))
        self.label_18.setText(_translate("w7xPyViewerSettingsWidget", "polynom order"))
        self.sgFilterPolyOrder_ui.setToolTip(_translate("w7xPyViewerSettingsWidget", "*SxxMax"))
        self.sgFilterPolyOrder_ui.setText(_translate("w7xPyViewerSettingsWidget", "1"))
        self.getFromUiApplyAndClose_btn.setText(_translate("w7xPyViewerSettingsWidget", "ok"))
        self.saveSettings_btn.setText(_translate("w7xPyViewerSettingsWidget", "save to file"))
        self.resetSetings_btn.setText(_translate("w7xPyViewerSettingsWidget", "reset"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w7xPyViewerSettingsWidget = QtWidgets.QWidget()
    ui = Ui_w7xPyViewerSettingsWidget()
    ui.setupUi(w7xPyViewerSettingsWidget)
    w7xPyViewerSettingsWidget.show()
    sys.exit(app.exec_())

