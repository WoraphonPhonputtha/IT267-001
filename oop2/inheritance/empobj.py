from empit import EmpIT
from empmkt import EmpMKT

#create object 
mike = EmpIT('001', 'Mike', 60000)
mike.add_skill('Python, Javascript')
mike.add_experience(5)
mike.emp_detail()
mike.it_salary()

anna = EmpMKT('002', 'Anna', 32000)
anna.emp_detail()
anna.mkt_salary()

#สร้างพนักงานแผนกการตลาดชื่อ Paul โดยที่มีเงินเดือน 45000 ได้คอม 35% โดยทำงานอยู่ Chaingmai
paul = EmpMKT('003', 'Paul', 45000)
paul.add_commission(35)
paul.add_location('Chaing-Mai')
paul.emp_detail()
paul.mkt_salary()
