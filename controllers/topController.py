from views.view import View
class TopController(object):
    def __init__(self):
        self.view=View()
        self.view.title("Temario a Json")
        self.view.geometry("546x440+480+150")
        self.file=None
