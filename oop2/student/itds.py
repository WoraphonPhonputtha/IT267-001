from student import Student
class ITDS(Student):
    def __init__(self, stuid, name, major):
        super().__init__(stuid, name, major)
        
    def _displayNameAndMajor(self):
        print(f'ITDS Name : {self._name}')
        super()._displayNameAndMajor()

stu = ITDS('6412345678', 'Amorn', 'Information Technology')
stu._displayNameAndMajor()
        