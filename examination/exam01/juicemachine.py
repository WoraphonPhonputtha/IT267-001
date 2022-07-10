class JuiceOrder:
    def __init__(self,menu:str,size:str,price:int) -> None:
        self.menu = menu
        self.size = size
        self.price = price

    def check_menu(self):
        menu_dic = {'OJ':25,'AJ':25,'WJ':30,'PJ':30}
        if menu == 'OJ':
            return ['OJ']
        elif menu == 'AJ':
            return ['AJ']
        elif menu == 'WJ':
            return ['WJ']
        elif menu == 'PJ':
            return ['PJ']
    
    def compute_price(self):
        size = size.upper()
        if size == 'L':
            price = price + 5

    def display_order(self):
        print(f'{self.menu}({self.size}*{self.price}) => {self.price} baht')

if __name__ == '__main__':
    order1 = JuiceOrder('WJ', 'L', 35)
    order1.display_order()
    order2 = JuiceOrder('OJ', 'R', 25)
    order2.display_order()
    order3 = JuiceOrder('PJ', 'L', 35)
    order3.display_order()