from animal import Animal

class Dog(Animal):
    def info(self):
        #super().info()
        Animal.info(self)
        print('I am a dog ')
        print(f'My name is {self.name}.')
        print(f'I am {self.age} years old.')
    
    def make_sound(self):
        Animal.make_sound(self)
        print('Hey! I make Woof! Woof! sound.')

class Cat(Animal):
    def info(self):
        #super().info()
        Animal.info(self)
        print('I am a cat ')
        print(f'My name is {self.name}.')
        print(f'I am {self.age} years old.')
    
    def make_sound(self):
        Animal.make_sound(self)
        print('Hey! I make Meow! Meow! sound.')

class Cow(Animal):
    def info(self):
        #super().info()
        Animal.info(self)
        print('I am a cow ')
        print(f'My name is {self.name}.')
        print(f'I am {self.age} years old.')
  
    def make_sound(self):
        Animal.make_sound(self)
        print('Hey! I make Moo! Moo! sound.')
