from views.view import View
from tkinter.ttk import Style
class TopController(object):
    def __init__(self):
        self.view=View()
        self.view.style = Style()
        #('clam', 'alt', 'default', 'classic')
        self.view.style.theme_use("classic")
        self.view.title("Temario a Json")
        self.view.geometry("546x440+480+150")
        self.file=None
