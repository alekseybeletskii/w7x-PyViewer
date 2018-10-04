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
        spectrogramSettingsWidget.resize(263, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(spectrogramSettingsWidget.sizePolicy().hasHeightForWidth())
        spectrogramSettingsWidget.setSizePolicy(sizePolicy)
        spectrogramSettingsWidget.setMinimumSize(QtCore.QSize(263, 200))
        spectrogramSettingsWidget.setMaximumSize(QtCore.QSize(263, 200))
        self.widget = QtWidgets.QWidget(spectrogramSettingsWidget)
        self.widget.setGeometry(QtCore.QRect(0, 10, 261, 181))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMinimumSize(QtCore.QSize(50, 15))
        self.label.setMaximumSize(QtCore.QSize(20, 15))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.nfft_ui = QtWidgets.QLineEdit(self.widget)
        self.nfft_ui.setMinimumSize(QtCore.QSize(60, 20))
        self.nfft_ui.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.nfft_ui.setFont(font)
        self.nfft_ui.setPlaceholderText("")
        self.nfft_ui.setObjectName("nfft_ui")
        self.gridLayout.addWidget(self.nfft_ui, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setMinimumSize(QtCore.QSize(50, 15))
        self.label_2.setMaximumSize(QtCore.QSize(50, 15))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.fs_kHz_ui = QtWidgets.QLineEdit(self.widget)
        self.fs_kHz_ui.setMinimumSize(QtCore.QSize(60, 20))
        self.fs_kHz_ui.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.fs_kHz_ui.setFont(font)
        self.fs_kHz_ui.setPlaceholderText("")
        self.fs_kHz_ui.setObjectName("fs_kHz_ui")
        self.gridLayout.addWidget(self.fs_kHz_ui, 0, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setMinimumSize(QtCore.QSize(50, 15))
        self.label_3.setMaximumSize(QtCore.QSize(20, 15))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.window_ui = QtWidgets.QLineEdit(self.widget)
        self.window_ui.setMinimumSize(QtCore.QSize(60, 20))
        self.window_ui.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.window_ui.setFont(font)
        self.window_ui.setPlaceholderText("")
        self.window_ui.setObjectName("window_ui")
        self.gridLayout.addWidget(self.window_ui, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setMinimumSize(QtCore.QSize(50, 15))
        self.label_4.setMaximumSize(QtCore.QSize(20, 15))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1)
        self.nperseg_ui = QtWidgets.QLineEdit(self.widget)
        self.nperseg_ui.setMinimumSize(QtCore.QSize(60, 20))
        self.nperseg_ui.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.nperseg_ui.setFont(font)
        self.nperseg_ui.setPlaceholderText("")
        self.nperseg_ui.setObjectName("nperseg_ui")
        self.gridLayout.addWidget(self.nperseg_ui, 1, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setMinimumSize(QtCore.QSize(55, 15))
        self.label_5.setMaximumSize(QtCore.QSize(55, 15))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.noverlap_ui = QtWidgets.QLineEdit(self.widget)
        self.noverlap_ui.setMinimumSize(QtCore.QSize(60, 20))
        self.noverlap_ui.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.noverlap_ui.setFont(font)
        self.noverlap_ui.setPlaceholderText("")
        self.noverlap_ui.setObjectName("noverlap_ui")
        self.gridLayout.addWidget(self.noverlap_ui, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setMinimumSize(QtCore.QSize(50, 15))
        self.label_6.setMaximumSize(QtCore.QSize(20, 15))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 2, 1, 1)
        self.detrend_ui = QtWidgets.QLineEdit(self.widget)
        self.detrend_ui.setMinimumSize(QtCore.QSize(60, 20))
        self.detrend_ui.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.detrend_ui.setFont(font)
        self.detrend_ui.setPlaceholderText("")
        self.detrend_ui.setObjectName("detrend_ui")
        self.gridLayout.addWidget(self.detrend_ui, 2, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setMinimumSize(QtCore.QSize(50, 15))
        self.label_7.setMaximumSize(QtCore.QSize(20, 15))
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.scaling_ui = QtWidgets.QLineEdit(self.widget)
        self.scaling_ui.setMinimumSize(QtCore.QSize(60, 20))
        self.scaling_ui.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.scaling_ui.setFont(font)
        self.scaling_ui.setPlaceholderText("")
        self.scaling_ui.setObjectName("scaling_ui")
        self.gridLayout.addWidget(self.scaling_ui, 3, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setMinimumSize(QtCore.QSize(50, 15))
        self.label_8.setMaximumSize(QtCore.QSize(20, 15))
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 2, 1, 1)
        self.mode_ui = QtWidgets.QLineEdit(self.widget)
        self.mode_ui.setMinimumSize(QtCore.QSize(60, 20))
        self.mode_ui.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.mode_ui.setFont(font)
        self.mode_ui.setPlaceholderText("")
        self.mode_ui.setObjectName("mode_ui")
        self.gridLayout.addWidget(self.mode_ui, 3, 3, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setMinimumSize(QtCore.QSize(50, 15))
        self.label_9.setMaximumSize(QtCore.QSize(20, 15))
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 1)
        self.scaleLinLogSqrt = QtWidgets.QComboBox(self.widget)
        self.scaleLinLogSqrt.setMinimumSize(QtCore.QSize(60, 20))
        self.scaleLinLogSqrt.setMaximumSize(QtCore.QSize(60, 20))
        self.scaleLinLogSqrt.setObjectName("scaleLinLogSqrt")
        self.scaleLinLogSqrt.addItem("")
        self.scaleLinLogSqrt.addItem("")
        self.scaleLinLogSqrt.addItem("")
        self.gridLayout.addWidget(self.scaleLinLogSqrt, 4, 1, 1, 1)
        self.resetSetings_btn = QtWidgets.QPushButton(self.widget)
        self.resetSetings_btn.setMinimumSize(QtCore.QSize(50, 20))
        self.resetSetings_btn.setMaximumSize(QtCore.QSize(50, 20))
        self.resetSetings_btn.setObjectName("resetSetings_btn")
        self.gridLayout.addWidget(self.resetSetings_btn, 5, 3, 1, 1)
        self.saveSettings_btn = QtWidgets.QPushButton(self.widget)
        self.saveSettings_btn.setMinimumSize(QtCore.QSize(50, 20))
        self.saveSettings_btn.setMaximumSize(QtCore.QSize(50, 20))
        self.saveSettings_btn.setObjectName("saveSettings_btn")
        self.gridLayout.addWidget(self.saveSettings_btn, 5, 2, 1, 1)

        self.retranslateUi(spectrogramSettingsWidget)
        QtCore.QMetaObject.connectSlotsByName(spectrogramSettingsWidget)

    def retranslateUi(self, spectrogramSettingsWidget):
        _translate = QtCore.QCoreApplication.translate
        spectrogramSettingsWidget.setWindowTitle(_translate("spectrogramSettingsWidget", "spectrogramSettings"))
        self.label.setText(_translate("spectrogramSettingsWidget", "nfft"))
        self.nfft_ui.setText(_translate("spectrogramSettingsWidget", "256"))
        self.label_2.setText(_translate("spectrogramSettingsWidget", "fs,kHz"))
        self.fs_kHz_ui.setText(_translate("spectrogramSettingsWidget", "1000"))
        self.label_3.setText(_translate("spectrogramSettingsWidget", "window"))
        self.window_ui.setText(_translate("spectrogramSettingsWidget", "hamming"))
        self.label_4.setText(_translate("spectrogramSettingsWidget", "nperseg"))
        self.nperseg_ui.setText(_translate("spectrogramSettingsWidget", "256"))
        self.label_5.setText(_translate("spectrogramSettingsWidget", "noverlap"))
        self.noverlap_ui.setText(_translate("spectrogramSettingsWidget", "32"))
        self.label_6.setText(_translate("spectrogramSettingsWidget", "detrend"))
        self.detrend_ui.setText(_translate("spectrogramSettingsWidget", "constant"))
        self.label_7.setText(_translate("spectrogramSettingsWidget", "scaling"))
        self.scaling_ui.setText(_translate("spectrogramSettingsWidget", "density"))
        self.label_8.setText(_translate("spectrogramSettingsWidget", "mode"))
        self.mode_ui.setText(_translate("spectrogramSettingsWidget", "psd"))
        self.label_9.setText(_translate("spectrogramSettingsWidget", "type"))
        self.scaleLinLogSqrt.setItemText(0, _translate("spectrogramSettingsWidget", "linear"))
        self.scaleLinLogSqrt.setItemText(1, _translate("spectrogramSettingsWidget", "log10"))
        self.scaleLinLogSqrt.setItemText(2, _translate("spectrogramSettingsWidget", "sqrt"))
        self.resetSetings_btn.setText(_translate("spectrogramSettingsWidget", "reset"))
        self.saveSettings_btn.setText(_translate("spectrogramSettingsWidget", "save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    spectrogramSettingsWidget = QtWidgets.QWidget()
    ui = Ui_spectrogramSettingsWidget()
    ui.setupUi(spectrogramSettingsWidget)
    spectrogramSettingsWidget.show()
    sys.exit(app.exec_())

