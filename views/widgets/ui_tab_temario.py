# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './qt_view/tab_temario.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_tab_temario(object):
    def setupUi(self, tab_temario):
        tab_temario.setObjectName("tab_temario")
        tab_temario.resize(898, 503)
        self.gridLayout = QtWidgets.QGridLayout(tab_temario)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(tab_temario)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 882, 566))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.hora_inicio_in = QtWidgets.QTimeEdit(self.scrollAreaWidgetContents)
        self.hora_inicio_in.setMaximumSize(QtCore.QSize(60, 16777215))
        self.hora_inicio_in.setObjectName("hora_inicio_in")
        self.gridLayout_2.addWidget(self.hora_inicio_in, 3, 5, 1, 1)
        self.subtemas_list = QtWidgets.QListWidget(self.scrollAreaWidgetContents)
        self.subtemas_list.setMinimumSize(QtCore.QSize(0, 330))
        self.subtemas_list.setObjectName("subtemas_list")
        self.gridLayout_2.addWidget(self.subtemas_list, 7, 0, 1, 11)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_4.setInputMask("")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_2.addWidget(self.lineEdit_4, 6, 0, 1, 5)
        self.nombre_tema_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nombre_tema_label.sizePolicy().hasHeightForWidth())
        self.nombre_tema_label.setSizePolicy(sizePolicy)
        self.nombre_tema_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.nombre_tema_label.setObjectName("nombre_tema_label")
        self.gridLayout_2.addWidget(self.nombre_tema_label, 5, 4, 1, 1)
        self.horario_box = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horario_box.sizePolicy().hasHeightForWidth())
        self.horario_box.setSizePolicy(sizePolicy)
        self.horario_box.setObjectName("horario_box")
        self.gridLayout_2.addWidget(self.horario_box, 3, 1, 1, 1)
        self.tema_box = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.tema_box.setObjectName("tema_box")
        self.gridLayout_2.addWidget(self.tema_box, 4, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 10, 1, 1)
        self.salon_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.salon_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.salon_label.setObjectName("salon_label")
        self.gridLayout_2.addWidget(self.salon_label, 0, 4, 1, 1)
        self.dia_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dia_label.sizePolicy().hasHeightForWidth())
        self.dia_label.setSizePolicy(sizePolicy)
        self.dia_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dia_label.setObjectName("dia_label")
        self.gridLayout_2.addWidget(self.dia_label, 3, 2, 1, 1)
        self.materia_in = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.materia_in.setObjectName("materia_in")
        self.gridLayout_2.addWidget(self.materia_in, 0, 1, 1, 3)
        self.num_tema_in = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.num_tema_in.setObjectName("num_tema_in")
        self.gridLayout_2.addWidget(self.num_tema_in, 5, 1, 1, 1)
        self.hora_inicio_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.hora_inicio_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.hora_inicio_label.setObjectName("hora_inicio_label")
        self.gridLayout_2.addWidget(self.hora_inicio_label, 3, 4, 1, 1)
        self.horario_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horario_label.sizePolicy().hasHeightForWidth())
        self.horario_label.setSizePolicy(sizePolicy)
        self.horario_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.horario_label.setObjectName("horario_label")
        self.gridLayout_2.addWidget(self.horario_label, 3, 0, 1, 1)
        self.nombre_tema_in = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.nombre_tema_in.setObjectName("nombre_tema_in")
        self.gridLayout_2.addWidget(self.nombre_tema_in, 5, 5, 1, 5)
        self.duracion_tema_in = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.duracion_tema_in.setObjectName("duracion_tema_in")
        self.gridLayout_2.addWidget(self.duracion_tema_in, 5, 3, 1, 1)
        self.color_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.color_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.color_label.setObjectName("color_label")
        self.gridLayout_2.addWidget(self.color_label, 0, 8, 1, 1)
        self.num_tema_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.num_tema_label.setObjectName("num_tema_label")
        self.gridLayout_2.addWidget(self.num_tema_label, 5, 0, 1, 1)
        self.color_box = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.color_box.setObjectName("color_box")
        self.gridLayout_2.addWidget(self.color_box, 0, 9, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 8, 9, 1, 1)
        self.materia_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.materia_label.sizePolicy().hasHeightForWidth())
        self.materia_label.setSizePolicy(sizePolicy)
        self.materia_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.materia_label.setObjectName("materia_label")
        self.gridLayout_2.addWidget(self.materia_label, 0, 0, 1, 1)
        self.tema_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tema_label.sizePolicy().hasHeightForWidth())
        self.tema_label.setSizePolicy(sizePolicy)
        self.tema_label.setObjectName("tema_label")
        self.gridLayout_2.addWidget(self.tema_label, 4, 0, 1, 1)
        self.dia_box = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dia_box.sizePolicy().hasHeightForWidth())
        self.dia_box.setSizePolicy(sizePolicy)
        self.dia_box.setObjectName("dia_box")
        self.gridLayout_2.addWidget(self.dia_box, 3, 3, 1, 1)
        self.duracion_tema_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.duracion_tema_label.sizePolicy().hasHeightForWidth())
        self.duracion_tema_label.setSizePolicy(sizePolicy)
        self.duracion_tema_label.setObjectName("duracion_tema_label")
        self.gridLayout_2.addWidget(self.duracion_tema_label, 5, 2, 1, 1)
        self.salon_in = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.salon_in.setMaximumSize(QtCore.QSize(250, 16777215))
        self.salon_in.setObjectName("salon_in")
        self.gridLayout_2.addWidget(self.salon_in, 0, 5, 1, 2)
        self.hora_fin_in = QtWidgets.QTimeEdit(self.scrollAreaWidgetContents)
        self.hora_fin_in.setMaximumSize(QtCore.QSize(60, 16777215))
        self.hora_fin_in.setObjectName("hora_fin_in")
        self.gridLayout_2.addWidget(self.hora_fin_in, 3, 9, 1, 1)
        self.hora_fin_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.hora_fin_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.hora_fin_label.setObjectName("hora_fin_label")
        self.gridLayout_2.addWidget(self.hora_fin_label, 3, 8, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 3, 10, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(tab_temario)
        QtCore.QMetaObject.connectSlotsByName(tab_temario)

    def retranslateUi(self, tab_temario):
        _translate = QtCore.QCoreApplication.translate
        tab_temario.setWindowTitle(_translate("tab_temario", "Form"))
        self.hora_inicio_in.setDisplayFormat(_translate("tab_temario", "HH:mm"))
        self.lineEdit_4.setPlaceholderText(_translate("tab_temario", "Subtema"))
        self.nombre_tema_label.setText(_translate("tab_temario", "Nombre"))
        self.salon_label.setText(_translate("tab_temario", "Salón"))
        self.dia_label.setText(_translate("tab_temario", "Dia"))
        self.hora_inicio_label.setText(_translate("tab_temario", "Hora inicio"))
        self.horario_label.setText(_translate("tab_temario", "Horario"))
        self.color_label.setText(_translate("tab_temario", "Color"))
        self.num_tema_label.setText(_translate("tab_temario", "Número"))
        self.pushButton.setText(_translate("tab_temario", "PushButton"))
        self.materia_label.setText(_translate("tab_temario", "Materia"))
        self.tema_label.setText(_translate("tab_temario", "Tema"))
        self.duracion_tema_label.setText(_translate("tab_temario", "Duracion"))
        self.hora_fin_in.setDisplayFormat(_translate("tab_temario", "HH:mm"))
        self.hora_fin_label.setText(_translate("tab_temario", "Hora fin"))
        self.pushButton_2.setText(_translate("tab_temario", "Agregar"))