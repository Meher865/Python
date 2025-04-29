hight= float(input("please enter your hight in meters"))
weight= float(input("please enter your weight in KGs"))
bmi= weight / (hight/100) **2
print ("your BMI is :",bmi)
if bmi >= 18.5:
 print("You are underweight")
elif bmi <= 24.9:
 print(" You are healthy")
elif bmi<= 29.9:
 print ("You are overweight")
else:
 print("You are Obese")