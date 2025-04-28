original_price=float(input("please enter the original price"))
selling_price=float(input("please enter the selling price"))
amount=original_price - selling_price
if (selling_price > amount):
    print("total profit =",amount)
else:
    print("you have made no profit!")
