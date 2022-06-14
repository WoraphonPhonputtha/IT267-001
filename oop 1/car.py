class Car():
    def __init__(self,model,color,year,price) -> None:
        self.model = model
        self.color = color
        self.year = year
        self.price = price

    def print_detail(self):
        print(f'Model : {self.model}')
        print(f'Color : {self.color}')
        print(f'Year : {self.year}')
        print(f'Price : {self.price}')

    def abc(self):
        print(f'Year : {self.year}')

    @classmethod
    def get_class_method(cls,text):
        print(f'This is Class method with {text}')

    @staticmethod
    def get_static_method(text): #มี 1 Argument คือ text
        print(f'String : {text}')

if __name__ == '__main__':
    my_car = Car('Cross', 'White', 2022, 1500000)
    my_car.print_detail()
    #Call Static method
    Car.get_static_method('Hello Class')
    my_car.get_static_method('Good car Object')
    #Call Class method
    Car.get_class_method('Go Home')
