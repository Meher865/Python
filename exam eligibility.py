medical_cause= input("do you have any medical cause of absense? answer in Y or N")
atten= int(input("please enter your attendance:"))
if medical_cause=='Y': 
 print("You are eligible for the exam")
else:
 if  atten >= 75:
   print("you are eligible for the exam" )
 else:
   print(" you are not eligible for the exam")
