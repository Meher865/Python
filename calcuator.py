def add(p,q):
    return p+q
def subtract(p,q):
    return p-q
def multiply(p,q):
    return p*q
def divide(p,q):
    return p/q
print("plese select your operation: a=addition b=subtraction c= multiplication d=divide")
choice=input("please enter your operation(a/b/c/d):")
num1=int(input("please enter your 1st number:"))
num2=int(input("please enter your 2nd number:"))
if choice=="a":
  print(num1,"+",num2,"=",add (num1,num2))
elif choice=="b":
    print(num1,"-",num2,"=" ,subtract(num1,num2))
elif choice=="c":
    print(num1,"*" ,num2, "=",multiply(num1,num2))
elif choice=="d":
    print(num1,"/" ,num2, "=",divide(num1,num2))  
else:
    print("invalid input")
