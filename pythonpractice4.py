num = 3
if num > 0:
    print("This is a positive number")
else:
    print("This is a negative number")

actual_amount = float(input("Please enter the actual Product price:"))
sale_amount = float(input("Please enter the sale Product price"))

if(sale_amount > actual_amount):
    amount = sale_amount - actual_amount
    print("Total Profit = {0}".format(amount))
else:
    print("No profit!!!")    