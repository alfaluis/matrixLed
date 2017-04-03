# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtDesigner/MatrixLed/displayPortConfiguration.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dialog_port_conf(object):
    def setupUiDialog(self, dialog_port_conf):
        dialog_port_conf.setObjectName("dialog_port_conf")
        dialog_port_conf.setWindowModality(QtCore.Qt.WindowModal)
        dialog_port_conf.setEnabled(True)
        dialog_port_conf.resize(300, 180)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dialog_port_conf.sizePolicy().hasHeightForWidth())
        dialog_port_conf.setSizePolicy(sizePolicy)
        dialog_port_conf.setMinimumSize(QtCore.QSize(300, 180))
        dialog_port_conf.setMaximumSize(QtCore.QSize(300, 180))
        self.verticalLayoutWidget = QtWidgets.QWidget(dialog_port_conf)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 281, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.lbl_port = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_port.setObjectName("lbl_port")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_port)
        self.cmb_ports = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.cmb_ports.setObjectName("cmb_ports")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cmb_ports)
        self.lbl_baud = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_baud.setObjectName("lbl_baud")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_baud)
        self.cmb_baudrate = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.cmb_baudrate.setObjectName("cmb_baudrate")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cmb_baudrate)
        self.cbx_dtr_rst = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.cbx_dtr_rst.setObjectName("cbx_dtr_rst")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.cbx_dtr_rst)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.btn_ok_cancel = QtWidgets.QDialogButtonBox(self.verticalLayoutWidget)
        self.btn_ok_cancel.setOrientation(QtCore.Qt.Horizontal)
        self.btn_ok_cancel.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.btn_ok_cancel.setObjectName("btn_ok_cancel")
        self.verticalLayout.addWidget(self.btn_ok_cancel)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)

        self.retranslateUiDialog(dialog_port_conf)
        self.btn_ok_cancel.accepted.connect(dialog_port_conf.accept)
        self.btn_ok_cancel.rejected.connect(dialog_port_conf.reject)
        QtCore.QMetaObject.connectSlotsByName(dialog_port_conf)

    def retranslateUiDialog(self, dialog_port_conf):
        _translate = QtCore.QCoreApplication.translate
        dialog_port_conf.setWindowTitle(_translate("dialog_port_conf", "Port Configuration"))
        self.lbl_port.setText(_translate("dialog_port_conf", "Serial port to connect to:"))
        self.lbl_baud.setText(_translate("dialog_port_conf", "Baud rate:"))
        self.cbx_dtr_rst.setText(_translate("dialog_port_conf", "Set DTR / RST"))

