
class MenuController:
    def set_menu_controller(self):
        self.actionAbrir.triggered.connect(self.abrir)
        self.actionCerrar.triggered.connect(self.cerrar)
        self.actionSalir.triggered.connect(self.salir)
