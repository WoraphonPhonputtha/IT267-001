class Animal:
    def __init__(self,name,age) -> None:
        self.__name = name
        self.__age = age

    @property #getter of name
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name = value

    @property #getter of age
    def age(self):
        return self.__age
    @age.setter
    def age(self,value):
        self.__age = value

    def info(self):
        print('========== Animal info ==========')
            
    def make_sound(self):
        print('========== Animal sound =========')
