from geographic import Geographic
from temperature import Temperature

class Country(Geographic,Temperature):
    def __init__(self,name,area,pop) -> None:
        #super().__init__()
        Geographic.__init__(self)
        Temperature.__init__(self)
        self.name = name
        self.area = area
        self.population = pop
        #ถ้าใช้ super ในวงเล็บไม่ต้องมีอะไรเลยแต่ถ้าใช้ class ต้องมี self เสมอ
    """def __init__(self,name,area,pop) -> None:
        self.name = name
        self.area = area
        self.population = pop"""
    
    def getpopulationdensity(self):
        return self.population / self.area

    def showdetail(self):
        print(f'Country : {self.name}')
        print(f'Location : {self.getcordinate()}')
        
        print(f'Population : {self.population:,d}')
        print(f'Area : {self.area:.2f}')
        print(f'Density : {self.getpopulationdensity():.2f}')
        
        print(f'Timezone : {self.gettimezone()}')
        print(f'CLimate : {self.getclimate()}')
        print(f'Temperature(C) : {self.getcelcius():.2f}')
        print(f'Temperature(F) : {self.getfahrenheit():.2f}')
        print(f'Weather : {self.getweather()}')

        print('------------------------------------')
