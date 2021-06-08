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
        new_tab=WidTabTemario()
        self.tabListController.addWidget(new_tab,None)
        self.view.tab_widget.insertTab(num_tabs,new_tab,"Nuevo archivo")
        self.view.tab_widget.setCurrentIndex(num_tabs)
        if self.view.tab_widget.count()>0:
            self.view.actionCalendarizar.setDisabled(False)

    def guardar(self):
        current_widget_id=self.view.tab_widget.currentWidget().id
        current_model=self.tabListController.get_model_by_id(current_widget_id)
        if current_model.file:
            current_model.write()
        else:
            self.guardar_como()

    def guardar_como(self):
        current_widget_id=self.view.tab_widget.currentWidget().id
        current_model=self.tabListController.get_model_by_id(current_widget_id)
        file_name=QFileDialog.getSaveFileName(self.view,"Guardar archivo",'.','','',QFileDialog.DontUseNativeDialog)[0]
        current_model.file=file_name
        current_model.write()
        index=self.view.tab_widget.currentIndex()
        self.view.tab_widget.setTabText(index,file_name.split('/')[-1])


    def abrir(self):
        file_name=QFileDialog.getOpenFileName(self.view,
        "Abrir archivo","~","Temarios (*.json)")[0]

        num_tabs=self.view.tab_widget.count()

        print(f"Number of tabs {num_tabs}")

        new_tab=WidTabTemario()
        self.tabListController.addWidget(new_tab,file_name)

        # self.temario_controller=TabTemarioController(new_tab,new_tab.model)

        self.view.tab_widget.insertTab(num_tabs,new_tab,self.file_name.split('/')[-1])
        self.view.tab_widget.setCurrentIndex(num_tabs)
        if self.view.tab_widget.count()>0:
            self.view.actionCalendarizar.setDisabled(False)

        # self.set_form()

    def cerrar(self):
        if self.view.tab_widget.count()>0:
            self.tabListController.close_tab(self.view.tab_widget.currentIndex())

    def salir(self):
        self.view.close()
