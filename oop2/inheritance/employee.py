class Employee:
    def __init__(self,id,name,salary) -> None:
        self.id = id
        self.name = name
        self._salary = salary

    def emp_detail(self):
        print(f'Id : {self.id}')
        print(f'Name : {self.name}')

    def _emp_salary(self):
        print(f'Salary : {self._salary} baht')