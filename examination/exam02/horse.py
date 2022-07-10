class Horse:
    def __init__(self,mh:float,name:str,color:str) -> None:
        self.max_height = mh
        self.name = name
        self.color = color

    def run(self):
        print(f'{self.name} is running')
    
    def show_name(self):
        print(f'Name : {self.name}')

    def show_info(self):
        print(f'Name : {self.name}')
        print(f'color : {self.color}')
        print(f'Max Height : {self.max_height}')