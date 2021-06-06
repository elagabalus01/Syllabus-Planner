# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './qt_view/subtema_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_subtema_dialog(object):
    def setupUi(self, subtema_dialog):
        subtema_dialog.setObjectName("subtema_dialog")
        subtema_dialog.resize(578, 300)
        self.gridLayout = QtWidgets.QGridLayout(subtema_dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.guardar = QtWidgets.QPushButton(subtema_dialog)
        self.guardar.setObjectName("guardar")
        self.gridLayout.addWidget(self.guardar, 1, 1, 1, 1)
        self.cancelar = QtWidgets.QPushButton(subtema_dialog)
        self.cancelar.setObjectName("cancelar")
        self.gridLayout.addWidget(self.cancelar, 1, 0, 1, 1)
        self.edit_subtema = QtWidgets.QPlainTextEdit(subtema_dialog)
        self.edit_subtema.setObjectName("edit_subtema")
        self.gridLayout.addWidget(self.edit_subtema, 0, 0, 1, 2)

        self.retranslateUi(subtema_dialog)
        self.cancelar.pressed.connect(subtema_dialog.close)
        QtCore.QMetaObject.connectSlotsByName(subtema_dialog)

    def retranslateUi(self, subtema_dialog):
        _translate = QtCore.QCoreApplication.translate
        subtema_dialog.setWindowTitle(_translate("subtema_dialog", "Editar subtema"))
        self.guardar.setText(_translate("subtema_dialog", "Guardar"))
        self.cancelar.setText(_translate("subtema_dialog", "Cancelar"))
