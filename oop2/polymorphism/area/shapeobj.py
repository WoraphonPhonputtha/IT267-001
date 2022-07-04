from shapetype import *

#Menu
print('===== Compute Area =====')
print('1) Square')
print('2) Circle')
print('3) Triangle')
choice = int(input('Enter choice : '))
print('=========================')

#check choice
if choice == 1 :
    s = Square()
    s.lenght = float(input('Enter Lenght : '))
    s.print_square()
elif choice == 2 :
    c = Circle()
    c.radius = float(input('Enter Radius : '))
    c.print_circle()
elif choice == 3 :
    t = Triangle()
    t.base = float(input('Enter Base : '))
    t.high = float(input('Enter High : '))
    t.print_triangle()
else:
    print('!!!!! Wrong choice !!!!!')