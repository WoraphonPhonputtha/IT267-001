#this file is inside bank package
from bank import customer,account
#from bank.customer import Customer
#from bank.account import Account

cus1 = customer.Customer()
cus1.new_customer()

cus1_acc = account.Account()
cus1_acc.open_account(cus1.name, 'Saving', '123-456-7890',500)

print("***** Open Bank Account Detail *****")
print(cus1.cus_info())
print(cus1_acc.display_balance())