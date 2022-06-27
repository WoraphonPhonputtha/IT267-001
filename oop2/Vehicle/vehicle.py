class Vehicle:
    def __init__(self,name,wheels,max_speed,vin) -> None:
        self.name = name
        self.wheels = wheels
        self._max_speed = max_speed
        self.__vin = vin

    def set_vin(self,vin):
        self.__vin = vin
        
    def v_detail(self):
        print('-----------------')
        print(f'Name : {self.name}')
        print('-----------------')
        print(f'Wheels : {self.wheels}')
        print(f'Max_speed : {self._max_speed}')
        print(f'Vin : {self.__vin}')