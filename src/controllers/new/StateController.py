from models.infrastructure.observer import Observer
from controllers.infrastructure import memento
import copy
class StateController(Observer):
    def __init__(self,observable):
        super().__init__(observable)
        self.state_admin=memento.Originator()
        self.state_list=memento.CareTaker()
        self.num_states=0
        self.current_state=0

    def notify(self, observable, *args, **kwargs):
        if kwargs['msg']=="ADD_STATE":
            new_state=observable
            self.add_state(new_state)

    def add_state(self,model):
        print("Agregando estado")
        print(f"Num estados {self.num_states}")
        self.num_states=self.num_states+1
        self.current_state=self.current_state+1
        self.state_admin.set_state(model)
        self.state_list.add(self.state_admin.save_memento())

    def get_next_state(self):
        if self.current_state<self.num_states:
            self.current_state=self.current_state+1
            print(f"Estado actual {self.current_state} de {self.num_states}")
            return self.get_state(self.current_state)

    def get_previus_state(self):
        if self.current_state>0:
            self.current_state=self.current_state-1
            print(f"Estado actual {self.current_state} de {self.num_states}")
            return self.get_state(self.current_state)

    def get_state(self,i):
        return self.state_list.get(i).getState()
