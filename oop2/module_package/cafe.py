class Dessert:
    def __init__(self) -> None:
        self.dessert = ['Ice cream','Sticky rice mango']
    
    def show_dessert(self):
        return f'Dessert : {self.dessert}'

class Drink:
    def __init__(self) -> None:
        self.drink = ['Coffee','Tea','Wine','Soda']
    
    def add_drink(self,new_drink:str):
        self.drink.append(new_drink)
    
    def show_drink(self):
        return f'Drink : {self.drink}'