n= int(input('please enter your number'))
b=' '
for i in range(n):
    if 2**i > n:
        for j in range (i-1,-1,-1):
            b+=str((n >> j)&1)
        break
print(b)
