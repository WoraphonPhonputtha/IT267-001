from project import Project
class Condo(Project):
    def __init__(self, name, time, location, type):
        super().__init__(name, time, location)
        self.type = 'Condo'
        self.__budget = budget #condo's instance variable

    def show(self):
        super().show()
        print(f'Type : {self.type}')
        print(f'Condo Budget : {self.__budget} MB')
        print(f'Project Budget : {self.get_budget()} MB')