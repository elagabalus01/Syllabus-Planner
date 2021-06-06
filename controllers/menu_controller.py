
class MenuController:
    def set_menu_controller(self):
        self.actionNuevo.triggered.connect(self.nuevo)
        self.actionGuardar.triggered.connect(self.guardar)
        self.actionGuardar_como.triggered.connect(self.guardar_como)
        self.actionAbrir.triggered.connect(self.abrir)
        self.actionCerrar.triggered.connect(self.cerrar)
        self.actionSalir.triggered.connect(self.salir)
        self.actionCalendarizar.triggered.connect(self.calendarizar_dialog)
