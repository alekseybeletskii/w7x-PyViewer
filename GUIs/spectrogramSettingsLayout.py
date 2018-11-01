# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spectrogramSettingsLayout.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_spectrogramSettingsWidget(object):
    def setupUi(self, spectrogramSettingsWidget):
        spectrogramSettingsWidget.setObjectName("spectrogramSettingsWidget")
        spectrogramSettingsWidget.resize(720, 410)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(spectrogramSettingsWidget.sizePolicy().hasHeightForWidth())
        spectrogramSettingsWidget.setSizePolicy(sizePolicy)
        spectrogramSettingsWidget.setMinimumSize(QtCore.QSize(720, 410))
        spectrogramSettingsWidget.setMaximumSize(QtCore.QSize(720, 410))
        spectrogramSettingsWidget.setBaseSize(QtCore.QSize(680, 410))
        self.layoutWidget = QtWidgets.QWidget(spectrogramSettingsWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 11, 704, 389))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_24 = QtWidgets.QLabel(self.layoutWidget)
        self.label_24.setMinimumSize(QtCore.QSize(50, 15))
        self.label_24.setMaximumSize(QtCore.QSize(50, 15))
        self.label_24.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 0, 0, 1, 1, QtCore.Qt.AlignRight)
        self.shotNum_ui = QtWidgets.QLineEdit(self.layoutWidget)
        self.shotNum_ui.setMinimumSize(QtCore.QSize(60, 20))
        self.shotNum_ui.setMaximumSize(QtCore.QSize(60, 20))
        self.shotNum_ui.setAutoFillBackground(False)
        self.shotNum_ui.setFrame(True)
        self.shotNum_ui.setObjectName("shotNum_ui")
        self.gridLayout.addWidget(self.shotNum_ui, 0, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.layoutWidget)
        self.label_21.setMinimumSize(QtCore.QSize(120, 15))
        self.label_21.setMaximumSize(QtCore.QSize(120, 100))
        self.label_21.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 0, 2, 1, 1, QtCore.Qt.AlignRight)
        self.treeName_ui = QtWidgets.QLineEdit(self.layoutWidget)
        self.treeName_ui.setMinimumSize(QtCore.QSize(60, 20))
        self.treeName_ui.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.treeName_ui.setFont(font)
        self.treeName_ui.setPlaceholderText("")
        self.treeName_ui.setObjectName("treeName_ui")
        self.gridLayout.addWidget(self.treeName_ui, 0, 3, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.layoutWidget)
        self.label_23.setMinimumSize(QtCore.QSize(50, 15))
        self.label_23.setMaximumSize(QtCore.QSize(50, 15))
        self.label_23.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 1, 0, 1, 1, QtCore.Qt.AlignRight)
        self.startMdsplusTime_ui = QtWidgets.QLineEdit(self.layoutWidget)
        self.startMdsplusTime_ui.setMinimumSize(QtCore.QSize(60, 20))
        self.startMdsplusTime_ui.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.startMdsplusTime_ui.setFont(font)
        self.startMdsplusTime_ui.setPlaceholderText("")
        self.startMdsplusTime_ui.setObjectName("startMdsplusTime_ui")
        self.gridLayout.addWidget(self.startMdsplusTime_ui, 1, 1, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.layoutWidget)
        self.label_25.setMinimumSize(QtCore.QSize(50, 15))
        self.label_25.setMaximumSize(QtCore.QSize(50, 15))
        self.label_25.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 1, 2, 1, 1, QtCore.Qt.AlignRight)
        self.endMdsplusTime_ui = QtWidgets.QLineEdit(self.layoutWidget)
        self.endMdsplusTime_ui.setMinimumSize(QtCore.QSize(60, 20))
        self.endMdsplusTime_ui.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.endMdsplusTime_ui.setFont(font)
        self.endMdsplusTime_ui.setPlaceholderText("")
        self.endMdsplusTime_ui.setObjectName("endMdsplusTime_ui")
        self.gridLayout.addWidget(self.endMdsplusTime_ui, 1, 3, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.layoutWidget)
        self.label_22.setMinimumSize(QtCore.QSize(50, 15))
        self.label_22.setMaximumSize(QtCore.QSize(50, 15))
        self.label_22.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 1, 4, 1, 1, QtCore.Qt.AlignRight)
        self.deltaMdsplusTime_ui = QtWidgets.QLineEdit(self.layoutWidget)
        self.deltaMdsplusTime_ui.setMinimumSize(QtCore.QSize(80, 20))
        self.deltaMdsplusTime_ui.setMaximumSize(QtCore.QSize(80, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.deltaMdsplusTime_ui.setFont(font)
        self.deltaMdsplusTime_ui.setPlaceholderText("")
        self.deltaMdsplusTime_ui.setObjectName("deltaMdsplusTime_ui")
        self.gridLayout.addWidget(self.deltaMdsplusTime_ui, 1, 5, 1, 2)
        self.line_8 = QtWidgets.QFrame(self.layoutWidget)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.gridLayout.addWidget(self.line_8, 2, 0, 1, 9)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(130, 15))
        self.label_2.setMaximumSize(QtCore.QSize(130, 15))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1, QtCore.Qt.AlignRight)
        self.fs_kHz_ui = QtWidgets.QLineEdit(self.layoutWidget)
        self.fs_kHz_ui.setMinimumSize(QtCore.QSize(60, 20))
        self.fs_kHz_ui.setMaximumSize(QtCore.QSize(60, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.fs_kHz_ui.setPalette(palette)
        self.fs_kHz_ui.setAutoFillBackground(False)
        self.fs_kHz_ui.setFrame(True)
        self.fs_kHz_ui.setObjectName("fs_kHz_ui")
        self.gridLayout.addWidget(self.fs_kHz_ui, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setMinimumSize(QtCore.QSize(50, 15))
        self.label.setMaximumSize(QtCore.QSize(50, 15))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 2, 1, 1, QtCore.Qt.AlignRight)
        self.nfft_ui = QtWidgets.QLineEdit(self.layoutWidget)
        self.nfft_ui.setMinimumSize(QtCore.QSize(60, 20))
        self.nfft_ui.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.nfft_ui.setFont(font)
        self.nfft_ui.setPlaceholderText("")
        self.nfft_ui.setObjectName("nfft_ui")
        self.gridLayout.addWidget(self.nfft_ui, 3, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(50, 15))
        self.label_4.setMaximumSize(QtCore.QSize(50, 15))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 4, 1, 1, QtCore.Qt.AlignRight)
        self.nperseg_ui = QtWidgets.QLineEdit(self.layoutWidget)
        self.nperseg_ui.setMinimumSize(QtCore.QSize(60, 20))
        self.nperseg_ui.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.nperseg_ui.setFont(font)
        self.nperseg_ui.setPlaceholderText("")
        self.nperseg_ui.setObjectName("nperseg_ui")
        self.gridLayout.addWidget(self.nperseg_ui, 3, 5, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setMinimumSize(QtCore.QSize(50, 15))
        self.label_5.setMaximumSize(QtCore.QSize(50, 15))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 7, 1, 1, QtCore.Qt.AlignRight)
        self.noverlap_ui = QtWidgets.QLineEdit(self.layoutWidget)
        self.noverlap_ui.setMinimumSize(QtCore.QSize(60, 20))
        self.noverlap_ui.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.noverlap_ui.setFont(font)
        self.noverlap_ui.setPlaceholderText("")
        self.noverlap_ui.setObjectName("noverlap_ui")
        self.gridLayout.addWidget(self.noverlap_ui, 3, 8, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(50, 15))
        self.label_3.setMaximumSize(QtCore.QSize(50, 15))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1, QtCore.Qt.AlignRight)
        self.window_ui = QtWidgets.QLineEdit(self.layoutWidget)
        self.window_ui.setMinimumSize(QtCore.QSize(60, 20))
        self.window_ui.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.window_ui.setFont(font)
        self.window_ui.setPlaceholderText("")
        self.window_ui.setObjectName("window_ui")
        self.gridLayout.addWidget(self.window_ui, 4, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setMinimumSize(QtCore.QSize(50, 15))
        self.label_6.setMaximumSize(QtCore.QSize(50, 15))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 2, 1, 1, QtCore.Qt.AlignRight)
        self.detrend_ui = QtWidgets.QLineEdit(self.layoutWidget)
        self.detrend_ui.setMinimumSize(QtCore.QSize(60, 20))
        self.detrend_ui.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.detrend_ui.setFont(font)
        self.detrend_ui.setPlaceholderText("")
        self.detrend_ui.setObjectName("detrend_ui")
        self.gridLayout.addWidget(self.detrend_ui, 4, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setMinimumSize(QtCore.QSize(50, 15))
        self.label_7.setMaximumSize(QtCore.QSize(50, 15))
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 4, 1, 1, QtCore.Qt.AlignRight)
        self.scaling_ui = QtWidgets.QLineEdit(self.layoutWidget)
        self.scaling_ui.setMinimumSize(QtCore.QSize(60, 20))
        self.scaling_ui.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.scaling_ui.setFont(font)
        self.scaling_ui.setPlaceholderText("")
        self.scaling_ui.setObjectName("scaling_ui")
        self.gridLayout.addWidget(self.scaling_ui, 4, 5, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setMinimumSize(QtCore.QSize(50, 15))
        self.label_8.setMaximumSize(QtCore.QSize(50, 15))
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 4, 7, 1, 1, QtCore.Qt.AlignRight)
        self.mode_ui = QtWidgets.QLineEdit(self.layoutWidget)
        self.mode_ui.setMinimumSize(QtCore.QSize(60, 20))
        self.mode_ui.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.mode_ui.setFont(font)
        self.mode_ui.setPlaceholderText("")
        self.mode_ui.setObjectName("mode_ui")
        self.gridLayout.addWidget(self.mode_ui, 4, 8, 1, 1)
        self.line_9 = QtWidgets.QFrame(self.layoutWidget)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.gridLayout.addWidget(self.line_9, 5, 0, 1, 9)
        self.label_27 = QtWidgets.QLabel(self.layoutWidget)
        self.label_27.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_27.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_27.setObjectName("label_27")
        self.gridLayout.addWidget(self.label_27, 6, 0, 1, 1, QtCore.Qt.AlignRight)
        self.applyBandStop_ui = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(60)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.applyBandStop_ui.sizePolicy().hasHeightForWidth())
        self.applyBandStop_ui.setSizePolicy(sizePolicy)
        self.applyBandStop_ui.setMinimumSize(QtCore.QSize(60, 20))
        self.applyBandStop_ui.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.applyBandStop_ui.setText("")
        self.applyBandStop_ui.setTristate(False)
        self.applyBandStop_ui.setObjectName("applyBandStop_ui")
        self.gridLayout.addWidget(self.applyBandStop_ui, 6, 1, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.layoutWidget)
        self.label_28.setMinimumSize(QtCore.QSize(70, 15))
        self.label_28.setMaximumSize(QtCore.QSize(70, 15))
        self.label_28.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_28.setObjectName("label_28")
        self.gridLayout.addWidget(self.label_28, 6, 2, 1, 1, QtCore.Qt.AlignRight)
        self.bandStopLowcut_kHz_ui = QtWidgets.QLineEdit(self.layoutWidget)
        self.bandStopLowcut_kHz_ui.setMinimumSize(QtCore.QSize(60, 20))
        self.bandStopLowcut_kHz_ui.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.bandStopLowcut_kHz_ui.setFont(font)
        self.bandStopLowcut_kHz_ui.setPlaceholderText("")
        self.bandStopLowcut_kHz_ui.setObjectName("bandStopLowcut_kHz_ui")
        self.gridLayout.addWidget(self.bandStopLowcut_kHz_ui, 6, 3, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.layoutWidget)
        self.label_26.setMinimumSize(QtCore.QSize(70, 0))
        self.label_26.setMaximumSize(QtCore.QSize(70, 15))
        self.label_26.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 6, 4, 1, 1, QtCore.Qt.AlignRight)
        self.bandStopHighcut_kHz_ui = QtWidgets.QLineEdit(self.layoutWidget)
        self.bandStopHighcut_kHz_ui.setMinimumSize(QtCore.QSize(60, 20))
        self.bandStopHighcut_kHz_ui.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.bandStopHighcut_kHz_ui.setFont(font)
        self.bandStopHighcut_kHz_ui.setPlaceholderText("")
        self.bandStopHighcut_kHz_ui.setObjectName("bandStopHighcut_kHz_ui")
        self.gridLayout.addWidget(self.bandStopHighcut_kHz_ui, 6, 5, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.layoutWidget)
        self.label_29.setMinimumSize(QtCore.QSize(70, 15))
        self.label_29.setMaximumSize(QtCore.QSize(70, 15))
        self.label_29.setSizeIncrement(QtCore.QSize(0, 0))
        self.label_29.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_29.setObjectName("label_29")
        self.gridLayout.addWidget(self.label_29, 6, 7, 1, 1, QtCore.Qt.AlignRight)
        self.bandStopOrder_ui = QtWidgets.QLineEdit(self.layoutWidget)
        self.bandStopOrder_ui.setMinimumSize(QtCore.QSize(60, 20))
        self.bandStopOrder_ui.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.bandStopOrder_ui.setFont(font)
        self.bandStopOrder_ui.setPlaceholderText("")
        self.bandStopOrder_ui.setObjectName("bandStopOrder_ui")
        self.gridLayout.addWidget(self.bandStopOrder_ui, 6, 8, 1, 1)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 7, 0, 1, 9)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 8, 0, 1, 1, QtCore.Qt.AlignRight)
        self.applyBandPass_ui = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(60)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.applyBandPass_ui.sizePolicy().hasHeightForWidth())
        self.applyBandPass_ui.setSizePolicy(sizePolicy)
        self.applyBandPass_ui.setMinimumSize(QtCore.QSize(60, 20))
        self.applyBandPass_ui.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.applyBandPass_ui.setText("")
        self.applyBandPass_ui.setTristate(False)
        self.applyBandPass_ui.setObjectName("applyBandPass_ui")
        self.gridLayout.addWidget(self.applyBandPass_ui, 8, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setMinimumSize(QtCore.QSize(70, 15))
        self.label_10.setMaximumSize(QtCore.QSize(70, 15))
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 8, 2, 1, 1, QtCore.Qt.AlignRight)
        self.bandPassLowcut_kHz_ui = QtWidgets.QLineEdit(self.layoutWidget)
        self.bandPassLowcut_kHz_ui.setMinimumSize(QtCore.QSize(60, 20))
        self.bandPassLowcut_kHz_ui.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.bandPassLowcut_kHz_ui.setFont(font)
        self.bandPassLowcut_kHz_ui.setPlaceholderText("")
        self.bandPassLowcut_kHz_ui.setObjectName("bandPassLowcut_kHz_ui")
        self.gridLayout.addWidget(self.bandPassLowcut_kHz_ui, 8, 3, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setMinimumSize(QtCore.QSize(70, 15))
        self.label_11.setMaximumSize(QtCore.QSize(70, 15))
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 8, 4, 1, 1, QtCore.Qt.AlignRight)
        self.bandPassHighcut_kHz_ui = QtWidgets.QLineEdit(self.layoutWidget)
        self.bandPassHighcut_kHz_ui.setMinimumSize(QtCore.QSize(60, 20))
        self.bandPassHighcut_kHz_ui.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.bandPassHighcut_kHz_ui.setFont(font)
        self.bandPassHighcut_kHz_ui.setPlaceholderText("")
        self.bandPassHighcut_kHz_ui.setObjectName("bandPassHighcut_kHz_ui")
        self.gridLayout.addWidget(self.bandPassHighcut_kHz_ui, 8, 5, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setMinimumSize(QtCore.QSize(70, 15))
        self.label_12.setMaximumSize(QtCore.QSize(70, 15))
        self.label_12.setSizeIncrement(QtCore.QSize(0, 0))
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 8, 7, 1, 1, QtCore.Qt.AlignRight)
        self.bandPassOrder_ui = QtWidgets.QLineEdit(self.layoutWidget)
        self.bandPassOrder_ui.setMinimumSize(QtCore.QSize(60, 20))
        self.bandPassOrder_ui.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.bandPassOrder_ui.setFont(font)
        self.bandPassOrder_ui.setPlaceholderText("")
        self.bandPassOrder_ui.setObjectName("bandPassOrder_ui")
        self.gridLayout.addWidget(self.bandPassOrder_ui, 8, 8, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.layoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 9, 0, 1, 9)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget)
        self.label_15.setMinimumSize(QtCore.QSize(130, 15))
        self.label_15.setMaximumSize(QtCore.QSize(130, 15))
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 10, 0, 1, 1, QtCore.Qt.AlignRight)
        self.applyDownsampling_ui = QtWidgets.QCheckBox(self.layoutWidget)
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
        self.gridLayout.addWidget(self.applyDownsampling_ui, 10, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget)
        self.label_14.setMinimumSize(QtCore.QSize(80, 0))
        self.label_14.setMaximumSize(QtCore.QSize(60, 15))
        self.label_14.setSizeIncrement(QtCore.QSize(0, 0))
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 10, 2, 1, 1, QtCore.Qt.AlignRight)
        self.targetFrq_kHz_ui = QtWidgets.QLineEdit(self.layoutWidget)
        self.targetFrq_kHz_ui.setMinimumSize(QtCore.QSize(60, 20))
        self.targetFrq_kHz_ui.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.targetFrq_kHz_ui.setFont(font)
        self.targetFrq_kHz_ui.setPlaceholderText("")
        self.targetFrq_kHz_ui.setObjectName("targetFrq_kHz_ui")
        self.gridLayout.addWidget(self.targetFrq_kHz_ui, 10, 3, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.layoutWidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 11, 0, 1, 9)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget)
        self.label_16.setMinimumSize(QtCore.QSize(130, 15))
        self.label_16.setMaximumSize(QtCore.QSize(130, 15))
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 12, 0, 1, 1, QtCore.Qt.AlignRight)
        self.setHistogramLevels_ui = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(60)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.setHistogramLevels_ui.sizePolicy().hasHeightForWidth())
        self.setHistogramLevels_ui.setSizePolicy(sizePolicy)
        self.setHistogramLevels_ui.setMinimumSize(QtCore.QSize(60, 20))
        self.setHistogramLevels_ui.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.setHistogramLevels_ui.setText("")
        self.setHistogramLevels_ui.setTristate(False)
        self.setHistogramLevels_ui.setObjectName("setHistogramLevels_ui")
        self.gridLayout.addWidget(self.setHistogramLevels_ui, 12, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget)
        self.label_17.setMinimumSize(QtCore.QSize(70, 0))
        self.label_17.setMaximumSize(QtCore.QSize(70, 15))
        self.label_17.setSizeIncrement(QtCore.QSize(0, 0))
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 12, 2, 1, 1, QtCore.Qt.AlignRight)
        self.histogramLevelMin_ui = QtWidgets.QLineEdit(self.layoutWidget)
        self.histogramLevelMin_ui.setMinimumSize(QtCore.QSize(60, 20))
        self.histogramLevelMin_ui.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.histogramLevelMin_ui.setFont(font)
        self.histogramLevelMin_ui.setPlaceholderText("")
        self.histogramLevelMin_ui.setObjectName("histogramLevelMin_ui")
        self.gridLayout.addWidget(self.histogramLevelMin_ui, 12, 3, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget)
        self.label_18.setMinimumSize(QtCore.QSize(80, 0))
        self.label_18.setMaximumSize(QtCore.QSize(80, 15))
        self.label_18.setSizeIncrement(QtCore.QSize(0, 0))
        self.label_18.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 12, 4, 1, 1, QtCore.Qt.AlignRight)
        self.histogramLevelMax_ui = QtWidgets.QLineEdit(self.layoutWidget)
        self.histogramLevelMax_ui.setMinimumSize(QtCore.QSize(60, 20))
        self.histogramLevelMax_ui.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.histogramLevelMax_ui.setFont(font)
        self.histogramLevelMax_ui.setPlaceholderText("")
        self.histogramLevelMax_ui.setObjectName("histogramLevelMax_ui")
        self.gridLayout.addWidget(self.histogramLevelMax_ui, 12, 5, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.layoutWidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout.addWidget(self.line_5, 13, 0, 1, 9)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget)
        self.label_19.setMinimumSize(QtCore.QSize(130, 15))
        self.label_19.setMaximumSize(QtCore.QSize(130, 15))
        self.label_19.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 14, 0, 1, 1, QtCore.Qt.AlignRight)
        self.saveHistogramColor_ui = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(60)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.saveHistogramColor_ui.sizePolicy().hasHeightForWidth())
        self.saveHistogramColor_ui.setSizePolicy(sizePolicy)
        self.saveHistogramColor_ui.setMinimumSize(QtCore.QSize(60, 20))
        self.saveHistogramColor_ui.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.saveHistogramColor_ui.setText("")
        self.saveHistogramColor_ui.setTristate(False)
        self.saveHistogramColor_ui.setObjectName("saveHistogramColor_ui")
        self.gridLayout.addWidget(self.saveHistogramColor_ui, 14, 1, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.layoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 15, 0, 1, 9)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setMinimumSize(QtCore.QSize(130, 15))
        self.label_9.setMaximumSize(QtCore.QSize(130, 15))
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 16, 0, 1, 1, QtCore.Qt.AlignRight)
        self.scaleLinLogSqrt_ui = QtWidgets.QComboBox(self.layoutWidget)
        self.scaleLinLogSqrt_ui.setMinimumSize(QtCore.QSize(60, 20))
        self.scaleLinLogSqrt_ui.setMaximumSize(QtCore.QSize(60, 20))
        self.scaleLinLogSqrt_ui.setObjectName("scaleLinLogSqrt_ui")
        self.scaleLinLogSqrt_ui.addItem("")
        self.scaleLinLogSqrt_ui.addItem("")
        self.scaleLinLogSqrt_ui.addItem("")
        self.gridLayout.addWidget(self.scaleLinLogSqrt_ui, 16, 1, 1, 1)
        self.line_6 = QtWidgets.QFrame(self.layoutWidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout.addWidget(self.line_6, 17, 0, 1, 9)
        self.label_20 = QtWidgets.QLabel(self.layoutWidget)
        self.label_20.setMinimumSize(QtCore.QSize(130, 15))
        self.label_20.setMaximumSize(QtCore.QSize(130, 15))
        self.label_20.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 18, 0, 1, 1, QtCore.Qt.AlignRight)
        self.exportSpectrogramToImg_ui = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(60)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.exportSpectrogramToImg_ui.sizePolicy().hasHeightForWidth())
        self.exportSpectrogramToImg_ui.setSizePolicy(sizePolicy)
        self.exportSpectrogramToImg_ui.setMinimumSize(QtCore.QSize(60, 20))
        self.exportSpectrogramToImg_ui.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.exportSpectrogramToImg_ui.setText("")
        self.exportSpectrogramToImg_ui.setTristate(False)
        self.exportSpectrogramToImg_ui.setObjectName("exportSpectrogramToImg_ui")
        self.gridLayout.addWidget(self.exportSpectrogramToImg_ui, 18, 1, 1, 1)
        self.line_7 = QtWidgets.QFrame(self.layoutWidget)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout.addWidget(self.line_7, 19, 0, 1, 9)
        self.getFromUiApplyAndClose_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.getFromUiApplyAndClose_btn.setMinimumSize(QtCore.QSize(50, 20))
        self.getFromUiApplyAndClose_btn.setMaximumSize(QtCore.QSize(50, 20))
        self.getFromUiApplyAndClose_btn.setObjectName("getFromUiApplyAndClose_btn")
        self.gridLayout.addWidget(self.getFromUiApplyAndClose_btn, 20, 5, 1, 1)
        self.saveSettings_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.saveSettings_btn.setMinimumSize(QtCore.QSize(80, 20))
        self.saveSettings_btn.setMaximumSize(QtCore.QSize(80, 20))
        self.saveSettings_btn.setObjectName("saveSettings_btn")
        self.gridLayout.addWidget(self.saveSettings_btn, 20, 6, 1, 2)
        self.resetSetings_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.resetSetings_btn.setMinimumSize(QtCore.QSize(50, 20))
        self.resetSetings_btn.setMaximumSize(QtCore.QSize(50, 20))
        self.resetSetings_btn.setObjectName("resetSetings_btn")
        self.gridLayout.addWidget(self.resetSetings_btn, 20, 8, 1, 1)

        self.retranslateUi(spectrogramSettingsWidget)
        QtCore.QMetaObject.connectSlotsByName(spectrogramSettingsWidget)

    def retranslateUi(self, spectrogramSettingsWidget):
        _translate = QtCore.QCoreApplication.translate
        spectrogramSettingsWidget.setWindowTitle(_translate("spectrogramSettingsWidget", "spectrogramSettings"))
        self.label_24.setText(_translate("spectrogramSettingsWidget", "shot#"))
        self.shotNum_ui.setText(_translate("spectrogramSettingsWidget", "180906039"))
        self.label_21.setText(_translate("spectrogramSettingsWidget", "tree(qoc, qxt1, qsr02)"))
        self.treeName_ui.setText(_translate("spectrogramSettingsWidget", "qoc"))
        self.label_23.setText(_translate("spectrogramSettingsWidget", "start, s"))
        self.startMdsplusTime_ui.setText(_translate("spectrogramSettingsWidget", "*"))
        self.label_25.setText(_translate("spectrogramSettingsWidget", "end, s"))
        self.endMdsplusTime_ui.setText(_translate("spectrogramSettingsWidget", "*"))
        self.label_22.setText(_translate("spectrogramSettingsWidget", "delta, cnt"))
        self.deltaMdsplusTime_ui.setText(_translate("spectrogramSettingsWidget", "*"))
        self.label_2.setText(_translate("spectrogramSettingsWidget", "signal frq, kHz"))
        self.fs_kHz_ui.setText(_translate("spectrogramSettingsWidget", "50"))
        self.label.setText(_translate("spectrogramSettingsWidget", "nfft"))
        self.nfft_ui.setText(_translate("spectrogramSettingsWidget", "256"))
        self.label_4.setText(_translate("spectrogramSettingsWidget", "nperseg"))
        self.nperseg_ui.setText(_translate("spectrogramSettingsWidget", "256"))
        self.label_5.setText(_translate("spectrogramSettingsWidget", "noverlap"))
        self.noverlap_ui.setText(_translate("spectrogramSettingsWidget", "32"))
        self.label_3.setText(_translate("spectrogramSettingsWidget", "window"))
        self.window_ui.setText(_translate("spectrogramSettingsWidget", "hamming"))
        self.label_6.setText(_translate("spectrogramSettingsWidget", "detrend"))
        self.detrend_ui.setText(_translate("spectrogramSettingsWidget", "constant"))
        self.label_7.setText(_translate("spectrogramSettingsWidget", "scaling"))
        self.scaling_ui.setText(_translate("spectrogramSettingsWidget", "density"))
        self.label_8.setText(_translate("spectrogramSettingsWidget", "mode"))
        self.mode_ui.setText(_translate("spectrogramSettingsWidget", "psd"))
        self.label_27.setText(_translate("spectrogramSettingsWidget", "apply bandStop, kHz"))
        self.label_28.setText(_translate("spectrogramSettingsWidget", "lowcut_stop"))
        self.bandStopLowcut_kHz_ui.setText(_translate("spectrogramSettingsWidget", "50"))
        self.label_26.setText(_translate("spectrogramSettingsWidget", "highcut_stop"))
        self.bandStopHighcut_kHz_ui.setText(_translate("spectrogramSettingsWidget", "60"))
        self.label_29.setText(_translate("spectrogramSettingsWidget", "order_stop"))
        self.bandStopOrder_ui.setText(_translate("spectrogramSettingsWidget", "5"))
        self.label_13.setText(_translate("spectrogramSettingsWidget", "apply bandPass, kHz"))
        self.label_10.setText(_translate("spectrogramSettingsWidget", "lowcut_pass"))
        self.bandPassLowcut_kHz_ui.setText(_translate("spectrogramSettingsWidget", "1"))
        self.label_11.setText(_translate("spectrogramSettingsWidget", "highcut_pass"))
        self.bandPassHighcut_kHz_ui.setText(_translate("spectrogramSettingsWidget", "200"))
        self.label_12.setText(_translate("spectrogramSettingsWidget", "order_pass"))
        self.bandPassOrder_ui.setText(_translate("spectrogramSettingsWidget", "5"))
        self.label_15.setText(_translate("spectrogramSettingsWidget", "apply downsampling"))
        self.label_14.setText(_translate("spectrogramSettingsWidget", "target frq, kHz"))
        self.targetFrq_kHz_ui.setText(_translate("spectrogramSettingsWidget", "500"))
        self.label_16.setText(_translate("spectrogramSettingsWidget", "set histogram levels"))
        self.label_17.setText(_translate("spectrogramSettingsWidget", "min(*SxxMax)"))
        self.histogramLevelMin_ui.setToolTip(_translate("spectrogramSettingsWidget", "*SxxMax"))
        self.histogramLevelMin_ui.setText(_translate("spectrogramSettingsWidget", "0.1"))
        self.label_18.setText(_translate("spectrogramSettingsWidget", "max(*SxxMax)"))
        self.histogramLevelMax_ui.setToolTip(_translate("spectrogramSettingsWidget", "*SxxMax"))
        self.histogramLevelMax_ui.setText(_translate("spectrogramSettingsWidget", "1"))
        self.label_19.setText(_translate("spectrogramSettingsWidget", "save histogram color"))
        self.label_9.setText(_translate("spectrogramSettingsWidget", "spectrogram matrix type"))
        self.scaleLinLogSqrt_ui.setItemText(0, _translate("spectrogramSettingsWidget", "linear"))
        self.scaleLinLogSqrt_ui.setItemText(1, _translate("spectrogramSettingsWidget", "log10"))
        self.scaleLinLogSqrt_ui.setItemText(2, _translate("spectrogramSettingsWidget", "sqrt"))
        self.label_20.setText(_translate("spectrogramSettingsWidget", "export spectrogram to png"))
        self.getFromUiApplyAndClose_btn.setText(_translate("spectrogramSettingsWidget", "ok"))
        self.saveSettings_btn.setText(_translate("spectrogramSettingsWidget", "save to file"))
        self.resetSetings_btn.setText(_translate("spectrogramSettingsWidget", "reset"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    spectrogramSettingsWidget = QtWidgets.QWidget()
    ui = Ui_spectrogramSettingsWidget()
    ui.setupUi(spectrogramSettingsWidget)
    spectrogramSettingsWidget.show()
    sys.exit(app.exec_())

