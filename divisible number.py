nume= int(input("please enter a numerator:"))
deno= int(input("please enter a denominator:"))
if nume%deno==0:
    print("\n" +str(nume)+"is devisible by "+str(deno))
else:
    print("\n"+str(nume)+"is not devisible by"+str(deno))