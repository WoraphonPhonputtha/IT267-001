from horse import Horse
from donkey import Donkey

class Mule(Donkey,Horse):
    def __init__(self,name:str,color:str,mh:float,age:int,weight:float) -> None:
        super().__init__(age, weight)
        self.max_height = mh
        self.name = name
        self.color = color
        self.age = age
        self.weight = weight
    
    def run(self):
        print('Mule is running')

    def info(self):
        print(f'***** {self.name} info *****')

    def show_info(self):
        print(f'Name : {self.name}')
        print(f'color : {self.color}')
        print(f'Max Height : {self.max_height}')
        print(f'Age : {self.age} year-old')
        print(f'Weight : {self.weight} kg')