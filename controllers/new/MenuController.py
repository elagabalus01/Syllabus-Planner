
class MenuController:
    def set_menu_controller(self):
        self.view.actionNuevo.triggered.connect(self.nuevo)
        self.view.actionGuardar.triggered.connect(self.guardar)
        self.view.actionGuardar_como.triggered.connect(self.guardar_como)
        self.view.actionAbrir.triggered.connect(self.abrir)
        self.view.actionCerrar.triggered.connect(self.cerrar)
        self.view.actionSalir.triggered.connect(self.salir)
        self.view.actionCalendarizar.triggered.connect(self.calendarizar_dialog)
