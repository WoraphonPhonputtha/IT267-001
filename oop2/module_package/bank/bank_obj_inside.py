#this file is inside bank package
from customer import Customer
from account import Account

cus1 = Customer()
cus1.new_customer()

cus1_acc = Account()
cus1_acc.open_account(cus1.name, 'Saving', '123-456-7890',500)

print("***** Open Bank Account Detail *****")
print(cus1.cus_info())
print(cus1_acc.display_balance())