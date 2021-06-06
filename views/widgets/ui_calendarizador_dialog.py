# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './qt_view/calendarizador_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CalendarizadorDialog(object):
    def setupUi(self, CalendarizadorDialog):
        CalendarizadorDialog.setObjectName("CalendarizadorDialog")
        CalendarizadorDialog.resize(401, 300)
        self.gridLayout = QtWidgets.QGridLayout(CalendarizadorDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.fecha_in = QtWidgets.QDateEdit(CalendarizadorDialog)
        self.fecha_in.setMaximumSize(QtCore.QSize(100, 16777215))
        self.fecha_in.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.fecha_in.setObjectName("fecha_in")
        self.gridLayout.addWidget(self.fecha_in, 1, 4, 1, 1)
        self.cal_in = QtWidgets.QLineEdit(CalendarizadorDialog)
        self.cal_in.setObjectName("cal_in")
        self.gridLayout.addWidget(self.cal_in, 0, 4, 1, 1)
        self.cal_lab = QtWidgets.QLabel(CalendarizadorDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cal_lab.sizePolicy().hasHeightForWidth())
        self.cal_lab.setSizePolicy(sizePolicy)
        self.cal_lab.setObjectName("cal_lab")
        self.gridLayout.addWidget(self.cal_lab, 0, 0, 1, 3)
        self.semanas_in = QtWidgets.QSpinBox(CalendarizadorDialog)
        self.semanas_in.setMaximumSize(QtCore.QSize(51, 16777215))
        self.semanas_in.setObjectName("semanas_in")
        self.gridLayout.addWidget(self.semanas_in, 2, 4, 1, 1)
        self.btn_calendarizar = QtWidgets.QPushButton(CalendarizadorDialog)
        self.btn_calendarizar.setObjectName("btn_calendarizar")
        self.gridLayout.addWidget(self.btn_calendarizar, 2, 5, 1, 1)
        self.semana_lab = QtWidgets.QLabel(CalendarizadorDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.semana_lab.sizePolicy().hasHeightForWidth())
        self.semana_lab.setSizePolicy(sizePolicy)
        self.semana_lab.setObjectName("semana_lab")
        self.gridLayout.addWidget(self.semana_lab, 2, 0, 1, 1)
        self.fecha_lab = QtWidgets.QLabel(CalendarizadorDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fecha_lab.sizePolicy().hasHeightForWidth())
        self.fecha_lab.setSizePolicy(sizePolicy)
        self.fecha_lab.setObjectName("fecha_lab")
        self.gridLayout.addWidget(self.fecha_lab, 1, 0, 1, 1)

        self.retranslateUi(CalendarizadorDialog)
        QtCore.QMetaObject.connectSlotsByName(CalendarizadorDialog)

    def retranslateUi(self, CalendarizadorDialog):
        _translate = QtCore.QCoreApplication.translate
        CalendarizadorDialog.setWindowTitle(_translate("CalendarizadorDialog", "Calendarizar"))
        self.fecha_in.setDisplayFormat(_translate("CalendarizadorDialog", "dd/MM/yyyy"))
        self.cal_in.setPlaceholderText(_translate("CalendarizadorDialog", "Nombre del calendario"))
        self.cal_lab.setText(_translate("CalendarizadorDialog", "Calendario"))
        self.btn_calendarizar.setText(_translate("CalendarizadorDialog", "Calendarizar"))
        self.semana_lab.setText(_translate("CalendarizadorDialog", "Semanas"))
        self.fecha_lab.setText(_translate("CalendarizadorDialog", "Fecha inico"))
