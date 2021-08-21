class CareTaker:
    def __init__(self):
        self.memento_list=[]
    def add(self,memento):
        self.memento_list.append(memento)
    def get(self,index):
        try:
            return self.memento_list[index]
        except IndexError:
            return -1
