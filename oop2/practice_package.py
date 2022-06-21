from cusorder.customer import Customer
from cusorder.order import Order

#create obj 
jame1 = Customer('Jame', 'Nontaburi')
jame2 = Order('15-06-2022', 'packed')

#display info
print(f'Order of {jame1.name} on {jame2.date} is {jame2.status}')