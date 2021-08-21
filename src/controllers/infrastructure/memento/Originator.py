from .Memento import Memento
class Originator:
    def __init__(self):
        self.state=None
    def set_state(self,state):
        self.state=state
    def save_memento(self):
        return Memento(self.state)
    def set_memento(self,memento):
        self.state=memento.state
