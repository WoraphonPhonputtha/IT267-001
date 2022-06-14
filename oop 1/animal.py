class Animal:
    animal = 'CAT'

    def new_animal(self,name:str,breed:str,color:str,age:int):
        self.name = name
        self.breed = breed
        self.color = color
        self.age = age
    
    def print_detail(self):
        print('---------------')
        print(f"Name : {self.name}")
        print(f"Animal : {self.animal}")
        print(f"Breed : {self.breed}")
        print(f"Color : {self.color}")
        print(f"Age : {self.age}")
    
    def __del__(self):
        print(f'Object was destroyed')

if __name__ == "__main__":
    Animal.animal = 'FISH'
    ula = Animal()
    ula.animal = 'DOG'
    ula.new_animal('Ula', 'Scottish', 'White', 1)
    ula.print_detail()
    
    drac = Animal()
    drac.new_animal('Drac', 'Scottish', 'White', 1)
    drac.print_detail()
    drac.breed = 'Catfish'
    drac.print_detail()

    #เรียกดูข้อมูลของ Object ผ่านชื่อ Class
    Animal.print_detail(ula)
    Animal.print_detail(drac)

    #เรียกดู Class Variable ทั้งหมด
    print(f"{Animal.__dict__}")

    #เรียกดู Instance Variable ทั้งหมด
    print(f"{ula.__dict__}")

    peter = Animal()
    peter.new_animal('Peter', 'Parrot', 'Green-Yellow-Red', 2)
    #add new attribute
    peter.legs = 2
    print(f'{peter.__dict__}')

