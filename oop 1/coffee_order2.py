class CoffeeOrder:
    #Class variable
    menu_type = 'Coffee'
    total = 0
    def __init__(self,customer_name:str,menu:str,num:int=1,size:str='R') -> None:
        self.customer_name = customer_name
        self.menu = menu.upper()
        self.num = num
        self.size = size.upper()
        #ยังไม่ต้องกำหนดก็ได้
        self.price = 0
    
    def check_menu(self):
        menu_dictionary = {
            'CM':5.99,
            'CP':4.99,
            'AM':4.99,
            'CL':4.99,
            'VL':4.75,
            'ES':3.00}
        if self.menu == 'CM':
            self.price = menu_dictionary.get('CM')
        elif self.menu == 'CP':
            self.price = menu_dictionary.get('CP')
        elif self.menu == 'AM':
            self.price = menu_dictionary.get('AM')
        elif self.menu == 'CL':
            self.price = menu_dictionary.get('CL')
        elif self.menu == 'VL':
            self.price = menu_dictionary.get('VL')
        elif self.menu == 'ES':
            self.price = menu_dictionary.get('ES')
        else:
            print('=================================')
    
    def compute_price(self):
        if self.size == 'L':
            self.price += 1
        elif self.size == 'XL':
            self.price += 1.5
        else:
            self.price
        
        #คำนวณราคาทั้งหมด = จำนวนแก้ว * ราคา
        CoffeeOrder.total = self.num * self.price
    
    def display_detail(self):
        self.check_menu()
        self.compute_price()
        return f'{self.customer_name}, {self.menu} ({self.num}{self.size} * ${self.price}) -> ${CoffeeOrder.total}'
    
    def __del__(self):
        print(f'Object was destroyed')

if __name__ == '__main__':
    order1 = CoffeeOrder('John','es',1,'R')
    print(order1.display_detail())
    order2 = CoffeeOrder('Mary','am',2,'L')
    print(order2.display_detail())