units= int(input("please enter the number of units you consumed"))
if (units>50):
    amount = units * 2.60
    surcharge=25
elif (units> 100):
    amount= 130+(units-50) * 3.25
    surcharges=35
elif (units>200):
 amount  + 130 + 162.50 + (units - 100) *5.26
 surcharges = 45
else:
   amount= 130 + 162.50 +((units -100)*8.45 )
   surcharge=45
   total= amount + surcharge
print("\n your electricity=%2%f",total)
    