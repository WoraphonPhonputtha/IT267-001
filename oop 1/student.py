class Student():
    #major:str = 'IT'
    #major = 'IT'
    #major:'IT' error
    def __init__(self,id:str,name:str,major:str = 'IT') -> None:
        self.id = id
        self.name = name
        self.major = major
    
    def display_detail(self):
        print('---------------')
        print(f'ID : {self.id}')
        print(f'Name : {self.name}')
        print(f'Major : {self.major}')
    
    def __del__(self):
        print(f'Object was destroyed')
    
if __name__ == '__main__':
    jessica = Student('111', 'Jessica', 'IT')
    jessica.display_detail()

    amy = Student('113', 'Amy')
    amy.display_detail()

    john = Student('112', 'John', 'MKT')
    john.display_detail()