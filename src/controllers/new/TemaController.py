from models import Tema,Subtema
from views.widgets.SubtemaDialog import SubtemaDialog
from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5.QtGui import QClipboard
from PyQt5.QtCore import QObject
class TemaController():
    def __init__(self,view,model,clipboard):
        self.clipboard=clipboard
        self.view=view
        self.model=model
        self.bind_slots()
        self.configure_context_menu()

    def configure_context_menu(self):
        self.view.subtemas_list.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.view.subtemas_list.customContextMenuRequested.connect(self.show_menu)

    def eliminar_subtema(self):
        index=self.view.subtemas_list.currentRow()
        subtema=self.view.subtemas_list.takeItem(index)
        subtema=subtema.text()
        # Se determina el tema al que pertenece el subtema
        index=self.view.tema_box.currentIndex()
        num=int(self.view.tema_box.itemText(index))
        print(f"SUbtema a eliminar {num}:{subtema} ")
        self.model.delete_subtema(num,subtema)
        #DELETING FROM MODEL
        self.model.notify_observers(msg="ADD_STATE")

    def show_menu(self):
        print("SHOWING MENU")
        menu=QtWidgets.QMenu()
        action=menu.addAction("Eliminar")
        clipboard=menu.addAction("Copiar tema")
        action.triggered.connect(self.eliminar_subtema)
        clipboard.triggered.connect(self.copia_clipboard)
        menu.exec(QtGui.QCursor.pos())
    def copia_clipboard(self):
        print("Copiando al clipboard")
        id=int(self.view.tema_box.currentText())

        current_tema=self.model.getTemaById(id)
        subtemas=current_tema.subtemas

        subtemas="\n".join([x.nombre for x in subtemas])
        self.clipboard.setText(subtemas)

    def bind_slots(self):
        self.view.btn_agregar_tema.pressed.connect(self.agregar_tema)
        self.view.btn_eliminar_tema.pressed.connect(self.eliminar_tema)
        self.view.subtema_in.returnPressed.connect(self.agregar_subtema)
        self.view.subtemas_list.itemDoubleClicked.connect(self.editar_subtema)
        self.view.tema_box.currentIndexChanged.connect(self.set_current_tema)

    def agregar_tema(self):
        new_tema=Tema()
        num_tema=self.view.num_tema_in.value()
        new_tema.numero=num_tema
        new_tema.tema=self.view.nombre_tema_in.text()
        new_tema.duracion=self.view.duracion_tema_in.value()
        new_tema.subtemas=[] #PROVICIONAL
        new_index=self.view.tema_box.count()

        if self.model.agregar_tema(new_tema):
            # Agrega el id a la lista de temas si no estaba agregado
            self.view.tema_box.insertItem(new_index,str(num_tema))
            print("Agregando tema")
        else:
            print("ya existía el tema tema")
        self.agregar_subtemas()
        print(new_tema)
        self.model.notify_observers(msg="ADD_STATE")

    def eliminar_tema(self):
        print("ELIMINANDO TEMA")
        index=self.view.tema_box.currentIndex()
        num=self.view.tema_box.itemText(index)
        self.model.delete_tema(int(num))
        self.view.tema_box.removeItem(index)
        self.model.notify_observers(msg="ADD_STATE")

    def agregar_subtema(self):
        subtema=self.view.subtema_in.text()
        self.view.subtema_in.clear()
        self.view.subtemas_list.addItem(subtema)
        self.agregar_subtemas()

    def agregar_subtemas(self):
        print("Agregando todos los subtemas")
        subtemas=[]
        for i in range(self.view.subtemas_list.count()):
            nuevo_subtema=Subtema(self.view.subtemas_list.item(i).text())
            subtemas.append(nuevo_subtema)
        id=int(self.view.tema_box.currentText())
        try:
            current_tema=self.model.getTemaById(id)
            current_tema.subtemas=subtemas
        except IndexError:
            if index!=0:
                print("Error al leer el tema actual para agregar subtemas")
            return
        self.model.notify_observers(msg="ADD_STATE")

    def editar_subtema(self,subtema:str):
        texto=""
        dialog=SubtemaDialog(self.view)
        dialog.text.connect(self.update_subtema)
        dialog.edit_subtema.setPlainText(subtema.text())
        dialog.guardar.pressed.connect(dialog.close)
        dialog.exec()

    def update_subtema(self,text):
        print(f"Se va a modificar el text {text}")
        row=self.view.subtemas_list.currentRow()
        item=self.view.subtemas_list.item(row)
        item.setText(text)
        self.agregar_subtemas()


    def set_current_tema(self,index):
        print(f"Current tema changed?{index}")
        id=int(self.view.tema_box.currentText())
        try:
            current_tema=self.model.getTemaById(id)
        except IndexError:
            if index!=0:
                print("Error")
            return
        self.view.subtemas_list.clear()
        self.view.nombre_tema_in.clear()
        self.view.num_tema_in.setValue(current_tema.numero)
        self.view.duracion_tema_in.setValue(current_tema.duracion)
        self.view.nombre_tema_in.insert(current_tema.tema)
        self.view.nombre_tema_in.setCursorPosition(0)
        subtemas=[subtema.nombre for subtema in current_tema.subtemas]
        self.view.subtemas_list.addItems(subtemas)
