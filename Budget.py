Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def calcBills():
    myBills = {'Electic': 120.00, 'Rent': 1200.00, 'Water_Sewer': 60.00,
               'Car Insurance': 75.00, 'Phone': 65.00}
    total = 0
    for i in myBills:
        total+= myBills[i]
    owed = 'The total owed for bills this month is: ${}'.format(total)
    return owed