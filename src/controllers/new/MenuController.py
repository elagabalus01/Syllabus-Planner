from PyQt5.QtWidgets import QFileDialog
from views.widgets.WidTabTemario import WidTabTemario
class MenuController:
    def __init__(self,model,view,tabListController):
        self.view=view
        self.model=model
        self.tabListController=tabListController
        self.set_menu_controller()

    def set_menu_controller(self):
        self.view.actionNuevo.triggered.connect(self.nuevo)
        self.view.actionGuardar.triggered.connect(self.guardar)
        self.view.actionGuardar_como.triggered.connect(self.guardar_como)
        self.view.actionAbrir.triggered.connect(self.abrir)
        self.view.actionCerrar.triggered.connect(self.cerrar)
        self.view.actionSalir.triggered.connect(self.salir)

    def nuevo(self):
        num_tabs=self.view.tab_widget.count()
        new_tab=WidTabTemario(self.view)
        self.tabListController.addWidget(new_tab,None)
        self.view.tab_widget.insertTab(num_tabs,new_tab,"Nuevo archivo")
        self.view.tab_widget.setCurrentIndex(num_tabs)
        if self.view.tab_widget.count()>0:
            self.view.actionCalendarizar.setDisabled(False)

    def guardar(self):
        current_widget_id=None
        try:
            current_widget_id=self.view.tab_widget.currentWidget().id
        except AttributeError:
            pass
        if current_widget_id:
            ctrl=self.tabListController.get_controller_by_id(current_widget_id)
            ctrl.serializer.write_file(ctrl.model)

    def guardar_como(self):
        current_widget_id=None
        try:
            current_widget_id=self.view.tab_widget.currentWidget().id
        except AttributeError:
            pass
        if current_widget_id:
            ctrl=self.tabListController.get_controller_by_id(current_widget_id)
            ctrl.serializer.write_as(ctrl.model)

    def abrir(self):
        file_name=QFileDialog.getOpenFileName(self.view,
        "Abrir archivo","","Temarios (*.json)")[0]

        num_tabs=self.view.tab_widget.count()

        print(f"Number of tabs {num_tabs}")
        if len(file_name)>0:
            new_tab=WidTabTemario(self.view)
            self.tabListController.addWidget(new_tab,file_name)

            self.view.tab_widget.insertTab(num_tabs,new_tab,file_name.split('/')[-1])
            self.view.tab_widget.setCurrentIndex(num_tabs)
            if self.view.tab_widget.count()>0:
                self.view.actionCalendarizar.setDisabled(False)

    def cerrar(self):
        if self.view.tab_widget.count()>0:
            self.tabListController.close_tab(self.view.tab_widget.currentIndex())

    def salir(self):
        self.view.close()
