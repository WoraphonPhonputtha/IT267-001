class Person:
    country = 'Thailand'
    def __init__(self,name,gender,profession,hours) -> None:
        self.name = name
        self.gender = gender
        self.profession = profession
        self.hours = hours

    def work(self):
        print(f'{self.name} is working as a {self.profession}')

    def study(self):
        print(f'{self.name} studies for {self.hours} hour(s)')

    def show(self):
        print(f'Name : {self.name} Gender : {self.gender} Profession : {self.profession} Study : {self.hours}')

    def __del__(self):
        print(f'Object was destroyed')
        
jessa = Person("Jessa", "Male", "Software Engineer", 10)
jessa.show()
jessa.work()
jessa.study()

Jon = Person("Jon", "Male", "Doctor", 15)
Jon.show()
Jon.work()
Jon.study()

Lisa = Person('Lalisa', 'Female', 'Korean Singer', 13)
Lisa.work()

print(f'Class Variable : {Person.country}')
print(f'Instance Variable : {Lisa.country}')

Lisa.country = 'Korea'
print('---------------')
print(f'Class Variable : {Person.country}')
print(f'Instance Variable : {Lisa.country}')
print(f'Instance Variable : {Jon.country}')

Person.country = 'England'
print('///////////////')
print(f'Class Variable : {Person.country}')
print(f'Instance Variable : {Lisa.country}')
print(f'Instance Variable : {Jon.country}')