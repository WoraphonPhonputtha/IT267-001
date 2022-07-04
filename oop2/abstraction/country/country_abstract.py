from abc import ABC,abstractmethod

class Country(ABC):
    def __init__(self,name,pop) -> None:
        super().__init__()
        self.name = name
        self.population = pop
    
    def show_detail(self):
        pass
