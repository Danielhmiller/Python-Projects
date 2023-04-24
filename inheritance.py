class User: 
    name = 'Daniel'
    email = 'danielmiller@gmail.com'
    password = 'bhufierbfb'
    account_id = 1
#the parent class that is inherited by the two classes below it.
    
class Employee(User):
    base_salary = 15.00
    department = 'Sales'
#automatically has the parents attributes so they don't have to be re-typed.

class Customer(User):
    mailing_address = ' '
    mailing_list = True
#automatically has the parents attributes so they don't have to be re-typed.
