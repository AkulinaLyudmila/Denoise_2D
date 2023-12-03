# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1126, 895)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_design = QtWidgets.QWidget(Dialog)
        self.widget_design.setObjectName("widget_design")
        self.layout_design = QtWidgets.QVBoxLayout(self.widget_design)
        self.layout_design.setContentsMargins(0, 0, 0, 0)
        self.layout_design.setSpacing(0)
        self.layout_design.setObjectName("layout_design")
        self.widget_menu = QtWidgets.QWidget(self.widget_design)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_menu.sizePolicy().hasHeightForWidth())
        self.widget_menu.setSizePolicy(sizePolicy)
        self.widget_menu.setMinimumSize(QtCore.QSize(0, 140))
        self.widget_menu.setObjectName("widget_menu")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_menu)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_dome_parameters = QtWidgets.QWidget(self.widget_menu)
        self.widget_dome_parameters.setObjectName("widget_dome_parameters")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_dome_parameters)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_text_sigma = QtWidgets.QLabel(self.widget_dome_parameters)
        self.label_text_sigma.setObjectName("label_text_sigma")
        self.gridLayout_2.addWidget(self.label_text_sigma, 2, 0, 1, 1)
        self.lineEdit_dome_amplitude_2 = QtWidgets.QLineEdit(self.widget_dome_parameters)
        self.lineEdit_dome_amplitude_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_dome_amplitude_2.setObjectName("lineEdit_dome_amplitude_2")
        self.gridLayout_2.addWidget(self.lineEdit_dome_amplitude_2, 1, 2, 1, 1)
        self.lineEdit_dome_sigma_2 = QtWidgets.QLineEdit(self.widget_dome_parameters)
        self.lineEdit_dome_sigma_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_dome_sigma_2.setObjectName("lineEdit_dome_sigma_2")
        self.gridLayout_2.addWidget(self.lineEdit_dome_sigma_2, 2, 2, 1, 1)
        self.lineEdit_dome_bias_x_2 = QtWidgets.QLineEdit(self.widget_dome_parameters)
        self.lineEdit_dome_bias_x_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_dome_bias_x_2.setObjectName("lineEdit_dome_bias_x_2")
        self.gridLayout_2.addWidget(self.lineEdit_dome_bias_x_2, 3, 2, 1, 1)
        self.lineEdit_dome_bias_y_2 = QtWidgets.QLineEdit(self.widget_dome_parameters)
        self.lineEdit_dome_bias_y_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_dome_bias_y_2.setObjectName("lineEdit_dome_bias_y_2")
        self.gridLayout_2.addWidget(self.lineEdit_dome_bias_y_2, 4, 2, 1, 1)
        self.lineEdit_dome_sigma_1 = QtWidgets.QLineEdit(self.widget_dome_parameters)
        self.lineEdit_dome_sigma_1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_dome_sigma_1.setObjectName("lineEdit_dome_sigma_1")
        self.gridLayout_2.addWidget(self.lineEdit_dome_sigma_1, 2, 1, 1, 1)
        self.label_text_bias_x = QtWidgets.QLabel(self.widget_dome_parameters)
        self.label_text_bias_x.setObjectName("label_text_bias_x")
        self.gridLayout_2.addWidget(self.label_text_bias_x, 3, 0, 1, 1)
        self.label_text_amplitude = QtWidgets.QLabel(self.widget_dome_parameters)
        self.label_text_amplitude.setObjectName("label_text_amplitude")
        self.gridLayout_2.addWidget(self.label_text_amplitude, 1, 0, 1, 1)
        self.lineEdit_dome_bias_x_1 = QtWidgets.QLineEdit(self.widget_dome_parameters)
        self.lineEdit_dome_bias_x_1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_dome_bias_x_1.setObjectName("lineEdit_dome_bias_x_1")
        self.gridLayout_2.addWidget(self.lineEdit_dome_bias_x_1, 3, 1, 1, 1)
        self.lineEdit_dome_bias_y_1 = QtWidgets.QLineEdit(self.widget_dome_parameters)
        self.lineEdit_dome_bias_y_1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_dome_bias_y_1.setObjectName("lineEdit_dome_bias_y_1")
        self.gridLayout_2.addWidget(self.lineEdit_dome_bias_y_1, 4, 1, 1, 1)
        self.label_text_dome_2 = QtWidgets.QLabel(self.widget_dome_parameters)
        self.label_text_dome_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_text_dome_2.setObjectName("label_text_dome_2")
        self.gridLayout_2.addWidget(self.label_text_dome_2, 0, 2, 1, 1)
        self.label_text_dome_1 = QtWidgets.QLabel(self.widget_dome_parameters)
        self.label_text_dome_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_text_dome_1.setObjectName("label_text_dome_1")
        self.gridLayout_2.addWidget(self.label_text_dome_1, 0, 1, 1, 1)
        self.label_text_bias_y = QtWidgets.QLabel(self.widget_dome_parameters)
        self.label_text_bias_y.setObjectName("label_text_bias_y")
        self.gridLayout_2.addWidget(self.label_text_bias_y, 4, 0, 1, 1)
        self.label_text_dome_3 = QtWidgets.QLabel(self.widget_dome_parameters)
        self.label_text_dome_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_text_dome_3.setObjectName("label_text_dome_3")
        self.gridLayout_2.addWidget(self.label_text_dome_3, 0, 3, 1, 1)
        self.lineEdit_dome_amplitude_3 = QtWidgets.QLineEdit(self.widget_dome_parameters)
        self.lineEdit_dome_amplitude_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_dome_amplitude_3.setObjectName("lineEdit_dome_amplitude_3")
        self.gridLayout_2.addWidget(self.lineEdit_dome_amplitude_3, 1, 3, 1, 1)
        self.lineEdit_dome_sigma_3 = QtWidgets.QLineEdit(self.widget_dome_parameters)
        self.lineEdit_dome_sigma_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_dome_sigma_3.setObjectName("lineEdit_dome_sigma_3")
        self.gridLayout_2.addWidget(self.lineEdit_dome_sigma_3, 2, 3, 1, 1)
        self.lineEdit_dome_bias_x_3 = QtWidgets.QLineEdit(self.widget_dome_parameters)
        self.lineEdit_dome_bias_x_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_dome_bias_x_3.setObjectName("lineEdit_dome_bias_x_3")
        self.gridLayout_2.addWidget(self.lineEdit_dome_bias_x_3, 3, 3, 1, 1)
        self.lineEdit_dome_bias_y_3 = QtWidgets.QLineEdit(self.widget_dome_parameters)
        self.lineEdit_dome_bias_y_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_dome_bias_y_3.setObjectName("lineEdit_dome_bias_y_3")
        self.gridLayout_2.addWidget(self.lineEdit_dome_bias_y_3, 4, 3, 1, 1)
        self.lineEdit_dome_amplitude_1 = QtWidgets.QLineEdit(self.widget_dome_parameters)
        self.lineEdit_dome_amplitude_1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_dome_amplitude_1.setObjectName("lineEdit_dome_amplitude_1")
        self.gridLayout_2.addWidget(self.lineEdit_dome_amplitude_1, 1, 1, 1, 1)
        self.horizontalLayout.addWidget(self.widget_dome_parameters)
        self.widget_buttons_action = QtWidgets.QWidget(self.widget_menu)
        self.widget_buttons_action.setObjectName("widget_buttons_action")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_buttons_action)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_signal = QtWidgets.QPushButton(self.widget_buttons_action)
        self.pushButton_signal.setObjectName("pushButton_signal")
        self.verticalLayout_2.addWidget(self.pushButton_signal)
        self.pushButton_spectrum = QtWidgets.QPushButton(self.widget_buttons_action)
        self.pushButton_spectrum.setObjectName("pushButton_spectrum")
        self.verticalLayout_2.addWidget(self.pushButton_spectrum)
        self.pushButton_recovery = QtWidgets.QPushButton(self.widget_buttons_action)
        self.pushButton_recovery.setObjectName("pushButton_recovery")
        self.verticalLayout_2.addWidget(self.pushButton_recovery)
        self.horizontalLayout.addWidget(self.widget_buttons_action)
        self.layout_design.addWidget(self.widget_menu)
        self.widget_main = QtWidgets.QWidget(self.widget_design)
        self.widget_main.setObjectName("widget_main")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_main)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_plot_1 = QtWidgets.QWidget(self.widget_main)
        self.widget_plot_1.setObjectName("widget_plot_1")
        self.layout_plot_1 = QtWidgets.QVBoxLayout(self.widget_plot_1)
        self.layout_plot_1.setContentsMargins(0, 0, 0, 0)
        self.layout_plot_1.setSpacing(0)
        self.layout_plot_1.setObjectName("layout_plot_1")
        self.gridLayout.addWidget(self.widget_plot_1, 0, 0, 1, 1)
        self.widget_plot_4 = QtWidgets.QWidget(self.widget_main)
        self.widget_plot_4.setObjectName("widget_plot_4")
        self.layout_plot_4 = QtWidgets.QVBoxLayout(self.widget_plot_4)
        self.layout_plot_4.setContentsMargins(0, 0, 0, 0)
        self.layout_plot_4.setSpacing(0)
        self.layout_plot_4.setObjectName("layout_plot_4")
        self.gridLayout.addWidget(self.widget_plot_4, 0, 1, 1, 1)
        self.widget_plot_2 = QtWidgets.QWidget(self.widget_main)
        self.widget_plot_2.setObjectName("widget_plot_2")
        self.layout_plot_2 = QtWidgets.QVBoxLayout(self.widget_plot_2)
        self.layout_plot_2.setContentsMargins(0, 0, 0, 0)
        self.layout_plot_2.setSpacing(0)
        self.layout_plot_2.setObjectName("layout_plot_2")
        self.gridLayout.addWidget(self.widget_plot_2, 1, 0, 1, 1)
        self.widget_plot_3 = QtWidgets.QWidget(self.widget_main)
        self.widget_plot_3.setObjectName("widget_plot_3")
        self.layout_plot_3 = QtWidgets.QVBoxLayout(self.widget_plot_3)
        self.layout_plot_3.setContentsMargins(0, 0, 0, 0)
        self.layout_plot_3.setSpacing(0)
        self.layout_plot_3.setObjectName("layout_plot_3")
        self.gridLayout.addWidget(self.widget_plot_3, 1, 1, 1, 1)
        self.layout_design.addWidget(self.widget_main)
        self.verticalLayout.addWidget(self.widget_design)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_text_sigma.setText(_translate("Dialog", "Сигма"))
        self.lineEdit_dome_amplitude_2.setText(_translate("Dialog", "50"))
        self.lineEdit_dome_sigma_2.setText(_translate("Dialog", "60"))
        self.lineEdit_dome_bias_x_2.setText(_translate("Dialog", "300"))
        self.lineEdit_dome_bias_y_2.setText(_translate("Dialog", "300"))
        self.lineEdit_dome_sigma_1.setText(_translate("Dialog", "30"))
        self.label_text_bias_x.setText(_translate("Dialog", "Смещение по x"))
        self.label_text_amplitude.setText(_translate("Dialog", "Амплитуда"))
        self.lineEdit_dome_bias_x_1.setText(_translate("Dialog", "100"))
        self.lineEdit_dome_bias_y_1.setText(_translate("Dialog", "200"))
        self.label_text_dome_2.setText(_translate("Dialog", "Купол 2"))
        self.label_text_dome_1.setText(_translate("Dialog", "Купол 1"))
        self.label_text_bias_y.setText(_translate("Dialog", "Смещение по y"))
        self.label_text_dome_3.setText(_translate("Dialog", "Купол 3"))
        self.lineEdit_dome_amplitude_3.setText(_translate("Dialog", "70"))
        self.lineEdit_dome_sigma_3.setText(_translate("Dialog", "20"))
        self.lineEdit_dome_bias_x_3.setText(_translate("Dialog", "400"))
        self.lineEdit_dome_bias_y_3.setText(_translate("Dialog", "150"))
        self.lineEdit_dome_amplitude_1.setText(_translate("Dialog", "100"))
        self.pushButton_signal.setText(_translate("Dialog", "Сигнал"))
        self.pushButton_spectrum.setText(_translate("Dialog", "Спектр"))
        self.pushButton_recovery.setText(_translate("Dialog", "Восстановление"))
