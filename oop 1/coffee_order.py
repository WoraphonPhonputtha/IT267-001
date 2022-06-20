class CoffeeOrder:
    def __init__(self,customer_name:str,menu_type:str,total:float,menu:str,num:int,size:str,price:float) -> None:
        self.menu_type = 'Coffee'
        self.total = 0
        self.customer_name = customer_name
        self.menu = menu
        self.num = 1
        self.size = 'R'
        self.price = price

    def check_menu(self,menu):
        menu_dictionary = {'CM':5.99,'CP':4.99,'AM':4.99,'CL':4.99,'VL':4.75,'ES':3.00}
        if menu == 'CM':
            return ['CM']
        elif menu == 'CP':
            return ['CP']
        elif menu == 'AM':
            return ['AM']
        elif menu == 'CL':
            return ['CL']
        elif menu == 'VL':
            return ['VL']
        elif menu == 'ES':
            return ['ES']
    def compute_price(size):
        size = size.upper()
        if size == 'L':
            price = price + 1
        elif size == 'XL':
            price = price + 1.5

    def display_detail(self):
        print(f'{customer_name}, {menu} ({num}{size} * ${price}) -> ${total}')

if __name__ == '__main__':
    John = CoffeeOrder('John','Coffee',3.0,'ES',1,'R',3.0)
    John.display_detail()